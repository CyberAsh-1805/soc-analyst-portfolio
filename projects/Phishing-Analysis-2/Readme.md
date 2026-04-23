# 🎣 Phishing Email Analysis 2 — Microsoft Impersonation

**Date:** January 20, 2026
**Tools Used:** VirusTotal, HaveIBeenPwned, 
CheckShortURL, URL Unshortener
**Classification:** Phishing Attack ✅ Confirmed

📄 [View Full Report (PDF)](./Ayomikun_Abdulazeez_Ashogbon.pdf)

---

## Overview

Investigated a suspicious email impersonating the
Microsoft IT team. The email contained an embedded
shortened URL and used urgency tactics to pressure
the recipient into clicking a verification link.

---

## IOCs Identified

| IOC | Type | Verdict |
|---|---|---|
| https://tinyurl.com/ypu5kfts | Shortened URL | 3/97 — Phishing |
| https://x-egamb.com/ | Destination URL | 5/97 — Malicious |

---

## Investigation Findings

### URL Analysis
- Shortened link (tinyurl.com/ypu5kfts) flagged by
  3 vendors including Fortinet and G-Data as Phishing
- Unshortened destination (x-egamb.com) flagged by
  5 vendors — CRDF (Malicious), Kaspersky (Phishing),
  Sophos (Malware), Fortinet (Phishing), SOCRadar
  (Phishing)
- URL contains password-input, trackers, and
  external-resources tags — credential harvesting site

### URL Unshortening
- Short URL: https://tinyurl.com/ypu5kfts
- Long URL: https://x-egamb.com/
- HTTP Code: 301 (redirect)

### Email Breach Check
- Sender email (info@libreriacies.es): No breaches found
- Receiver email (sonyundefinedralph@gmail.com):
  No breaches found

### Sender Domain Analysis
- Domain: libreriacies.es
- IP: 217.18.163.139 — Granada, Spain
- VirusTotal: 0/93 — Clean domain
- Ranked in Alexa/Statvoo top 296,179

---

## Phishing Indicators

- **Identity Spoofing** — Claims to be Microsoft IT
  team but sender domain has no relation to Microsoft
- **URL Masking** — TinyURL used to hide malicious
  destination flagged by multiple vendors
- **Urgency Tactic** — Email creates deadline pressure
  to verify account
- **Embedded Link** — Legitimate Microsoft emails
  do not embed shortened links
- **Credential Harvesting Site** — Destination URL
  contains password-input fields

---

## Conclusion

This is a confirmed phishing attack impersonating
Microsoft IT team. The shortened URL redirects to
a credential harvesting site flagged by multiple
security vendors. Recommended actions:

- Block x-egamb.com at the web gateway
- Add tinyurl.com/ypu5kfts to URL blocklist
- Report to Microsoft phishing team

