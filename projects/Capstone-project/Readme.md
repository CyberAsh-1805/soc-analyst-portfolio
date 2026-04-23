
# 🏢 NovaTech Security Assessment — Capstone Project

**Author:** Ashogbon Ayomikun Abdulazeez
**Assessment Date:** April 1, 2026
**Type:** Cybersecurity Assessment Report

📄 [Download Full Report (PDF)](./Ashogbon_Ayomikun_Abdulazeez_Capstone_project.pdf)

---

## Executive Summary

Conducted a comprehensive cybersecurity assessment on
the NovaTech internal network (192.168.10.0/24),
covering network infrastructure analysis, SOC alert
investigation, vulnerability assessment, risk
evaluation, and security recommendations.

---

## Network Topology

| Device | Role | IP Address |
|---|---|---|
| Router | Gateway | 192.168.10.1 |
| Employee Workstation | End User | 192.168.10.15 |
| Web Server | Hosts company website | 192.168.10.20 |
| File Server | Stores company documents | 192.168.10.25 |
| Database Server | Stores application data | 192.168.10.30 |

---

## Key Findings

### SOC Alert Investigation
- **Attack Type:** Brute-Force Attack
- **Target:** Web Server (192.168.10.20)
- **IOCs:** Multiple failed login attempts from
  external IP, unusual authentication patterns
- **Response:** Isolate host, block attacker IP,
  disable affected account, restore from backup

### Vulnerabilities Identified
- Apache 2.4.29 running on Web Server — outdated
  with known CVEs
- Default credentials (root/root) on Database Server
- Anonymous FTP login enabled on File Server
- No MFA enforced on any system
- No network segmentation — single breach risks
  full network compromise
- MySQL Port 3306 exposed externally

---

## Risk Assessment

| Asset | Threat | Risk Level |
|---|---|---|
| Web Server | Brute-force / outdated Apache exploit | HIGH |
| Database Server | Data breach / theft | HIGH |
| File Server | Unauthorized access via anonymous FTP | HIGH |
| Network Infrastructure | Lateral movement | MEDIUM |

---

## Recommendations

1. Update Apache to latest stable version
2. Enforce strong password policy — remove root/root
3. Enable MFA on all administrative interfaces
4. Disable anonymous FTP — migrate to SFTP
5. Restrict MySQL Port 3306 to internal access only
6. Implement network segmentation using VLANs
7. Deploy EDR on all workstations
8. Tune SIEM for brute-force and lateral movement
   alerts
