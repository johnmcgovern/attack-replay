#
# file.py - Lookup dictionaries
#

file_to_sourcetype_lookup = {
    "windows-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}

file_to_source_lookup = {
    "windows-powershell": "WinEventLog:Microsoft-Windows-Powershell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}
