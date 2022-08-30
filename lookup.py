#
# file.py - Lookup dictionaries
#

# File key to sourcetype mapping
file_to_sourcetype_lookup = {
    "carbon_black_events": "bit9:carbonblack:json",
    "downloadfile_windows-security": "WinEventLog:Security",
    "windows-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}

# File key to source mapping (optional)
file_to_source_lookup = {
    "windows-powershell": "WinEventLog:Microsoft-Windows-Powershell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}
