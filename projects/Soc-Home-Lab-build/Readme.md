# SOC Home Lab with Wazuh, Suricata & VirusTotal

![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-blue) ![Suricata](https://img.shields.io/badge/IDS-Suricata-orange) ![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED) ![pfSense](https://img.shields.io/badge/Firewall-pfSense-black) ![MITRE](https://img.shields.io/badge/Mapped-MITRE%20ATT%26CK-red)

A self-built SOC lab simulating a Tier 1 analyst workflow: centralized logging, custom correlation rules, threat intelligence enrichment, and automated malware response using Wazuh, Suricata, and VirusTotal.

**Author:** Ashogbon Abdulazeez, Aspiring SOC Analyst | Blue Team | Detection Engineering | SIEM | Threat Hunting

📄 Full write-up: [SOC Home Lab Report.pdf](./SIEM%20LAB%20BUILD%20REPORT%20.pdf)
🖥️ Slides: [SOC Home Lab Presentation.pptx](./Siem%20Soc%20Home%20Lab%20Presentation.pdf)

---

## Lab Architecture

![Architecture Diagram](./Architecture%20Diagram.png)

- **Wazuh (Docker)** on Kali Linux
- **Ubuntu Endpoint** with Wazuh Agent and Suricata IDS
- **Windows 11 Endpoint** with Wazuh Agent and Sysmon
- **pfSense Firewall** forwarding syslog events
- **VirusTotal Integration** for threat intel enrichment
- **Active Response** for automated malicious file removal

---

## What's Inside

- Centralized log collection across Windows, Linux, network, and firewall
- Custom dashboards for authentication, process activity, and network traffic
- Custom correlation rules: SSH brute-force detection (T1110) and suspicious process execution (T1059)
- Full Detect → Analyze → Respond workflow using VirusTotal enrichment and Wazuh Active Response

For rule logic, dashboard screenshots, troubleshooting notes, and configuration details, see the full report above.

---

## Repository Contents

| File | Description |
|------|-------------|
| [SOC Home Lab Report.pdf](./SOC%20Home%20Lab%20Report.pdf) | Complete technical documentation |
| [SOC Home Lab Presentation.pptx](./SOC%20Home%20Lab%20Presentation.pptx) | Project presentation slides |
| [Architecture Diagram.png](./Architecture%20Diagram.png) | Lab architecture |
| [Screenshots/](./Screenshots) | Dashboards, alerts, and validation screenshots |

---

## Skills Demonstrated

SIEM Deployment · Log Analysis · Threat Hunting · Threat Intelligence Integration · Intrusion Detection · Endpoint Monitoring · Sysmon · Suricata · pfSense · Docker · Active Response Automation · Detection Engineering · Correlation Rule Development

