#
# file.py - Lookup dictionaries
#

# File key to sourcetype mapping
file_to_sourcetype_lookup = {
    "carbon_black_events": "bit9:carbonblack:json",
    "downloadfile_windows-security": "WinEventLog:Security",
    "windows-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-system": "WinEventLog:System",
    "sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "osquery": "osquery:results",
    "azure-audit": "mscs:azure:eventhub",
    "splunkd": "splunkd",
    "certblob_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "logAllPowerSploitModulesWithOldNames": "WinEventLog:Security",
    "aws_iam_accessdenied_discovery_events": "aws:cloudtrail",
    "aws_iam_assume_role_policy_brute_force": "aws:cloudtrail",
    "aws_iam_excessive_list_command_usage": "aws:cloudtrail",
    "sysmon_linux.log": "Syslog:Linux-Sysmon/Operational",
    "windows-sysmon2": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "stream_dns": "stream:dns",
    "stream_events_zeek": "bro:dns:json",
    "suricata_events": "suricata",
    "gdrive_share_external": "gsuite:drive:json",
    "attack_data_network_resolution_dm": "stream:dns",
    "attack_data_stream:dns": "stream:dns",
    "gdrive_susp_attach": "gsuite:drive:json",
    "gsuite_external_domain": "gsuite:gmail:bigquery",
    "gsuite_gmail_file_ext": "gsuite:gmail:bigquery",
    "gsuite_susp_subj_attach": "gsuite:gmail:bigquery",
    "gsuite_susp_url": "gsuite:gmail:bigquery",
    "msdt": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_cabinf": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_control": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_iceded": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_macros": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_mshtml": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-symon_wsh": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "aws_cloudtrail_events": "aws:cloudtrail",
    "o365_bypass_mfa_via_trusted_ip": "o365:management:activity",
    "powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational"
    
}

# File key to source mapping (optional)
file_to_source_lookup = {
    "windows-powershell": "WinEventLog:Microsoft-Windows-Powershell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}
