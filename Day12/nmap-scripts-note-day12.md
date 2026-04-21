#🛡️ Day 2: Nmap Scripting Engine (NSE) & Vulnerability Scanning
Date: April 21, 2026

Topic: Automating Vulnerability Discovery

Goal: Move from "Service Identification" to "Vulnerability Assessment."

📖 1. The Concept: What is NSE?
The Nmap Scripting Engine (NSE) is one of Nmap's most powerful features. It allows users to write (and share) simple scripts using the Lua programming language to automate a wide range of networking tasks.

Instead of just checking if a port is open, NSE allows us to:

Vulnerability Detection: Check if a specific service version has a known exploit (CVE).

Backdoor Detection: Look for signs of worms or malware already present on the system.

Exploitation: Perform lightweight exploitation (e.g., trying default passwords).

📂 2. Understanding Script Categories
Nmap scripts are organized into categories. When performing an ethical hack, we select categories based on our "Rules of Engagement":


🛠️ Lab 2: Putting it into Practice
For this lab, I targeted hackthissite.org to identify potential "unlocked windows" on their web server.

Command 1: The "Best of" Discovery Scan
This runs the default set of scripts to gather general intelligence.

Bash
# -sC is equivalent to --script=default
nmap -sV -sC hackthissite.org
What this does: Tells Nmap to find versions (-sV) and then run safe scripts (-sC) to pull things like the page title, server headers, and SSL cert details.

Command 2: The Vulnerability Deep-Dive
This is a targeted scan that checks the versions found against a database of known security holes.

Bash
nmap -sV --script vuln hackthissite.org
What this does: Specifically looks for VULNERABLE indicators. It checks for things like "Slowloris" DoS vulnerabilities or outdated SSL configurations.

Command 3: Web Directory Enumeration
To see if there are hidden folders (like /config or /backup) that are exposed.

Bash
nmap -p 80 --script http-enum hackthissite.org
What this does: It "guesses" common directory names to see if the server returns a 200 OK response.

📊 3. Interpreting Results
When reading the output, I look for the following keywords:

VULNERABLE: The target likely has a security hole.

CVE-XXXX-XXXX: The unique ID for the vulnerability. I can search this on Exploit-DB to find a working exploit.

State: LIKELY VULNERABLE: Nmap isn't 100% sure, but the version number matches a known bad version.

💡 Key Takeaways
Context Matters: A version number (from Day 1) is just a number until it is matched with a script (Day 2) that proves it is dangerous.

Automation Speed: NSE allows a hacker to test for 500+ vulnerabilities in minutes, which would take a human days to do manually.

Ethical Boundary: Running --script vuln or intrusive scripts on a network I don't own can be detected by Firewalls (IDS/IPS). Always scan with permission.