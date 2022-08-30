# attack-replay

This project takes data samples for the Splunk Threat Research team's attack_data project and replays them into Splunk via the HEC input.

Place data in the project file structure as is shown below:

- ./data/T1059.001/atomic_red_team/windows-sysmon.log

Usage: 

- python main.py T1059.001 atomic_red_team

The TTP ID should be specified first followed by the data source name. Both should correspond exactly to the relevant locations in the imported attack_data.

Data samples from the attack_data project are drawn from attack_data/datasets/attack_techniques/.


Notes:

- To add a sourcetype or source mapping, update the dictionaries in lookup.py.
- Host inference feature coming (hopefully) someday. Right now host is static.
- Copy config-sample.py to config.py and modify as needed.