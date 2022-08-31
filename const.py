#
# const.py - Static and calculated variables.
#

import urllib3

from config import *

splunk_auth_header = {'Authorization': 'Splunk {}'.format(splunk_hec_token)}
splunk_hec_event_endpoint = "services/collector/event"
splunk_hec_raw_endpoint = "services/collector/raw"

data_home_path = "data/"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)