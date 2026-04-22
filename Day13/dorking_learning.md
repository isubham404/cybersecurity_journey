# 30 Days of Ethical Hacking: Day 03
## Topic: OSINT & Google Dorking (Passive Recon)

### 📝 Overview
Today I learned how to gather intelligence without interacting with the target server. This is called **Passive Reconnaissance**. By using Google as a tool, I can find leaked data and hidden entry points.

### 🔍 Core Concepts
1. **OSINT (Open Source Intelligence):** The practice of collecting information from publicly available sources (Social Media, Whois, Search Engines).
2. **Google Dorking:** Using advanced search operators to find information that is indexed by Google but not intended for public view.
3. **Information Leakage:** Identifying `filetype:log` or `filetype:env` files that contain sensitive system configurations.

### 🛠️ Lab 3: Passive Search Exercises
*Tested using legal/educational domains.*

| Query | Objective |
| :--- | :--- |
| `site:suiit.ac.in filetype:pdf` | Find all public PDF documents hosted by the university. |
| `intitle:"index of" "parent directory"` | Identify servers with directory listing enabled (Exposure). |
| `inurl:phpmyadmin/setup` | Find misconfigured database setup pages. |

### 💡 Key Takeaway
You don't always need complex tools like Nmap to find a vulnerability. Sometimes, the most sensitive information (like passwords or private keys) is just one Google search away because of poor configuration.

### 🚀 What's Next?
**Day 04: Subdomain Enumeration.** Moving beyond the main website to find "forgotten" servers (e.g., `dev.target.com`).