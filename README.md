# MSF Commander v4.0

<p align="center">
  <a href="https://github.com/dark-hacker-error/msf-commander">
    <img src="https://img.shields.io/badge/Version-4.0-brightgreen?style=for-the-badge" alt="Version"/>
    <img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge" alt="Platform"/>
    <img src="https://img.shields.io/badge/Metasploit-Framework-red?style=for-the-badge" alt="Metasploit"/>
    <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge" alt="Python"/>
    <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License"/>
    <img src="https://img.shields.io/badge/Author-Roshan_Hacker-purple?style=for-the-badge" alt="Author"/>
  </a>
</p>

<p align="center">
  <b>Complete Offensive Security Arsenal for Ethical Hackers</b><br>
  Auto-install dependencies | Mobile-friendly interface | 24+ payload types | Automatic listener setup
</p>

---

## Overview

MSF Commander is a Python-based wrapper for the Metasploit Framework that provides a comprehensive, menu-driven interface for penetration testing and security assessments. It features automatic dependency installation, tool detection, mobile-optimized UI, and seamless payload generation with automatic listener configuration.

### Key Capabilities

| Feature | Description |
|---------|-------------|
| Automatic Tool Detection | Identifies all installed security tools at startup |
| Dependency Auto-Installation | Installs Metasploit, nmap, sqlmap, hydra, and other required tools |
| Mobile-Optimized Interface | Compact design optimized for Termux and Android environments |
| Payload Generator | 24+ payload types with automatic handler configuration |
| Automatic Listener Setup | Starts MSF handler immediately after payload generation |
| SD Card Integration | Generated payloads automatically copied to device storage |
| 13 Attack Modules | Network, web, credentials, post-exploitation, and more |
| Encoding and Evasion | Multiple encoders for antivirus bypass |
| Pivoting and Tunneling | Autoroute, port forwarding, SOCKS proxy support |

---

## Installation

### Prerequisites

- Python 3.x
- Root access (required for Metasploit Framework)
- Internet connection (for initial setup)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/dark-hacker-error/msf-commander.git

# Navigate to the project directory
cd msf-commander

# Run the tool (automatically installs all dependencies)
python3 main.py
```

### Alternative Installation (Android/Termux)

```bash
# Copy to device storage
cp -r msf-commander /storage/emulated/0/Hacking\ tools\ list/

# Run from the new location
python3 "/storage/emulated/0/Hacking tools list/msf-commander/main.py"
```

---

## Usage

### Main Menu

When you launch MSF Commander, you will see the following options:

```
[1]  Setup and Install          - Auto-install all dependencies
[2]  MSF Console               - Launch Metasploit console
[3]  Payload Generator         - Generate payloads with automatic listener
[4]  Start Listener Only       - Quick multi/handler launcher
[5]  List Payloads/Encoders    - View all msfvenom options
[6]  Network Exploits          - EternalBlue, MS17-010, SMB exploits
[7]  Client-Side Exploits      - PDF, Office, Java, Flash exploits
[8]  Local Exploits            - Privilege escalation modules
[9]  Auxiliary Modules         - 44 scanners, fuzzers, DoS tools
[10] Web Attacks               - SQLMap, XSS, directory bruteforce
[11] Credential Attacks        - Brute force, pass-the-hash, John
[12] Post-Exploitation         - 50 post-exploit modules
[13] Evasion and Encoding      - Bypass antivirus with encoders
[14] Pivoting and Tunneling    - Autoroute, portfwd, SOCKS
[15] Mobile Exploits           - Android/iOS meterpreter
[16] Database Attacks          - MySQL, PostgreSQL, MSSQL
[17] Social Engineering        - SET framework integration
[18] Meterpreter Commands      - 70+ meterpreter commands
[19] Reporting and Export      - Nmap integration, database queries
[20] Resource Script Builder   - Create .rc scripts
[21] Tool Detector             - Check all installed tools
```

### Payload Generator

The payload generator supports 24+ payload types across multiple platforms:

**Windows Payloads:**
- Meterpreter (EXE, DLL, MSI, HTA, PowerShell, VBA/Macro, MSBuild XML, CSharp)
- Shell (Reverse TCP)
- HTTPS Reverse
- TCP Bind

**Linux Payloads:**
- Meterpreter (ELF, Python, HTTPS)
- Shell Reverse TCP

**Mobile Payloads:**
- Android Meterpreter (APK)

**Cross-Platform Payloads:**
- Mac OS X Meterpreter (Macho)
- PHP, Python, Ruby, Perl, Node.js Meterpreter
- Java Meterpreter (JAR)
- WAR/ASPX/JSP

### Automatic Handler Setup

When you generate a payload, MSF Commander automatically:

1. Generates the payload using msfvenom
2. Creates a handler resource script (.rc)
3. Copies the payload to /sdcard/
4. Prompts to start the listener
5. Opens msfconsole with the handler configured

```
Payload: android/meterpreter/reverse_tcp
LHOST: 192.168.1.100
LPORT: 4444

Payload generated: /root/instgram.apk
Handler created: /tmp/handler_instgram.rc
Copied to: /sdcard/instgram.apk

Start listener now? (y/n)
```

---

## Auto-Installed Tools

MSF Commander automatically detects and installs the following:

### Python Packages
- colorama
- requests
- dnspython

### System Tools
- nmap
- sqlmap
- hydra
- curl
- wget
- git
- ruby

### Metasploit Framework

Auto-detected from:
- ~/metasploit-framework/msfconsole
- /opt/metasploit-framework/bin/msfconsole
- /usr/bin/msfconsole

Auto-installed via:
1. apt-get install metasploit-framework
2. Rapid7 installer script
3. Git clone with bundle install

---

## Project Structure

```
msf-commander/
├── main.py              # Main entry point and menu system
├── setup.py             # Setup and installation menu
├── exploits.py          # Network, client, local, mobile, database exploits
├── auxiliary.py         # Scanners, fuzzers, denial-of-service modules
├── web_hacking.py       # Web attacks, SQLMap, directory bruteforce
├── cred_attacks.py      # Brute force, pass-the-hash, John the Ripper
├── post_exploit.py      # 50 post-exploitation modules
├── encoders_evasion.py  # Antivirus evasion and encoding
├── pivoting.py          # Autoroute, portfwd, SOCKS proxy
├── meterpreter_cmds.py  # 70+ meterpreter commands
├── reporting.py         # Nmap integration, database queries, export
├── resource_builder.py  # Resource script builder
├── __init__.py          # Package initialization
└── README.md            # This file
```

---

## Technical Details

### Tool Detection

MSF Commander uses a multi-path detection system for Metasploit:

```python
MSF_PATHS = [
    ~/metasploit-framework/msfconsole,
    /opt/metasploit-framework/bin/msfconsole,
    /usr/bin/msfconsole,
    /usr/local/bin/msfconsole,
]
```

### Ruby Warning Suppression

The tool automatically suppresses Ruby gem warnings that can interfere with msfvenom output:

```python
cmd = f'RUBYOPT="-W0" {cmd}'
```

### SD Card Integration

Payloads are automatically copied to available storage:

```python
for sd in ["/sdcard", "/storage/emulated/0"]:
    if os.path.exists(sd):
        shutil.copy2(filepath, os.path.join(sd, filename))
```

---

## Security Notice

This tool is designed for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal and unethical. Always obtain proper authorization before conducting security assessments.

---

## Contributing

Contributions are welcome. Please feel free to submit pull requests, report issues, or suggest new features.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

**Roshan Hacker**

- GitHub: [dark-hacker-error](https://github.com/dark-hacker-error)
- Repository: [msf-commander](https://github.com/dark-hacker-error/msf-commander)

---

## Acknowledgments

- Metasploit Framework by Rapid7
- Kali Linux Team
- Open source security community
