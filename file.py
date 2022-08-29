#
# file.py - File and filesystem type operations.
#

import linecache

def get_data_file_length(data_file_path):
    dataFile = open(data_file_path, "r")
    for dataFileLength, line in enumerate(dataFile):
        pass
    dataFileLength += 1
    dataFile.close()
    print("Data File Length:", dataFileLength)
    return dataFileLength


def get_line(data_file_path, line_number):
    line_data = linecache.getline(data_file_path, line_number)
    return line_data