#!/usr/bin/env python3

#
# main.py - Main execution logic.
#

from genericpath import exists
from os import walk

import requests
import sys
import time

from config import *
from const import *
from file import *
from lookup import *


try:
    print("\nReplaying attack data for TTP ID:", sys.argv[1])
except: 
    print("No TTP ID specified as a CLI argument (i.e. main.py T1059.001). Exiting")
    exit()

log_directory_path = data_file_location + sys.argv[1] + "/"
print("Log Directory Path:", log_directory_path)

f = []
for (dirpath, dirnames, filenames) in walk(log_directory_path):
    f.extend(filenames)
    break

f.remove(".DS_Store")

if len(f)> 0:
    print("Found these files:", f)
else: 
    print("No log files found in path")
    exit()

# Open a persistent tcp session to Splunk HEC 
session = requests.session()
print("\n-----")

for file_name in f:
    if debug:
        print("File Name:", file_name)

    file_key = file_name.rstrip(".log")
    if debug:
        print("File Key:", file_key)

    if file_to_sourcetype_lookup[file_key] is not None:
        if debug:
            print("Sourcetype Match:", file_to_sourcetype_lookup[file_key])

    else:
        print("Sourcetype match not found in file_to_sourcetype_lookup")
        exit()


    data_file_path = log_directory_path + file_name
    data_file_length = get_data_file_length(data_file_path)
    current_line = 1
    event_json_storage = ""


    print("Writing", data_file_path, "to", splunk_index, "(", data_file_length, "lines )" )

    while current_line <= data_file_length:
        current_event = get_line(data_file_path, current_line)

        event_json = {
            "time": time.time(), 
            "index": splunk_index, 
            "host": splunk_host,
            "source": file_name, 
            "sourcetype":file_to_sourcetype_lookup[file_key],  
            "event": current_event }        

        # Group events together for sending as a batch
        event_json_storage += json.dumps(event_json) + "\r\n"

         # Mod the currentLine to send as a batch per the eventsPerHecBatch factor
        if current_line % events_per_hec_batch == 0:                        
            r = session.post(splunk_url, headers=splunk_auth_header, data=event_json_storage, verify=False)
            event_json_storage = ""
        
        current_line += 1

    # Clear out event storage after while is done to catch remaining events
    r = session.post(splunk_url, headers=splunk_auth_header, data=event_json_storage, verify=False)
    event_json_storage = ""

    print("Done with", data_file_path, "to", splunk_index, "index (", data_file_length, "lines )" )
    print("-----\n")

session.close()
