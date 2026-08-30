<div align="center">

# ⚔️ MSF Commander v4.0

### Complete Offensive Security Arsenal for Penetration Testing

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Metasploit](https://img.shields.io/badge/Metasploit-F14E32?style=for-the-badge&logo=metasploit&logoColor=white)](https://metasploit.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Android-blue?style=for-the-badge)]()
[![Payloads](https://img.shields.io/badge/Payloads-24%2B-red?style=for-the-badge)]()
[![Stars](https://img.shields.io/github/stars/dark-hacker-error/msf-commander?style=for-the-badge)](https://github.com/dark-hacker-error/msf-commander/stargazers)
[![Forks](https://img.shields.io/github/forks/dark-hacker-error/msf-commander?style=for-the-badge)](https://github.com/dark-hacker-error/msf-commander/network/members)
[![Issues](https://img.shields.io/github/issues/dark-hacker-error/msf-commander?style=for-the-badge)](https://github.com/dark-hacker-error/msf-commander/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/dark-hacker-error/msf-commander?style=for-the-badge)](https://github.com/dark-hacker-error/msf-commander/pulls)

**⚡ Auto-Install | 📱 Mobile Friendly | 🎯 24+ Payloads | 🔧 Zero Config**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Payloads](#-payloads) • [Contributing](#-contributing)

---

**🔥 The most powerful offensive security tool for penetration testers and ethical hackers.**

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Payloads](#-payloads)
- [Supported Platforms](#-supported-platforms)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)
- [Disclaimer](#-disclaimer)

---

## 📖 About

**MSF Commander v4.0** is a comprehensive offensive security toolkit that simplifies Metasploit Framework operations. Built with Python, it provides an intuitive interface for generating payloads, managing sessions, and executing penetration testing operations.

### 🎯 Why MSF Commander?

| Feature | MSF Commander | Manual Metasploit |
|---------|---------------|-------------------|
| Setup Time | ⚡ Auto-Install | ❌ Manual Config |
| Mobile Support | ✅ Yes | ❌ No |
| Payload Generation | 🎯 24+ Payloads | ⚠️ Limited |
| User Interface | 🎨 User-Friendly | 💻 Terminal Only |
| Speed | 🚀 Fast | 🐢 Slow |

---

## ✨ Features

### 🔧 Core Features
- **🚀 Auto-Installation** - One-click setup for all dependencies
- **📱 Mobile Friendly** - Works on Android (Termux) and desktop
- **🎯 24+ Payloads** - Windows, Linux, Android, macOS payloads
- **🔐 Reverse Shells** - TCP, HTTP, HTTPS reverse connections
- **📊 Session Management** - Easy multi-session handling
- **🎨 User-Friendly Interface** - Color-coded menus and options

### 🛡️ Payload Types
```
✅ Windows Payloads    - EXE, DLL, PowerShell
✅ Linux Payloads      - ELF, Bash
✅ Android Payloads    - APK, DEX
✅ macOS Payloads      - Mach-O
✅ Web Payloads        - PHP, ASP, JSP
✅ Macro Payloads      - Office Documents
```

### ⚡ Advanced Features
- **🔄 Auto-Update** - Always latest version
- **📦 Modular Design** - Easy to extend
- **🎯 Lhost/Lport Configuration** - Simple network setup
- **📊 Payload Encoder** - Bypass antivirus detection
- **🔐 Multi-Handler** - Support multiple connections

---

## 📥 Installation

### 🐧 Linux (Kali/Ubuntu/Debian)

```bash
# Clone the repository
git clone https://github.com/dark-hacker-error/msf-commander.git

# Navigate to directory
cd msf-commander

# Run auto-installer
python3 msf-commander.py --install
```

### 📱 Android (Termux)

```bash
# Install Termux from F-Droid
# Then run:
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/dark-hacker-error/msf-commander.git
cd msf-commander
python msf-commander.py --install
```

### 🐧 Kali Linux (Direct)

```bash
git clone https://github.com/dark-hacker-error/msf-commander.git
cd msf-commander
chmod +x msf-commander.py
python3 msf-commander.py
```

---

## 🚀 Usage

### Quick Start

```bash
# Launch MSF Commander
python3 msf-commander.py

# Or with specific options
python3 msf-commander.py --lhost 192.168.1.100 --lport 4444
```

### 📱 Generate Payload

```bash
# Windows Reverse TCP
python3 msf-commander.py --payload windows/meterpreter/reverse_tcp

# Android Reverse TCP
python3 msf-commander.py --payload android/meterpreter/reverse_tcp

# Linux Reverse TCP
python3 msf-commander.py --payload linux/x86/meterpreter/reverse_tcp
```

### 🔧 Options

| Option | Description | Example |
|--------|-------------|---------|
| `--install` | Auto-install dependencies | `--install` |
| `--lhost` | Local host IP | `--lhost 192.168.1.100` |
| `--lport` | Local port | `--lport 4444` |
| `--payload` | Payload type | `--payload windows/meterpreter/reverse_tcp` |
| `--output` | Output file | `--output shell.exe` |

---

## 🎯 Supported Payloads

### 📱 Mobile Payloads
| Payload | Platform | Description |
|---------|----------|-------------|
| `android/meterpreter/reverse_tcp` | Android | Full Android control |
| `android/meterpreter/reverse_http` | Android | HTTP-based connection |
| `android/shell/reverse_tcp` | Android | Basic shell access |

### 💻 Desktop Payloads
| Payload | Platform | Description |
|---------|----------|-------------|
| `windows/meterpreter/reverse_tcp` | Windows | Full Windows control |
| `windows/meterpreter/reverse_http` | Windows | HTTP-based connection |
| `linux/x86/meterpreter/reverse_tcp` | Linux | Full Linux control |
| `osx/x86/shell_reverse_tcp` | macOS | macOS shell access |

### 🌐 Web Payloads
| Payload | Type | Description |
|---------|------|-------------|
| `php/meterpreter/reverse_tcp` | PHP | PHP web shell |
| `java/jsp_shell_reverse_tcp` | JSP | Java web shell |
| `asp/shell_reverse_tcp` | ASP | ASP web shell |

---

## 📱 Supported Platforms

### ✅ Fully Supported
- **Linux** - Kali, Ubuntu, Debian, Parrot
- **Android** - Via Termux
- **macOS** - Limited support

### ⚠️ Partial Support
- **Windows** - Via WSL
- **iOS** - Not supported

---

## ❓ FAQ

### Q: Is this tool legal?
**A:** MSF Commander is for educational and authorized penetration testing only. Always get proper authorization before testing.

### Q: Does it work on Android?
**A:** Yes! MSF Commander is fully compatible with Android via Termux.

### Q: How many payloads are included?
**A:** MSF Commander v4.0 includes 24+ different payload types.

### Q: Do I need to install Metasploit separately?
**A:** No! The auto-installer handles everything.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### 🐛 Bug Reports
Found a bug? Please [open an issue](https://github.com/dark-hacker-error/msf-commander/issues) with:
- Bug description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔒 Security

For reporting security vulnerabilities, please see [SECURITY.md](SECURITY.md).

---

## ⚠️ Disclaimer

```
This tool is provided for educational and authorized security testing purposes only.
The author is not responsible for any misuse or damage caused by this program.
Always obtain proper authorization before performing security testing.
Unauthorized access to computer systems is illegal and unethical.
```

---

## 🙏 Support

If you find MSF Commander useful, please give it a ⭐ star on GitHub!

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=dark-hacker-error/msf-commander&type=Date)](https://star-history.com/#dark-hacker-error/msf-commander&Date)

</div>

---

<div align="center">

**Made with ❤️ by Roshan Hacker**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dark-hacker-error)

**⚡ Hack the Planet! 🌍**

</div>
