#
# config.py - User modifiable variables.
#


splunk_url = 'https://example.splk.me:8088/services/collector/event'
splunk_hec_token = "9802541d-394f-4053-b973-306757e15ed3"
splunk_index = "test"   # Currently we always override the data files index specification (but this may change)
splunk_host = "attack-host" # Default host to use when we can't infer it from the data

debug = True

events_per_hec_batch = 200