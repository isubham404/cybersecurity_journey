# 30 Days of Ethical Hacking: Day 04
## Topic: Subdomain Enumeration (Finding Forgotten Assets)

### 📝 Overview
Today I learned that a target's main website is only the tip of the iceberg. **Subdomain Enumeration** is the process of mapping out all the "hidden" servers belonging to an organization.

### 🔍 Core Concepts
1. **Attack Surface:** The total number of points (subdomains, IPs) where an attacker can try to enter.
2. **Certificate Transparency (CT) Logs:** Public logs of all SSL certificates. These often reveal secret subdomains like `internal.target.com`.
3. **Passive vs Active:** Passive (using APIs/Logs) is stealthy; Active (Brute-forcing DNS) is thorough but detectable.

### 🛠️ Lab 4: Enumeration Tools & Commands

| Tool | Command | Purpose |
| :--- | :--- | :--- |
| **Subfinder** | `subfinder -d <target> -o results.txt` | Fast passive subdomain discovery. |
| **HTTPX** | `cat results.txt | httpx -sc -title` | Validates which subdomains are alive. |
| **crt.sh** | Browser-based search | Uses SSL logs to find historical subdomains. |

### 💡 Key Takeaway
Vulnerabilities are rarely found on the main homepage. They are found on the `dev-test.target.com` subdomain that a developer forgot to turn off three years ago.

### 🚀 What's Next?
**Day 05: Vulnerability Scanning & Analysis.** Now that we have a list of subdomains, how do we automatically find which one is "breakable"?