# 🔐 Practical Security Implementation

**Organization:** Remote Hustle
**Participant ID:** AD010001
**Date:** February 22, 2026
**Type:** Internship Task — Stage 1

📄 [Download Full Report (PDF)](./Stage01_CS_ AD010001_SecurityImplementation.pdf)

---

## Overview

Developed and documented a comprehensive security
implementation plan covering password policy,
two-factor authentication setup, and access control
framework for a multi-department organization.

---

## 1. Password Security Policy

### Requirements
- Minimum length: 8 characters
- Must include uppercase, lowercase, number and
  special character (e.g. $, !, @, #, &)
- Password sharing via chat or email is prohibited
- Use password managers for storing credentials

### Password Rotation Guidelines
- Enable MFA (fingerprint, face recognition)
- Change password only when threat is detected
- Restrict and change access when employee leaves

### Secure Storage Best Practices
- Use encryption (e.g. SHA-256)
- Enable biometrics or MFA on password manager app

---

## 2. Two-Factor Authentication (2FA)

**Method:** Google Authenticator App
**Type:** Time-Based One-Time Password (TOTP)

### Activation Steps
1. Navigate to Google Account → Security →
   2-Step Verification → Set up Authenticator
2. Used manual key entry instead of QR code
3. Opened Google Authenticator → + → Enter setup key
4. Input account name, key, and selected Time-based
5. Entered generated code to confirm — added successfully

### Risk Reduction Benefits
- Mitigates credential theft — attacker cannot login
  without the time-based token even with the password
- Provides a second barrier harder to bypass than
  password alone

---

## 3. Access Control Framework

| Department | View Access | Edit Access | Admin Privilege | Approval Authority |
|---|---|---|---|---|
| HR | Employee profiles, payroll | Personal contact, leave requests | None | HR Director |
| Developers | Technical docs, source code | Developer environment | Full sandbox control | Tech Lead |
| Finance | Financial reports, tax documents | Accounts payable, invoices, ledger | None | CFO |
| Marketing | Brand guidelines | Social media, campaign assets | Website Admin | Marketing Manager |
| Admin | Entire company | All | Full database | CEO |

