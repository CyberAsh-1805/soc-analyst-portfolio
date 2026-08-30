# Detection Engineering & Alert Triage

Tier 1 SOC Analyst simulation project built on my existing [SOC home lab](../Soc-Home-Lab-build). This project focused on validating log sources, developing custom Wazuh detection rules mapped to MITRE ATT&CK, testing those rules through simulated attacks, tuning out alert noise, and applying a structured triage workflow to the resulting alerts.

## Resources

- 📄 [Full Report](./Detection%20Engineering%20%26%20Alert%20Triage%20Report.pdf)
- 🖥️ [Presentation](./Detection%20Engineering%20%26%20Alert%20Triage%20Presentation%20.pdf)
- 📋 [Triage Workflow](./Triage%20Workflow.pdf)
- 🗂️ [Lab Work Evidence](./Lab%20Works)


## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Lab Environment](#lab-environment)
- [Phase 1: Log Source Validation](#phase-1-log-source-validation)
- [Phase 2: Detection Rule Development](#phase-2-detection-rule-development)
- [Phase 3: Attack Simulation & Detection Results](#phase-3-attack-simulation--detection-results)
- [Detection Tuning](#detection-tuning)
- [Phase 4: Triage Workflow](#phase-4-triage-workflow)
- [Findings](#findings)
- [Challenges](#challenges)
- [Recommendations](#recommendations)
- [Appendix: Detection Rules](#appendix-detection-rules)

## Overview

I updated my existing SOC lab to better simulate the day-to-day work of a Tier 1 SOC Analyst, with a focus on detecting, investigating, and triaging security events. The result is a more practical SOC environment where events can be visualized, detected, investigated, and documented through a repeatable workflow.

## Objectives

- Validate that required log sources were actively sending telemetry to Wazuh
- Identify and fix gaps in Linux audit logging
- Build custom detection rules for selected MITRE ATT&CK techniques
- Test the rules using Atomic Red Team and manual simulation
- Tune rules that generated excessive noise
- Build a triage workflow for consistent alert review
- Apply the workflow to nine alerts and document final dispositions

## Lab Environment

- Wazuh (single-node, Docker on Kali Linux)
- Suricata on Ubuntu
- pfSense as firewall
- Sysmon on Windows 11
- Auditd on the Ubuntu endpoint

## Phase 1: Log Source Validation

Before building new detections, I manually generated activity and confirmed events were reaching Wazuh correctly.

**Gap found:** Auditd was not installed on the Ubuntu endpoint, and several planned detections depended on it. I installed Auditd, configured the required audit rules, and added the corresponding log collection config to the Wazuh agent.

**Confirmed operational:**
- Linux authentication and system events
- Linux journald authentication events (auditd)
- Firewall/network gateway logs (pfSense)
- Syslog, SSH activity, and brute-force correlation
- Windows Sysmon process creation telemetry


## Phase 2: Detection Rule Development

Five custom rules were built in `local_rules.xml`, mapped to MITRE ATT&CK techniques covering persistence, execution, and credential access.

| Rule ID | MITRE ATT&CK | Technique | Wazuh Level |
|---------|-------------|-----------|-------------|
| 100402 | T1053.003 | Scheduled Task/Job: Cron | 8 |
| 100405 | T1543.002 | Systemd Service | 9 |
| 100407 | T1059.004 | Command and Scripting Interpreter: Unix Shell | 10 |
| 100409 | T1003.008 | OS Credential Dumping | 12 |
| 100410 | T1552.001 | Unsecured Credentials | 10 |

- Cron and Systemd rules use Wazuh File Integrity Monitoring against relevant paths
- Auditd-based rules required custom Auditd rules first, so the correct telemetry existed before the Wazuh detection logic could act on it
- Every rule includes a MITRE ATT&CK mapping field

## Phase 3: Attack Simulation & Detection Results

Attacks were simulated using Atomic Red Team where a test existed, and manually within the isolated lab where it didn't.

All five rules triggered successfully:

- **100410** — Level 10 alert on `/etc/shadow` access
- **100409** — Level 12 alert on Auditd credential-dumping telemetry
- **100402** — detected cron file creation under `/etc/cron.d/`
- **100405** — detected Systemd service file creation
- **100407** — detected interactive Bash execution via Auditd

**Noise identified:** Rule 100409 alone generated over 53,000 Level 12+ alerts out of 56,247 total during the observed period, confirming the detection logic worked but the initial scope was far too broad for real SOC use.

## Detection Tuning

| Rule | Tuning Applied |
|------|-----------------|
| 100407 | Restricted to interactive terminal sessions (`pts/X`, `ttyX`) to cut background/automated noise |
| 100410 | Added exclusions for legitimate admin/system processes (`sudo`, `su`, `passwd`, `sshd`, `cron`, etc.) |
| 100409 | Added an exception for known debugging binaries generating unnecessary alerts |

This step demonstrated the gap between simply writing a detection rule and producing one that's actually usable in day-to-day SOC operations.

## Phase 4: Triage Workflow

A lightweight triage playbook was created defining how an analyst reviews an alert, assigns severity, investigates, and decides on disposition.

**Severity classification (by Wazuh level):**

| Severity | Level | Description |
|----------|-------|--------------|
| Low | 1–4 | Informational, limited security impact |
| Medium | 5–7 | Suspicious, requires investigation |
| High | 8–11 | Persistence, unauthorized execution, credential access risk |
| Critical | 12–15 | Credential theft, active attack, possible compromise |

**Workflow steps:** Review alert → Validate alert → Investigate activity → Determine outcome (True Positive / False Positive / Insufficient Evidence) → Assign severity → Determine disposition (Closed / Escalated) → Document reasoning.

**Applied to 9 alerts:**

| # | Alert | Rule ID | Level | Severity | Outcome | Disposition | Escalated |
|---|-------|---------|-------|----------|---------|--------------|-----------|
| 1 | Command Execution | 100407 | 10 | High | True Positive | Closed | No |
| 2 | Credential Dumping | 100409 | 12 | Critical | True Positive | Closed | No |
| 3 | Systemd Service Modification | 100405 | 9 | High | True Positive | Closed | No |
| 4 | Cron Job Creation | 100402 | 8 | High | True Positive | Closed | No |
| 5 | Shadow File Access | 100410 | 10 | High | True Positive | Closed | No |
| 6 | SSH Brute Force | 100300 | 12 | Critical | True Positive | Closed | No |
| 7 | Suspicious Execution | 100003 | 10 | High | True Positive | Closed | No |
| 8 | Interface Promiscuous Mode | 51004 | 5 | Medium | False Positive | Closed | No |
| 9 | AppArmor Access Denied | 52002 | 5 | Medium | False Positive | Closed | No |

2 of 9 alerts were false positives (legitimate network monitoring and normal security-policy enforcement); the remaining 7 were true positives generated by the custom detection rules, all tied to intentional lab simulation activity with no evidence of actual compromise.

## Findings

- Auditd was missing on the Linux endpoint, which initially blocked several detections from functioning until it was installed and configured
- All five custom rules fired correctly against their intended telemetry
- Detection logic being technically correct doesn't guarantee it's operationally useful. Rule 100409 alone showed how an overly broad rule creates alert fatigue even when it's "working"
- A structured triage workflow turns raw alert firing into documented, defensible decisions

## Challenges

- Missing Auditd installation had to be discovered and resolved before Auditd-based detections could be tested
- Wazuh rules alone weren't sufficient. The underlying Auditd configuration had to generate correctly-keyed telemetry first
- Atomic Red Team didn't cover every scenario, so some activity had to be simulated manually
- Alert noise from Auditd-based rules required dedicated tuning and filtering to be SOC-practical

## Recommendations

- Continue reviewing detection rules against normal baseline activity as the lab grows
- Maintain Auditd configuration alongside Wazuh rules so required telemetry stays available
- Periodically review high-volume rules for unnecessary or repetitive alerts
- Keep using MITRE ATT&CK mappings for new detections to maintain a clear link between attacker behavior and detection logic
- Keep applying the triage workflow to new alerts for consistency

## Appendix: Detection Rules

### Original Rules

```xml
<rule id="100402" level="8">
  <if_sid>550,554</if_sid>
  <field name="syscheck.path" type="pcre2">(?i)^/etc/(cron\.d|cron\.(daily|hourly|weekly|monthly)|crontab)|^/var/spool/cron/(crontabs/)?.*</field>
  <description>T1053.003 [Linux]: Cron job created or modified for persistence ($(syscheck.path))</description>
  <mitre><id>T1053.003</id></mitre>
</rule>

<rule id="100405" level="9">
  <if_sid>550,554</if_sid>
  <field name="syscheck.path" type="pcre2">(?i)^/(etc|lib|usr/lib)/systemd/system/.*\.service$</field>
  <description>T1543.002 [Linux]: Systemd service unit modified or created ($(syscheck.path))</description>
  <mitre><id>T1543.002</id></mitre>
</rule>

<rule id="100407" level="10">
  <if_group>audit</if_group>
  <field name="audit.key">script_interp</field>
  <field name="audit.exe" type="pcre2">(?i)/bin/bash|/usr/bin/python3|/usr/bin/dash</field>
  <description>T1059.004 [Linux]: Suspicious interpreter execution (bash/python/dash)</description>
  <mitre><id>T1059.004</id></mitre>
</rule>

<rule id="100409" level="12">
  <if_group>audit</if_group>
  <field name="audit.key">credential_dump</field>
  <description>T1003.008 [Linux]: Possible credential dumping via /proc memory access or shadow file inspection</description>
  <mitre><id>T1003.008</id></mitre>
</rule>

<rule id="100410" level="10">
  <if_group>audit</if_group>
  <field name="audit.key">credential_access</field>
  <description>T1552.001 [Linux]: Read access to sensitive credential file (/etc/shadow)</description>
  <mitre><id>T1552.001</id></mitre>
</rule>
```

### Tuned Rules

```xml
<rule id="100407" level="10">
  <if_group>audit</if_group>
  <field name="audit.key">script_interp</field>
  <field name="audit.exe" type="pcre2">(?i)^/usr/(bin|sbin)/(bash|python3?|dash|perl|php)$|^/bin/(bash|dash)</field>
  <field name="audit.tty" type="pcre2">^(pts/\d+|tty\d+)</field>
  <description>T1059.004 [Linux]: Suspicious script interpreter execution on terminal ($(audit.tty)) by user ($(audit.exe))</description>
  <mitre><id>T1059.004</id></mitre>
</rule>

<rule id="100409" level="12">
  <if_group>audit</if_group>
  <field name="audit.key">credential_dump</field>
  <field name="audit.exe" type="pcre2" negate="yes">(?i)/usr/bin/(strace|gdb)</field>
  <description>T1003.008 [Linux]: Possible credential dumping via /proc memory access or shadow file inspection</description>
  <mitre><id>T1003.008</id></mitre>
</rule>

<rule id="100410" level="10">
  <if_group>audit</if_group>
  <field name="audit.key">credential_access</field>
  <field name="audit.file.name" type="pcre2">^/etc/(shadow|gshadow|master.passwd)</field>
  <field name="audit.exe" type="pcre2" negate="yes">(?i)/usr/bin/(sudo|su|passwd|chage|gpasswd|login)|/usr/sbin/(sshd|cron|unix_chkpwd|unattended-upgrade|useradd|usermod)|/var/ossec/bin/wazuh-.*</field>
  <description>T1552.001 [Linux]: Unauthorized access attempt to sensitive credential file ($(audit.file.name)) by $(audit.exe)</description>
  <mitre><id>T1552.001</id></mitre>
</rule>
```

### Auditd Rules

```bash
# Rule 100410 / T1552.001 - Credential Access
-w /etc/shadow -p rwa -k credential_access
-w /etc/gshadow -p rwa -k credential_access

# Rule 100409 / T1003.008 - Process Memory Dumping
-a always,exit -F arch=b64 -S process_vm_readv,ptrace -k credential_dump
-a always,exit -F arch=b32 -S process_vm_readv,ptrace -k credential_dump

# Rule 100407 / T1059.004 - Interactive Script Interpreters
-a always,exit -F arch=b64 -S execve -k script_interp
-a always,exit -F arch=b32 -S execve -k script_interp
```


