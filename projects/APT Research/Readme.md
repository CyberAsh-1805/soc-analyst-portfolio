# APT29 Threat Actor Profile

A research write-up on APT29, mapped to the MITRE ATT&CK framework, documenting tactics, techniques, and procedures (TTPs) observed across the group's known operations.

## Overview

Advanced Persistent Threats (APTs) are sophisticated, long-term cyberattack campaigns carried out by well-resourced adversaries, typically nation-state actors or organized threat groups, with the goal of gaining and maintaining unauthorized access to targeted networks over an extended period. They are defined by advanced capabilities, persistence, stealth, and deliberate targeting of specific organizations.

Unlike opportunistic cybercrime, which usually seeks quick financial gain, APTs are commonly tied to objectives such as cyber espionage, intelligence gathering, data theft, or long-term disruption. Attackers conduct reconnaissance, establish persistence, escalate privileges, move laterally, and exfiltrate sensitive information while trying to remain undetected.

Understanding APT behavior matters for security analysts because effective detection requires more than identifying known malware; it requires understanding the techniques and behaviors used across the full attack lifecycle. The MITRE ATT&CK framework supports this by categorizing adversarial behavior into tactics, techniques, and sub-techniques, helping defenders recognize attack patterns and improve detection and response.

## Group Profile: APT29

| Field | Details |
|---|---|
| **Also known as** | Cozy Bear, The Dukes, CozyDuke, NOBELIUM, Midnight Blizzard, UNC2452, Dark Halo, SolarStorm |
| **Active since** | At least 2008 |
| **Attribution** | Russia's Foreign Intelligence Service (SVR) |
| **Motivation** | State-sponsored cyber-espionage |

### Country Affiliation

APT29 is affiliated with Russia and is attributed to the Foreign Intelligence Service (SVR). The group is primarily associated with state-sponsored cyber-espionage activities.

### Targeted Organizations / Systems

- Government agencies
- NATO member networks across Europe
- Research institutes and think tanks
- Technology organizations and managed service providers
- Cloud and Microsoft 365 environments, email accounts, identity systems, and network infrastructure

### Operational Location

APT29 is based in Russia, with operations conducted remotely against organizations across Europe, North America, and other regions.

### Activities and Targeting

APT29 primarily conducts cyber-espionage and intelligence-gathering operations. Its activities include gaining unauthorized access to targeted environments, compromising identities and cloud accounts, maintaining persistence, collecting sensitive information, and exfiltrating data.

Notable operations include the 2015 Democratic National Committee compromise and the 2020 SolarWinds supply-chain attack, which the US and UK governments attributed to the SVR in April 2021. The group has also compromised technology and managed service providers to reach their downstream customers, and has targeted Microsoft 365 and Azure environments directly.

### Common TTPs

Spearphishing, password spraying, valid accounts, PowerShell, WMI, scheduled tasks, credential theft, exploitation of public-facing applications, remote services, supply-chain compromise, cloud identity abuse, proxying, and data exfiltration.

## MITRE ATT&CK Mapping

### Initial Access

| Technique | ID | Use |
|---|---|---|
| Phishing: Spearphishing Attachment | T1566.001 | Used spearphishing emails with attachments to deliver exploits to initial victims |
| Phishing: Spearphishing Link | T1566.002 | Used spearphishing links directing victims to malicious ZIP files and other payloads |
| Exploit Public-Facing Application | T1190 | Exploited vulnerabilities in Citrix, Pulse Secure, FortiGate, Zimbra, and Microsoft Exchange |
| Supply Chain Compromise | T1195.002 | Gained initial access through a trojanized update of SolarWinds Orion software |

### Credential Access

| Technique | ID | Use |
|---|---|---|
| Brute Force: Password Guessing | T1110.001 | Conducted successful password-guessing attacks against targeted mailboxes |
| Brute Force: Password Spraying | T1110.003 | Conducted password-spray attacks against accounts |
| OS Credential Dumping | T1003 | Used credential-dumping techniques to obtain credentials from compromised systems |
| Steal Web Session Cookie | T1539 | Stole Chrome browser cookies to access victim accounts and bypass authentication |

### Execution

| Technique | ID | Use |
|---|---|---|
| PowerShell | T1059.001 | Used encoded PowerShell to install malware, create tasks, identify configurations, and exfiltrate data |
| Windows Command Shell | T1059.003 | Used cmd.exe to execute commands on remote machines |
| Windows Management Instrumentation | T1047 | Used WMI to execute backdoors, steal credentials, and move laterally |

### Persistence

| Technique | ID | Use |
|---|---|---|
| Registry Run Keys / Startup Folder | T1547.001 | Added Registry Run Keys to establish persistence and execute malware at startup |
| Scheduled Task/Job: Scheduled Task | T1053.005 | Created or modified scheduled tasks to maintain persistence |
| Web Shell | T1505.003 | Installed web shells on exploited Microsoft Exchange servers |

### Privilege Escalation

| Technique | ID | Use |
|---|---|---|
| Bypass User Account Control | T1548.002 | Bypassed User Account Control to obtain elevated privileges |

### Discovery

| Technique | ID | Use |
|---|---|---|
| Account Discovery: Domain Account | T1087.002 | Used PowerShell commands such as Get-ADUser and Get-ADGroupMember to discover domain accounts |
| File and Directory Discovery | T1083 | Obtained information about files and directories on compromised systems |

### Lateral Movement

| Technique | ID | Use |
|---|---|---|
| Remote Services: RDP | T1021.001 | Used RDP sessions to move from public-facing systems to internal servers |
| Remote Services: SMB/Windows Admin Shares | T1021.002 | Used administrative accounts to connect to targeted systems over SMB |

### Defense Evasion

| Technique | ID | Use |
|---|---|---|
| Obfuscated Files or Information | T1027 | Used packing, binary padding, steganography, and other methods to hide malicious content |
| Indicator Removal: File Deletion | T1070.004 | Removed tools and custom backdoors after achieving remote access |

### Command and Control

| Technique | ID | Use |
|---|---|---|
| Application Layer Protocol: Web Protocols | T1071.001 | Used HTTP for command-and-control communication and data exfiltration |
| Proxy | T1090 | Used compromised residential endpoints, Tor, and other proxy mechanisms to hide C2 traffic |

### Collection

| Technique | ID | Use |
|---|---|---|
| Remote Email Collection | T1114.002 | Collected emails from targeted mailboxes using Exchange Web Services and mailbox export requests |
| Data from Local System | T1005 | Stole data and extracted files from compromised hosts and networks |

### Exfiltration

| Technique | ID | Use |
|---|---|---|
| Archive Collected Data | T1560.001 | Used 7-Zip to compress stolen emails into password-protected archives before exfiltration |
| Exfiltration Over Alternative Protocol | T1048.002 | Exfiltrated staged data through encrypted HTTPS requests to attacker-controlled infrastructure |

## Analysis Summary

APT29's techniques show a strong emphasis on stealth, identity compromise, abuse of legitimate administrative tools, cloud environments, and long-term persistence. The group's coverage across nearly every MITRE ATT&CK tactic, from initial access through execution, persistence, discovery, lateral movement, collection, and exfiltration, illustrates a mature, patient operating style built around remaining undetected for as long as possible.

## References

- MITRE ATT&CK: [APT29 (G0016)](https://attack.mitre.org/groups/G0016/)

