#
# file.py - Lookup dictionaries
#

# File key to sourcetype mapping
file_to_sourcetype_lookup = {
    "7045_kerneldrivers": "WinEventLog:System",
    "Cobalt_spawnto": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "T1105-windows-security": "WinEventLog:Security",
    "T1197_windows-security": "WinEventLog:Security",
    "adsisearcher-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "all_functionrouter_http_streams": "stream:http",
    "all_icalc": "WinEventLog:Security",
    "attack-range-windows-domain-controller": "WinEventLog:Microsoft-Windows-Sysmon/Operational",
    "attack_data": "WinEventLog:Microsoft-Windows-Sysmon/Operational",
    "attack_data_network_resolution_dm": "stream:dns",
    "attack_data_stream:dns": "stream:dns",
    "audittrail": "audittrail",
    "aurora-edr": "aurora-edr",
    "authkey_linux-sysmon": "Syslog:Linux-Sysmon/Operational",
    "aws_cloudtrail_events": "aws:cloudtrail",
    "aws_ecr_container_upload": "aws:cloudtrail",
    "aws_ecr_scanning_findings_events": "aws:cloudtrail",
    "aws_iam_accessdenied_discovery_events": "aws:cloudtrail",
    "aws_iam_assume_role_policy_brute_force": "aws:cloudtrail",
    "aws_iam_delete_policy": "aws:cloudtrail",
    "aws_iam_excessive_list_command_usage": "aws:cloudtrail",
    "aws_iam_failure_group_deletion": "aws:cloudtrail",
    "aws_iam_successful_group_deletion": "aws:cloudtrail",
    "aws_security_scanner": "aws:cloudtrail",
    "azure-activity": "mscs:azure:audit",
    "azure-audit": "mscs:azure:eventhub",
    "bits-windows-security": "WinEventLog:Security",
    "bro_conn": "bro:conn:json",
    "carbon_black_events": "bit9:carbonblack:json",
    "certblob_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "circle_ci_disable_security_job": "circleci",
    "circle_ci_disable_security_step": "circleci",
    "cisco_ios": "cisco:ios",
    "clear_evt": "WinEventLog:Security",
    "confluence": "pan:threat",
    "container_implant_1": "aws:cloudtrail",
    "container_implant_2": "aws:cloudtrail",
    "copy-powershell": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "credaccess-powershell": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "crowdstrike_falcon": "crowdstrike:events:sensor",
    "curl-linux-sysmon": "sysmon_linux",
    "deny": "WinEventLog:Security",
    "disable_evt": "WinEventLog:Security",
    "domaingroup": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "domainpolicy": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "domaintrust": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "dotnet_lolbin-windows-security": "WinEventLog:Security",
    "downloadfile_windows-security": "WinEventLog:Security",
    "downloadfile_windows-security": "WinEventLog:Security",
    "empire": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "encode-windows-security": "WinEventLog:Security",
    "enumeration": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "exchange_events": "MSWindows:IIS",
    "f5": "pan:threat",
    "firewall-powershell": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "frombase64string": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "gdrive_share_external": "gsuite:drive:json",
    "gdrive_susp_attach": "gsuite:drive:json",
    "get-aduser-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "getdc": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "getdomainuser": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "getdomainuser-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "getlocalgroup": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "github_actions_disable_security_workflow": "aws:firehose:json",
    "github_pull_request": "aws:firehose:json",
    "github_push_develop": "aws:firehose:json",
    "github_push_master": "aws:firehose:json",
    "github_security_advisor_alert": "aws:firehose:json",
    "gsuite_external_domain": "gsuite:gmail:bigquery",
    "gsuite_gmail_file_ext": "gsuite:gmail:bigquery",
    "gsuite_susp_subj_attach": "gsuite:gmail:bigquery",
    "gsuite_susp_url": "gsuite:gmail:bigquery",
    "hidden_windows-security": "WinEventLog:Security",
    "high_number_of_login_failures_from_a_single_source": "o365:management:activity",
    "http_request_body_streams": "stream:http",
    "iso_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "java": "stream:http",
    "java_spawn_shell_nix": "sysmon_linux",
    "java_write_jsp-linux-sysmon": "sysmon_linux",
    "krbrelayup": "WinEventLog:Security",
    "kubernetes_kube_hunter": "kube:objects:events",
    "kubernetes_nginx_lfi_attack": "kube:container:controller",
    "kubernetes_nginx_rfi_attack": "kube:container:controller",
    "linux-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "linux-sysmon_curlwget": "sysmon_linux",
    "linux_secure": "linux_secure",
    "linuxrisk": "stash",
    "log4j_network_logs": "stream:ip",
    "log4j_proxy_logs": "nginx:plus:kv",
    "log4shell-nginx": "nginx:plus:kv",
    "logAllDSInternalsModules": "WinEventLog:Security",
    "logAllMimikatzModules": "WinEventLog:Security",
    "logAllPowerSploitModulesWithOldNames": "WinEventLog:Security",
    "logExcessiveTaskHost": "WinEventLog:Security",
    "logExcessiveWindowsTemp": "WinEventLog:Security",
    "logFgdump": "WinEventLog:Security",
    "logLazagneCredDump": "WinEventLog:Security",
    "logLiveKDFullKernelDump": "WinEventLog:Security",
    "logPowerShellModule": "WinEventLog:Security",
    "lolbinrisk": "stash",
    "mimikatz-windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "mofcomp": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "msbuild-windows-security": "WinEventLog:Security",
    "msdt": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "msiexec_moved": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "msra-windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "nettcpconnection": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "o365_add_app_role_assignment_grant_user": "o365:management:activity",
    "o365_add_service_principal": "o365:management:activity",
    "o365_brute_force_login": "o365:management:activity",
    "o365_bypass_mfa_via_trusted_ip": "o365:management:activity",
    "o365_disable_mfa": "o365:management:activity",
    "o365_email_forwarding_rule": "o365:management:activity",
    "o365_export_pst_file": "o365:management:activity",
    "o365_new_federated_domain": "o365:management:activity",
    "o365_new_federated_domain_added": "o365:management:activity",
    "o365_new_federation": "o365:management:activity",
    "o365_sso_logon_errors": "o365:management:activity",
    "ordinal_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "osquery": "osquery:results",
    "pantraffic": "pan:traffic",
    "powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "prohibited_apps_spawning_cmd": "WinEventLog:Security",
    "protocolhandlers": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "ptt_pth_kerb_ntlm_anon_DC_dataset": "WinEventLog:Security",
    "ptt_pth_kerb_ntlm_anon_dest_dataset": "WinEventLog:Security",
    "raw-msra-windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "reconusingwmi": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "reflection": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "safemode_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "sbl_xml": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "sc_kernel": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "sd_delete_windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "security": "WinEventLog:Security",
    "shadow-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "splunk_web_access": "splunk_web_access",
    "splunk_zip_bomb_vulnerability": "splunkd",
    "splunkd": "splunkd",
    "spring4shell_nginx": "nginx:plus:kv",
    "ssl_splunk": "stream:tcp",
    "stream_dns": "stream:dns",
    "stream_events_zeek": "bro:dns:json",
    "stream_http_events": "stream:http",
    "streamreader": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "suricata_events": "suricata",
    "suspicious_rights_delegation": "o365:management:activity",
    "sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "sysmon_linux": "Syslog:Linux-Sysmon/Operational",
    "sysmon_linux_cron_append": "Syslog:Linux-Sysmon/Operational",
    "sysmon_print": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "sysmon_sys_filemod": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "t1547001-runonce": "WinEventLog:Security",
    "vmware_scanning_pan_threat": "pan:threat",
    "widows-security": "WinEventLog:Security",
    "win32process": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-directory_service": "WinEventLog",
    "windows-powershell": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-powershell-xml": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operationalml",
    "windows-powershell-xml2": "XmlWinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-powershell_kerberos": "WinEventLog:Microsoft-Windows-PowerShell/Operational",
    "windows-printservice_admin": "WinEventLog:Microsoft-Windows-PrintService/Admin",
    "windows-printservice_operational": "WinEventLog:Microsoft-Windows-PrintService/Operational",
    "windows-sec-events": "WinEventLog:Security",
    "windows-security": "WinEventLog:Security",
    "windows-security-2": "WinEventLog:Security",
    "windows-security-xml": "XmlWinEventLog",
    "windows-security_bcdedit_wbadmin": "WinEventLog:Security",
    "windows-symon_wsh": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon-odbc-regsvr": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon-odbc-rsp": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon-registry": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon2": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_cabinf": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_control": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_creddump": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", 
    "windows-sysmon_curl": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_curl_upload": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_dllhost": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_iceded": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_installutil_path": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_macros": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_mshtml": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_proxylogon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_searchprotocolhost": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_setspn": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-sysmon_umservices": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
    "windows-system": "WinEventLog:System",
    "windows-taskschedule": "WinEventLog:Microsoft-Windows-TaskScheduler/Operational",
    "windows-taskschedule_xml": "XmlWinEventLog:Microsoft-Windows-TaskScheduler/Operational",
    "zeek-dce_rpc": "bro:dce_rpc:json",
}

# File key to source mapping (optional)
file_to_source_lookup = {
    "windows-powershell": "WinEventLog:Microsoft-Windows-Powershell/Operational",
    "windows-security": "WinEventLog:Security",
    "windows-sysmon": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
}
