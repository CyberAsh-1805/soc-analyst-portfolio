# APT29 Threat Actor Profile

Research write-up on APT29, mapped to the MITRE ATT&CK framework. Full report: [APT29_Threat_Profile.pdf](./APT29…..pdf)

## Summary

APT29, also known as Cozy Bear, Midnight Blizzard, NOBELIUM, and The Dukes, is a Russian state-sponsored threat group attributed to the SVR, active since at least 2008. The group focuses on long-term cyber-espionage: compromising identities and cloud environments, maintaining stealthy persistence, and exfiltrating sensitive data from government, NATO-aligned, and technology-sector targets.

**Notable operations:** the 2015 DNC compromise and the 2020 SolarWinds supply-chain attack.

## Quick Facts

| Field | Details |
|---|---|
| **Aliases** | Cozy Bear, The Dukes, CozyDuke, NOBELIUM, Midnight Blizzard, UNC2452, Dark Halo, SolarStorm |
| **Active since** | 2008 |
| **Attribution** | Russia (SVR) |
| **Motivation** | State-sponsored espionage |
| **Primary targets** | Government, NATO networks, think tanks, tech firms, MSPs, cloud/M365 environments |

## ATT&CK Coverage

APT29's TTPs span nearly every stage of the attack lifecycle:

| Tactic | Example Technique |
|---|---|
| Initial Access | Spearphishing, exploit public-facing apps, supply chain compromise (SolarWinds) |
| Credential Access | Password spraying, credential dumping, session cookie theft |
| Execution | PowerShell, WMI, Windows Command Shell |
| Persistence | Registry run keys, scheduled tasks, web shells |
| Privilege Escalation | UAC bypass |
| Discovery | Domain account & file/directory discovery |
| Lateral Movement | RDP, SMB/admin shares |
| Defense Evasion | Obfuscation, file deletion |
| Command & Control | HTTP-based C2, proxying via Tor/residential proxies |
| Collection | Remote email collection, local data theft |
| Exfiltration | 7-Zip archiving, HTTPS exfiltration |

Full technique-to-ID mapping and use-case detail is in the [complete report](./APT29_Threat_Profile.pdf).

## References

- MITRE ATT&CK: [APT29 (G0016)](https://attack.mitre.org/groups/G0016/)

