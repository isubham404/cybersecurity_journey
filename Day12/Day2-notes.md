# 30 Days of Ethical Hacking: Day 02
## Topic: Nmap Scripting Engine (NSE) & Vulnerability Scanning

### 📝 Overview
Today I explored the **Nmap Scripting Engine (NSE)**. While Day 1 was about finding the "Service Version," Day 2 was about using that version to find **Exploitable Vulnerabilities**.

### 🔍 Core Concepts
1. **NSE (Lua Scripts):** Nmap's built-in engine that allows for automated vulnerability detection and network discovery.
2. **Vulnerability Assessment:** Using the `--script vuln` flag to identify specific CVEs (Common Vulnerabilities and Exposures) associated with the target's software versions.
3. **Information Leakage:** Using scripts like `http-enum` to find hidden directories that shouldn't be public.

### 🛠️ Lab Activity
**Target:** `hackthissite.org`

#### Command 1: Default Discovery
```bash
nmap -sC hackthissite.org