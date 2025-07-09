# 🛠️ cPanel Pentesting Toolkit

**Author:** Ariyan Bin Bappy  
**Group:** Octo Dark Cyber Squad  
**Type:** Ethical Hacking Toolkit  
**Purpose:** For authorized penetration testing and educational cybersecurity research.

---

## 📦 Toolkit Overview

This repo includes two powerful tools for cPanel penetration testing:

| Tool                  | Description                                                    |
|-----------------------|----------------------------------------------------------------|
| `cpanel_cracker.py`   | Multi-threaded cPanel brute force script with proxy support    |
| `password_generator.py` | Username/password/combo wordlist generator                    |

⚠️ **Strictly for authorized and legal testing**. Use responsibly.

---

## 🔓 Tool #1: `odcs_cpanel.py`

Cracks into cPanel login panels running on port `2082` or `2083`.

### 🔑 Features
- Multi-threaded brute-force
- Accepts combo files or separate user/pass lists
- Optional proxy support (HTTP/SOCKS)
- Stops on first success and shows full result
- Clean real-time logging with status


