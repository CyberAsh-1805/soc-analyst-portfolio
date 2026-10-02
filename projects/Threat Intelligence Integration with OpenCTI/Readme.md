# Threat Intelligence Integration with OpenCTI

![OpenCTI](https://img.shields.io/badge/OpenCTI-Threat%20Intel-0f1e3d?style=for-the-badge)
![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-005571?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-C8102E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

Extending a Wazuh-based SOC home lab with OpenCTI so that security alerts are automatically enriched with threat intelligence.

**Author:** Ashogbon Ayomikun

**Date:** September 2026

**Part of:** [SOC home lab](../Soc-Home-Lab-build).

## Documentation

| Resource | Link |
|---|---|
| Full report (PDF) | [Threat Intelligence Integration with OpenCTI Report](Threat%20Intelligence%20Integration%20with%20OpenCTI%20Report.pdf) |
| Presentation slides | [View slides](Threat%20Intelligence%20Integration%20with%20OpenCTI.pptx) |
| Screenshots | [/Screenshots](Screenshots) |

## Overview

This project adds OpenCTI as a threat intelligence layer on top of an existing SOC homelab. When a Wazuh alert contains an Indicator of Compromise (IP, URL or file hash), it is checked against OpenCTI and an enriched alert is raised if there is a match, giving the analyst immediate context during triage.

**Workflow:**

```
Security Event > Wazuh > OpenCTI IOC Lookup > Threat Intel Match > Enriched Wazuh Alert > Analyst Investigation
```

## Lab Environment

![Lab architecture and data flow](screenshots/architecture.png)
*Endpoint telemetry flows to Wazuh, and Wazuh queries OpenCTI over GraphQL for IOC enrichment.*

| Component | Role |
|---|---|
| Wazuh (Docker on Kali Linux) | SIEM: Manager, Indexer, Dashboard |
| Ubuntu endpoint | Syslog, auth logs, Suricata, Wazuh Agent |
| Windows endpoint | Sysmon, Wazuh Agent |
| pfSense | Firewall, logs forwarded to Wazuh over UDP 514 |
| OpenCTI (Docker Compose) | Threat intelligence platform |

The existing environment already included seven custom Wazuh detection rules (brute force, suspicious process execution, cron persistence, OS credential dumping, unsecured credential access, Unix script interpreters, system service activity).

## Threat Intelligence Sources

| Source | Status |
|---|---|
| URLhaus | Integrated |
| MalwareBazaar | Integrated (after fixing the connector config) |
| ThreatFox | Integrated (replaced AlienVault OTX) |
| MITRE ATT&CK | Integrated (connector reset required) |

## What Was Built

1. **Deployed OpenCTI** with Docker Compose (Elasticsearch, Redis, RabbitMQ, MinIO and connectors), then explored the data model and validated it by manually creating a Threat Actor, an Indicator and a relationship.
2. **Integrated threat feeds** and reviewed example indicators from each source (Cobalt Strike C2 IP from ThreatFox, a Remus loader SHA-256 from MalwareBazaar, a Mozi/Mirai distribution URL from URLhaus).
3. **Built the Wazuh to OpenCTI enrichment pipeline** using a custom GraphQL integration and two custom rules:
   - `100101` (level 12): IOC matched and flagged malicious
   - `100102` (level 7): IOC known to OpenCTI but not flagged malicious
4. **Applied threat intel to a real detection** by enriching the existing SSH brute-force rule.

## Validation

| Test | Input | Result |
|---|---|---|
| Negative IOC | `185.220.101.5` | 0 matches |
| Positive IOC | `37.187.150.121` | Match, score 80, 7 indicators |
| Controlled alert | Test alert with `175.41.16.98` | Enriched successfully |
| Live brute force | 5 failed SSH logins from `175.41.16.98` | Brute-force alert plus OpenCTI match alert (rule 100101) on the Wazuh dashboard |

The live test confirmed the pipeline runs event-driven, not only when the script is run manually.

## Challenges and Fixes

| Challenge | Resolution |
|---|---|
| MITRE ATT&CK data not appearing, then technique IDs missing | Reset the connector (twice) |
| MalwareBazaar delivered no data | Changed `OPENCTI_URL` from `localhost` to the `opencti` service name, since `localhost` pointed at the connector container itself |
| AlienVault OTX failed (time-format error, then 503) | Removed it and deployed ThreatFox instead |
| Integration worked manually but not in the background | Set `integrator.debug=2` in `internal_options.conf` and restarted the Wazuh Manager, which exposed the background process in the logs |

## Key Takeaways

- A connector showing as active does not guarantee data is flowing, so connector health should be checked regularly.
- Keep alternative intel sources ready in case a feed fails.
- Keep tokens and API keys in environment variables and out of shared configs and documentation.
- Turning up integration debug logging is essential when a manual test passes but the live pipeline does not.

## Skills Demonstrated

Threat intelligence platform deployment (OpenCTI), Wazuh integration and custom rule writing, GraphQL-based enrichment, Docker Compose, IOC analysis, MITRE ATT&CK mapping, detection engineering, troubleshooting and documentation.

## Security Note

All tokens, API keys and credentials have been redacted from the report and screenshots.

## Contact

[LinkedIn](https://linkedin.com/in/ayomikun-ashogbon-0330a7391)

