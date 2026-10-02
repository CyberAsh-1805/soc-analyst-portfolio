# SOC Alert Triage

![Alerts](https://img.shields.io/badge/Alerts%20Triaged-10-blue)
![Platform](https://img.shields.io/badge/Platform-LetsDefend-green)
![Framework](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-red)
![Role](https://img.shields.io/badge/Role-SOC%20Tier%201-orange)

Ten alert investigations completed on the LetsDefend platform in a Tier 1 SOC analyst role. Each alert was triaged, classified, contained where needed, and documented in a structured report.

**Analyst:** Ashogbon Ayomikun

**Platform:** LetsDefend (SIEM, Log Management, Endpoint Security, Email Security, Threat Intel)

**Quick Links:** [Full Report (PDF)](./ALERT%20TRIAGE%20REPORT.pdf) | [Screenshots](./Screenshots)

## Contents

- [`ALERT_TRIAGE_REPORT.pdf`](./ALERT%20TRIAGE%20REPORT.pdf): the full reports for all 10 alerts
- [`screenshots/`](./Screenshots): appendix evidence (SIEM case closure, endpoint containment, VirusTotal, AbuseIPDB, MXToolbox)

## Report Structure

Every report follows the same layout, aligned with NIST SP 800-61 and using SANS-style intake fields:

1. Verdict (classification, severity, Tier 2 escalation)
2. Alert details
3. Evidence
4. Investigation
5. Analysis
6. Indicators of compromise
7. MITRE ATT&CK mapping
8. Actions taken
9. Recommendations
10. Appendix (screenshots)

## Alerts Investigated

| Alert | Name | Type | Severity | Verdict |
|-------|------|------|----------|---------|
| SOC274 | PAN-OS Command Injection (CVE-2024-3400) | Web Attack | Critical | True Positive |
| SOC239 | Splunk Enterprise RCE via User XSLT (CVE-2023-46214) | Unauthorized Access | High | True Positive |
| SOC127 | SQL Injection Detected | Web Attack | High | True Positive |
| SOC250 | APT35 HyperScrape Data Exfiltration Tool | Data Leakage | Medium | True Positive |
| SOC176 | RDP Brute Force Detected | Brute Force | Medium | True Positive |
| SOC282 | Phishing, Deceptive Mail Detected | Exchange | Medium | True Positive |
| SOC251 | Quishing (QR Code Phishing) | Exchange | Medium | True Positive |
| SOC335 | CVE-2024-49138 Exploitation | Privilege Escalation | Medium | True Positive |
| SOC326 | Impersonating Domain MX Record Change | ThreatIntel | Medium | True Positive |
| SOC325 | Unauthorized Cloud Region Access Attempt | Web Attack | Low | True Positive (blocked, closed) |

Full details, evidence, IOCs, and recommendations for each alert are in the [PDF report](./ALERT%20TRIAGE%20REPORT.pdf), with supporting evidence in the [screenshots folder](./Screenshots).

## Coverage

- **Initial access:** exploitation of public-facing applications, phishing, quishing, RDP brute force
- **Execution and privilege escalation:** command injection, reverse shell via malicious XSLT, local privilege escalation exploit
- **Collection and exfiltration:** email theft over a C2 channel
- **Brand abuse and recon:** lookalike domain with MX record change, restricted-region access attempts

## Skills Demonstrated

- Alert triage and true/false positive classification
- Log analysis in a SIEM (firewall, OS, proxy, and exchange logs)
- Threat intelligence enrichment with VirusTotal, AbuseIPDB, and MXToolbox
- Email header and sender authentication checks (SPF, DKIM, DMARC)
- Malware file hash and C2 analysis
- Host containment and Tier 2 escalation decisions
- MITRE ATT&CK technique mapping
- Writing actionable recommendations and incident documentation

## Tools Used

LetsDefend SIEM, Log Management, Endpoint Security, Email Security, Threat Intel, VirusTotal, AbuseIPDB, MXToolbox, MITRE ATT&CK

## Notes

All alerts are from LetsDefend practice platform. IPs, hosts, and users shown belong to Letsdefend.

## About Me

Aspiring SOC Analyst with hands on experience and known certificates

- Portfolio: [github.com/CyberAsh-1805/soc-analyst-portfolio](https://github.com/CyberAsh-1805/soc-analyst-portfolio)
- LinkedIn: [linkedin.com/in/ayomikun-ashogbon-0330a7391](https://linkedin.com/in/ayomikun-ashogbon-0330a7391)
