# ⚔️ MSF Commander v4.0 - Metasploit Framework Deep Core Commander

<p align="center">
  <img src="https://img.shields.io/badge/Version-4.0-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Metasploit-Framework-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge"/>
</p>

<p align="center">
  🛡️ <b>Complete Offensive Security Arsenal</b> 🛡️<br>
  <i>Auto-install all dependencies • Mobile Friendly UI • Auto-detect Metasploit</i>
</p>

---

## 🔥 What is MSF Commander?

MSF Commander is a **powerful Python-based wrapper** for the Metasploit Framework that provides a **menu-driven, mobile-friendly interface** for ethical hacking and penetration testing. It auto-installs all dependencies, detects tools automatically, and moves payloads to your device storage.

### ⚡ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Auto Tool Detection** | Automatically finds all installed hacking tools |
| 📦 **Auto Install** | Installs missing dependencies (MSF, nmap, sqlmap, etc.) |
| 📱 **Mobile Friendly** | Compact UI optimized for Termux/Android |
| 💣 **Payload Generator** | 24+ payload types with auto handler setup |
| 📡 **Auto Listener** | Starts MSF handler automatically after payload generation |
| 📁 **Auto Move to SD Card** | Generated payloads auto-copy to `/sdcard/` |
| 🎯 **13 Attack Modules** | Network, Web, Credentials, Post-Exploit, and more |
| 🔐 **Evasion & Encoding** | Multiple encoders to bypass AV |
| 🔗 **Pivoting & Tunneling** | Autoroute, Portfwd, SOCKS proxy |

---

## 📸 Screenshots

```
   ╔═══════════════════════════════════╗
   ║   ███╗   ███╗██╗   ██╗██████╗    ║
   ║   ████╗ ████║╚██╗ ██╔╝██╔══██╗   ║
   ║   ██╔████╔██║ ╚████╔╝ ██████╔╝   ║
   ║   ██║╚██╔╝██║  ╚██╔╝  ██╔══██╗   ║
   ║   ██║ ╚═╝ ██║   ██║   ██████╔╝   ║
   ║   ╚═╝     ╚═╝   ╚═╝   ╚═════╝   ║
   ╠═══════════════════════════════════╣
   ║  ⚔️  MSF COMMANDER v4.0  ⚔️      ║
   ║  Mobile Friendly Edition         ║
   ╚═══════════════════════════════════╝
```

---

## 🚀 Quick Setup (Kali Linux / Parrot OS)

### Prerequisites
- Python 3.x
- Root access (for Metasploit)
- Internet connection

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/msf-commander.git

# Navigate to folder
cd msf-commander

# Run the tool (auto-installs everything!)
python3 main.py
```

### Or Copy to /sdcard (Android/Termux)

```bash
# Copy to phone storage
cp -r metasploit_tool /storage/emulated/0/Hacking\ tools\ list/

# Run from there
python3 "/storage/emulated/0/Hacking tools list/metasploit_tool/main.py"
```

---

## 📋 Complete Menu Options

| # | Module | Description |
|---|--------|-------------|
| 1 | ⚙️ Setup & Install | Auto-install all dependencies |
| 2 | 🖥️ MSF Console | Launch Metasploit console |
| 3 | 💣 Payload Generator | Generate 24+ payload types + auto listener |
| 4 | 📡 Start Listener Only | Quick multi/handler launcher |
| 5 | 📋 List Payloads/Encoders | View all msfvenom options |
| 6 | 🌐 Network Exploits | EternalBlue, MS17-010, SMB exploits |
| 7 | 📁 Client-Side Exploits | PDF, Office, Java, Flash exploits |
| 8 | 🔓 Local Exploits | Privilege escalation modules |
| 9 | 🔍 Auxiliary Modules | 44 scanners, fuzzers, DoS tools |
| 10 | 🌐 Web Attacks | SQLMap, XSS, Dir Bruteforce |
| 11 | 🔐 Credential Attacks | Brute force, Pass-the-Hash, John |
| 12 | 🛡️ Post-Exploitation | 50 post-exploit modules |
| 13 | 🎭 Evasion & Encoding | Bypass AV with encoders |
| 14 | 🔗 Pivoting & Tunneling | Autoroute, Portfwd, SOCKS |
| 15 | 📱 Mobile Exploits | Android/iOS meterpreter |
| 16 | 🗄️ Database Attacks | MySQL, PostgreSQL, MSSQL |
| 17 | 📡 Social Engineering | SET framework integration |
| 18 | 🎮 Meterpreter Commands | 70+ meterpreter commands |
| 19 | 📊 Reporting & Export | Nmap integration, DB queries |
| 20 | 🔧 Resource Script Builder | Create .rc scripts |
| 21 | 🔍 Tool Detector | Check all installed tools |

---

## 💣 Payload Generator - Supported Types

### Windows
- [1] Windows Meterpreter (EXE)
- [2] Windows Meterpreter (DLL)
- [3] Windows Meterpreter (MSI)
- [4] Windows Meterpreter (HTA)
- [5] Windows Meterpreter (PowerShell)
- [6] Windows Meterpreter (VBA/Macro)
- [7] Windows Meterpreter (MSBuild XML)
- [8] Windows Meterpreter (CSharp EXE)
- [9] Windows Shell (Reverse TCP)
- [10] Windows Meterpreter (HTTPS Reverse)
- [11] Windows Meterpreter (TCP Bind)

### Linux
- [12] Linux Meterpreter (ELF)
- [13] Linux Meterpreter (Python)
- [14] Linux Shell Reverse TCP
- [15] Linux Meterpreter (HTTPS)

### Mobile
- [16] Android Meterpreter (APK)

### Cross-Platform
- [17] Mac OS X Meterpreter (Macho)
- [18] PHP Meterpreter
- [19] Python Meterpreter
- [20] Ruby Meterpreter
- [21] Perl Meterpreter
- [22] Node.js Meterpreter
- [23] Java Meterpreter (JAR)
- [24] WAR/ASPX/JSP

---

## 📡 Auto-Handler Feature

When you generate a payload, MSF Commander **automatically**:

1. ✅ Generates the payload with msfvenom
2. ✅ Creates a handler .rc script
3. ✅ Copies payload to `/sdcard/`
4. ✅ Asks to start the listener
5. ✅ Opens msfconsole with handler ready

```
Payload: android/meterpreter/reverse_tcp
LHOST: 192.168.1.100
LPORT: 4444

✅ Payload generated: /root/instgram.apk
✅ Handler: /tmp/handler_instgram.rc
✅ Moved to /sdcard/instgram.apk

⚠️  LISTENER CHALANA MAT BHOOLNA!
Option A: Auto-start (ye tool karega)
Option B: Manual - msfconsole -r /tmp/handler_instgram.rc
```

---

## 🛠️ Auto-Installed Tools

MSF Commander automatically detects and installs:

### Python Packages
- `colorama` - Terminal colors
- `requests` - HTTP library
- `dnspython` - DNS toolkit

### System Tools
- `nmap` - Network scanner
- `sqlmap` - SQL injection
- `hydra` - Brute force
- `curl` / `wget` - HTTP clients
- `git` - Version control
- `ruby` - Metasploit dependency

### Metasploit Framework
Auto-detects from:
- `~/metasploit-framework/msfconsole`
- `/opt/metasploit-framework/bin/msfconsole`
- `/usr/bin/msfconsole`

Auto-installs via:
1. `apt-get install metasploit-framework`
2. Rapid7 installer script
3. Git clone + bundle install

---

## 📁 Project Structure

```
metasploit_tool/
├── main.py              # Master entry point + menu
├── setup.py             # Setup & installation menu
├── exploits.py          # Network/Client/Local/Mobile/DB exploits
├── auxiliary.py          # Scanners, fuzzers, DoS modules
├── web_hacking.py       # Web attacks, SQLMap, Dir brute
├── cred_attacks.py      # Brute force, Pass-the-Hash, John
├── post_exploit.py      # 50 post-exploitation modules
├── encoders_evasion.py  # AV evasion & encoding
├── pivoting.py          # Autoroute, Portfwd, SOCKS
├── meterpreter_cmds.py  # 70+ meterpreter commands
├── reporting.py         # Nmap, DB queries, export
├── resource_builder.py  # .rc script builder
└── __init__.py          # Package init
```

---

## ⚠️ Disclaimer

```
This tool is for educational and authorized security testing purposes only.
Unauthorized access to computer systems is illegal and unethical.
Always obtain proper authorization before testing.
The author is not responsible for any misuse of this tool.
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- ⭐ Star this repo if you find it useful!

---

## 📄 License

MIT License - Feel free to use and modify.

---

## 🔗 Links

- [Metasploit Framework](https://www.metasploit.com/)
- [Kali Linux](https://www.kali.org/)
- [Metasploit Documentation](https://docs.metasploit.com/)

---

<p align="center">
  <b>⚔️ Made with ❤️ for Ethical Hackers ⚔️</b><br>
  <i>Stay Legal. Stay Ethical. Keep Hacking!</i>
</p>
