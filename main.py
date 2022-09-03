#!/usr/bin/env python3

#
# main.py - Main execution logic.
#


import json
import os
import requests
import sys
import time

from os import walk

from config import *
from const import *
from file import *
from lookup import *


# Get file base path in arguments
try:
    data_path = data_home_path + sys.argv[1]
    absolute_path = os.path.dirname(__file__)
    print("\nBase Path:", data_path)
    print("Absolute Path:", absolute_path + data_path)
except: 
    print("No base file path specified. Exiting")
    exit()

print("")


# Make an alphabetical list of all files in the base directory
file_list = []
for (dirpath, dirnames, filenames) in walk(absolute_path + "/" + data_path):
    file_list += [os.path.join(dirpath, file) for file in filenames]
file_list.sort()

# File list cleanup (remove .yml, .txt, and .DS_Store)
file_list = [ item for item in file_list if not ".yml" in item ]
file_list = [ item for item in file_list if not ".yaml" in item ]
file_list = [ item for item in file_list if not ".txt" in item ]
file_list = [ item for item in file_list if not ".DS_Store" in item ]

# Print out the final file list to the console
print("File List:")
for item in file_list:
    item = item.replace(absolute_path + "/", "")
    print(item)

# Check that we have at least one item remaining in the file list
if len(file_list) == 0:
    print("No log files found in path")
    exit()

time.sleep(5)


# Open a persistent tcp session to Splunk HEC 
session = requests.session()

# For each file in the file list
for file_path in file_list:

    print("\n-----")
    print("File Path:", file_path)

    file_name = os.path.basename(file_path)
    print("File Name:", file_name)

    file_key = os.path.splitext(file_name)[0]
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

        # Handle sourcetypes that are multiline and need the raw HEC endpoint
        splunk_hec_mode = "event"
        if sourcetype.startswith("WinEventLog"):
            splunk_hec_mode = "raw"
            print("Splunk HEC Endpoint:", splunk_url + splunk_hec_raw_endpoint)
        else: 
            print("Splunk HEC Endpoint:", splunk_url + splunk_hec_event_endpoint)

        data_file_length = get_data_file_length(file_path)
        current_line = 1
        event_json_storage = ""


        print("Writing", file_path, "to", splunk_index, "(", data_file_length, "lines )" )

        # HEC: "services/collector/event" endpoint
        if splunk_hec_mode == "event":
            # For each line in the current file
            while current_line <= data_file_length:
                
                current_event = get_line(file_path, current_line)

                event_json = {
                    "time": time.time(), 
                    "index": splunk_index, 
                    "host": splunk_host,
                    "source": source, 
                    "sourcetype": sourcetype,  
                    "event": current_event 
                    }        

                # Group events together for sending as a batch
                event_json_storage += json.dumps(event_json) + "\r\n"

                # Mod the currentLine to send as a batch per the eventsPerHecBatch factor
                if current_line % events_per_hec_batch == 0:
                    r = session.post(splunk_url + splunk_hec_event_endpoint, headers=splunk_auth_header, data=event_json_storage, verify=False)
                    event_json_storage = ""
                
                current_line += 1

            # Send remaining events in event_json_storage to HEC after the while loop concludes
            r = session.post(splunk_url + splunk_hec_event_endpoint, headers=splunk_auth_header, data=event_json_storage, verify=False)
            event_json_storage = ""

        # HEC: "services/collector/raw" endpoint
        if splunk_hec_mode == "raw":
            print("Skipping WinEventLog sourcetypes for now.")

            # For each line in the current file
            while current_line <= data_file_length:

                current_event = get_line(file_path, current_line)
                # Disabled until we can fix multiline
                # r = session.post(splunk_url + splunk_hec_raw_endpoint, headers=splunk_auth_header, data=current_event, verify=False)

                current_line += 1

        print("Done with", file_path, "to", splunk_index, "index (", data_file_length, "lines )" )
        print("-----")


# Close the persistent tcp session to Splunk HEC 
session.close()