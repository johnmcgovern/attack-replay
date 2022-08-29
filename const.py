#
# const.py - Static and calculated variables.
#

import urllib3

from config import *

splunk_auth_header = {'Authorization': 'Splunk {}'.format(splunk_hec_token)}

data_file_location = "data/"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)