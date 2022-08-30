#!/usr/bin/env python3

#
# main.py - Main execution logic.
#

from os import walk

import json
import requests
import sys
import time

from config import *
from const import *
from file import *
from lookup import *


# TTP ID (argv[1])
# Bring in the TTP ID from arguments
try:
    ttp_id = sys.argv[1]
    print("\nTTP ID:", sys.argv[1])
except: 
    print("No TTP ID specified as a CLI argument (i.e. main.py T1059.001). Exiting")
    exit()

# Find all of the data sample types in the TTP ID path
# i.e. ./data/T1059.001/<data_types>/filename.log
ttp_id_path = data_home_path + ttp_id + "/"
data_source_list = []
for (dirpath, dirnames, filenames) in walk(ttp_id_path):
    data_source_list.extend(dirnames)
    break
data_source_list.sort()
print("TTP Path:", ttp_id_path)


# Data Source ID (argv[1])
# Check that the data source has been passed in as the second argument
try: 
    if sys.argv[2] is not None: 
        data_source_id = sys.argv[2]
        print("Data Source ID:", sys.argv[2])

# Exit with helpful info if a data source was not passed in
except:
    print("\nNo data source was passed via arguments.")
    print("Please choose an option below:")
    print("./data/" + ttp_id + "/<data_source>/file.log\n")
    for item in data_source_list:
        print(item)
    print()
    exit()

data_source_path = ttp_id_path + data_source_id + "/"
print("Data Source Path:", data_source_path)


# Given the full path, generate a list of file names
file_list = []
for (dirpath, dirnames, filenames) in walk(data_source_path):
    file_list.extend(filenames)
    break

# File list cleanup (remove .yml and .DS_Store)
file_list = [ item for item in file_list if not ".yml" in item ]
ds_store_string = ".DS_Store"
if ds_store_string in file_list:
    file_list.remove(ds_store_string)

# Check that we have at least one item remaining in the file list
if len(file_list)> 0:
    print("Found these files:", file_list)
else: 
    print("No log files found in path")
    exit()

# Open a persistent tcp session to Splunk HEC 
session = requests.session()

# For each file in the file list
for file_name in file_list:
    print("\n-----")
    print("File Name:", file_name)

    file_key = file_name.replace(".log", "")
    print("File Key:", file_key)

    # If we don't have a file key to sourcetype match, wait for the next item
    if file_key not in file_to_sourcetype_lookup.keys():
        print("Sourcetype match not found for", file_key)
        print("-----")

    # If we have a file key to sourcetype match, continue
    if file_key in file_to_sourcetype_lookup.keys():

        sourcetype = file_to_sourcetype_lookup[file_key]
        print("Sourcetype Match:", file_to_sourcetype_lookup[file_key])

        if file_key in file_to_source_lookup.keys():
            source = file_to_source_lookup[file_key]
        else:
            source = file_name

        data_file_path = data_source_path + file_name
        data_file_length = get_data_file_length(data_file_path)
        current_line = 1
        event_json_storage = ""


        print("Writing", data_file_path, "to", splunk_index, "(", data_file_length, "lines )" )

        # For each line in the current file
        while current_line <= data_file_length:
            
            current_event = get_line(data_file_path, current_line)

            event_json = {
                "time": time.time(), 
                "index": splunk_index, 
                "host": splunk_host,
                "source": source, 
                "sourcetype": sourcetype,  
                "event": current_event }        

            # Group events together for sending as a batch
            event_json_storage += json.dumps(event_json) + "\r\n"

            # Mod the currentLine to send as a batch per the eventsPerHecBatch factor
            if current_line % events_per_hec_batch == 0:                        
                r = session.post(splunk_url, headers=splunk_auth_header, data=event_json_storage, verify=False)
                event_json_storage = ""
            
            current_line += 1

        # Send remaining events in event_json_storage to HEC after the while loop concludes
        r = session.post(splunk_url, headers=splunk_auth_header, data=event_json_storage, verify=False)
        event_json_storage = ""

        print("Done with", data_file_path, "to", splunk_index, "index (", data_file_length, "lines )" )
        print("-----")

session.close()
