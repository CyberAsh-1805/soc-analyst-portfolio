# Threat Intelligence Analyst Simulation

## Overview
This project demonstrates a Tier-1 SOC Analyst threat intelligence investigation based on a SIEM alert involving suspicious outbound network traffic from a finance workstation. The investigation focuses on identifying and validating Indicators of Compromise (IOCs), mapping attacker behavior to the MITRE ATT&CK framework, and recommending containment and detection improvements.

## Scenario
A SIEM alert identified repeated outbound connections from **WS-FINANCE-04** to a known malicious IP address over HTTPS outside business hours. The activity occurred without an active user session and involved outbound data transfer, indicating possible command-and-control (C2) communication or data exfiltration.

## Objectives
- Investigate and classify the IOC.
- Validate findings using threat intelligence platforms.
- Map observed behavior to the MITRE ATT&CK framework.
- Assess the IOC using the Pyramid of Pain.
- Develop a SIEM correlation rule.
- Recommend containment and long-term detection improvements.

## Tools Used
- AlienVault OTX
- AbuseIPDB
- VirusTotal
- MITRE ATT&CK Framework

## Key Findings
- Confirmed the destination IP as a malicious Tor exit node.
- Classified the indicator as a Network IOC.
- Identified potential C2 communication and data exfiltration activity.
- Mapped observed techniques to relevant MITRE ATT&CK techniques.
- Proposed a SIEM correlation rule for automated detection.

## Recommendations
- Block the malicious IP address.
- Isolate the affected workstation for forensic analysis.
- Integrate threat intelligence feeds into the SIEM.
- Enhance detection rules for similar malicious activity.

## Skills Demonstrated
- Threat Intelligence Analysis
- IOC Investigation
- MITRE ATT&CK Mapping
- SIEM Detection Engineering
- Incident Analysis
- Threat Hunting Fundamentals


## Project Report

| Document | Description |
|----------|-------------|
| 📄 [Threat Intelligence Report](./Threat%20Intelligence%20Report.pdf) | Full investigation report, IOC analysis, MITRE ATT&CK mapping, SIEM correlation rule, and incident response recommendations. |
