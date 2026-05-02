# 🧪 Cybersecurity Lab: Web Enumeration & Analysis

## 🎯 Objective
Learn how to:
- Discover hidden directories using Gobuster
- Identify vulnerabilities using Nikto
- Interpret tool output like a real penetration tester
- Pivot from findings to further testing

---

## 🧠 Core Concept

> Hackers don’t attack first — they **enumerate and analyze**.

Web applications often hide:
- Admin panels
- Assets (JS, CSS)
- APIs
- Backup files

---

# ⚙️ Tools Used

## 1. Gobuster
- Used for directory brute-forcing

## 2. Nikto
- Used for web vulnerability scanning

---

# 🧪 Step 1: Directory Enumeration (Gobuster)

## Command Used
```bash
gobuster dir -u https://site.com -w /usr/share/wordlists/dirb/common.txt
Output Found
/assets (Status: 302)
🔍 Interpretation
/assets directory exists
Status 302 = Redirect
Direct access is restricted or controlled
🧠 Meaning of 302 Redirect

Possible reasons:

Authentication required
Direct access blocked
Backend routing (e.g., Salesforce)
⚠️ Common Mistake

❌ Wrong:

gobuster dir -u https://site.com/login?param=...

✔️ Correct:

gobuster dir -u https://site.com -w common.txt
🔄 Next Actions
1. Check Redirect Manually
curl -I https://site.com/assets

Look for:

Location: header
2. Try Subdirectories
/assets/
/assets/js
/assets/css
/assets/images
3. Use Browser DevTools
Open website → Press F12
Go to Network tab
Reload page

Look for:

.js files
API calls
Hidden endpoints
🧪 Step 2: Vulnerability Scan (Nikto)
Command Used
nikto -h https://site.com
🔍 Key Findings
1. Missing HttpOnly Flag
Cookie created without httponly flag
🧠 Meaning:
Cookies accessible via JavaScript
Vulnerable to XSS attacks
2. Uncommon Headers
x-sfdc-edge-cache
x-request-id
x-edge-shared-cache-skip
🧠 Meaning:
Internal system details exposed
Helps in backend fingerprinting
3. Backend Technology Identified
x-powered-by: Salesforce ApexPages
🧠 Meaning:
Application uses Salesforce backend
Can research known vulnerabilities
🔄 Real Hacker Workflow
Step 1: From Gobuster
Identify directories
Investigate accessible resources
Step 2: From Nikto
Analyze:
Cookies
Headers
Technologies
Step 3: Combine Findings

Example:

If JS files found in /assets
And cookies are not HttpOnly
→ Possible XSS attack vector
🧠 Key Skills Learned
Reading tool output (not just running tools)
Understanding HTTP status codes
Identifying security misconfigurations
Thinking in terms of attack surface
🧠 Memory Trick

F A C T

F → Found directories (Gobuster)
A → Analyze headers (Nikto)
C → Check cookies
T → Test parameters
⚠️ Important Notes
Target appears to be a real production system
Likely hardened and protected
Focus on learning, not exploitation
🚀 Next Steps
Extract and analyze JavaScript files
Test URL parameters
Learn Burp Suite for interception
Try labs on:
TryHackMe
Hack The Box
✅ Conclusion

This lab teaches:

How to discover hidden paths
How to analyze web server responses
How to think like a penetration tester

Enumeration + Analysis = Real Cybersecurity Skill