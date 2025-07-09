# 🔐 cPanel Pentesting Toolkit

**Author:** Ariyan Bin Bappy  
**Group:** Octo Dark Cyber Squad  
**Type:** Ethical Hacking Toolkit  
**Use:** Security research, brute-force testing, wordlist generation  
⚠️ **For authorized testing and educational use only.**

---

## 📦 Included Tools

### 1. 🔓 `cpanel_cracker.py`

Multi-threaded brute-force tool for testing `cPanel` login portals (`:2082`, `:2083`).

- Supports combo lists or separate username/password files
- Proxy rotation support
- Stops at first successful login
- Clean output (success/fail per attempt)

**Usage:**
```bash
python3 tools/cpanel_cracker.py
