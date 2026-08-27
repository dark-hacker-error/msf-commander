
def box(title, icon="⚔️"):
    print()
    print(f"[31m[1m  ┌{'─'*46}┐[0m")
    print(f"[31m[1m  │[0m  [32m[1m{icon}  [33m[1m{title}[0m  [31m[1m{' '*(43-len(title))}[0m")
    print(f"[31m[1m  └{'─'*46}┘[0m")
    print()

section_header = box

def move_to_sdcard(filepath):
    if not os.path.exists(filepath):
        return False
    for sd in ["/sdcard", "/storage/emulated/0"]:
        if os.path.exists(sd):
            dest = os.path.join(sd, os.path.basename(filepath))
            try:
                import shutil as _sh
                _sh.copy2(filepath, dest)
                print(f"  [32m[1m  ✅ Moved to {dest}[0m")
                return True
            except:
                pass
    print(f"  [36m[1m  ➜ {filepath}[0m")
    return False
#!/usr/bin/env python3
"""Setup & Installation Module"""

import os
import sys
import subprocess
import shutil
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama"], capture_output=True)
    from colorama import Fore, Style, init
    init(autoreset=True)

R, G, Y, B, M, C, W = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
D, BRIGHT, RESET = Style.DIM, Style.BRIGHT, Style.RESET_ALL

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_bar(text="Loading", duration=2):
    dots = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    bar_len = 30
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        prog = i % (bar_len + 1)
        filled = "█" * prog
        empty = "░" * (bar_len - prog)
        pct = int((prog / bar_len) * 100)
        print(f"\r{C}{BRIGHT}  [{G}{filled}{C}{empty}] {pct}% {dots[i % len(dots)]} {text}...{RESET}  ", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print(f"\r{G}{BRIGHT}  ✅ [{'█'*bar_len}] 100% ✓ {text} Done!{RESET}                              ")

def info(msg):
    print(f"  {C}{BRIGHT}  ℹ️  ➤ {msg}{RESET}")

def success(msg):
    print(f"  {G}{BRIGHT}  ✅ ✔ {msg}{RESET}")

def error(msg):
    print(f"  {R}{BRIGHT}  ❌ ✘ {msg}{RESET}")

def warning(msg):
    print(f"  {Y}{BRIGHT}  ⚠️  ⚡ {msg}{RESET}")

def cmd_result(label, value):
    print(f"  {M}{BRIGHT}  ◆ {B}{label}:{RESET} {G}{BRIGHT}{value}{RESET}")

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        return result.returncode == 0, result.stdout, result.stderr
    except:
        return False, "", "Timeout"

def box_alias(title, icon="⚙️"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def check_msf():
    return shutil.which("msfconsole") is not None

def check_msfvenom():
    return shutil.which("msfvenom") is not None

def check_nmap():
    return shutil.which("nmap") is not None

def check_sqlmap():
    return shutil.which("sqlmap") is not None

def setup_menu():
    section_header("SETUP & INSTALLATION", "⚙️")
    
    print(f"""
  {M}[1]{RESET}  {G}🚀  Full Auto-Install (Metasploit + All Tools){RESET}
  {M}[2]{RESET}  {G}📦  Install Metasploit Only{RESET}
  {M}[3]{RESET}  {G}🔍  Install Nmap{RESET}
  {M}[4]{RESET}  {G}💉  Install SQLMap{RESET}
  {M}[5]{RESET}  {G}🕸️  Install Hydra (Brute Force){RESET}
  {M}[6]{RESET}  {G}📡  Install Social Engineering Tools (SET){RESET}
  {M}[7]{RESET}  {G}🔓  Install John the Ripper{RESET}
  {M}[8]{RESET}  {G}🐍  Install Burp Suite Community{RESET}
  {M}[9]{RESET}  {G}🌐  Install Wireshark / TShark{RESET}
  {M}[10]{RESET} {G}📋  Check All Installed Tools{RESET}
  {M}[11]{RESET} {G}🔧  Fix Dependencies (apt-get update){RESET}
  {M}[12]{RESET} {G}🗑️   Uninstall Metasploit{RESET}
  {M}[0]{RESET}  {R}🔙  Back to Main Menu{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-12]: {RESET}").strip()
    
    if choice == "1":
        full_install()
    elif choice == "2":
        install_msf()
    elif choice == "3":
        install_tool("nmap", "apt-get install -y nmap", check_nmap)
    elif choice == "4":
        install_tool("sqlmap", "apt-get install -y sqlmap", check_sqlmap)
    elif choice == "5":
        install_tool("hydra", "apt-get install -y hydra", lambda: shutil.which("hydra"))
    elif choice == "6":
        install_set()
    elif choice == "7":
        install_tool("john", "apt-get install -y john", lambda: shutil.which("john"))
    elif choice == "8":
        install_burp()
    elif choice == "9":
        install_tool("wireshark", "apt-get install -y wireshark tshark", lambda: shutil.which("tshark"))
    elif choice == "10":
        check_all_tools()
    elif choice == "11":
        fix_deps()
    elif choice == "12":
        uninstall_msf()

def full_install():
    print(f"\n  {Y}{BRIGHT}🚀 Starting Full Auto-Install...{RESET}\n")
    
    loading_bar("Updating apt repositories", 3)
    os.system("apt-get update -y 2>/dev/null")
    
    tools = [
        ("Metasploit Framework", "Metasploit", install_msf, check_msf),
        ("Nmap Scanner", "nmap", lambda: install_tool("nmap", "apt-get install -y nmap", check_nmap), check_nmap),
        ("SQLMap", "sqlmap", lambda: install_tool("sqlmap", "apt-get install -y sqlmap", check_sqlmap), check_sqlmap),
        ("Hydra", "hydra", lambda: install_tool("hydra", "apt-get install -y hydra", lambda: shutil.which("hydra")), lambda: shutil.which("hydra")),
        ("John the Ripper", "john", lambda: install_tool("john", "apt-get install -y john", lambda: shutil.which("john")), lambda: shutil.which("john")),
        ("Wireshark", "tshark", lambda: install_tool("wireshark", "apt-get install -y wireshark tshark", lambda: shutil.which("tshark")), lambda: shutil.which("tshark")),
    ]
    
    for name, pkg, installer, checker in tools:
        if checker():
            print(f"  {G}{BRIGHT}  ✅ {name}: Already installed{RESET}")
        else:
            print(f"  {Y}{BRIGHT}  📦 Installing {name}...{RESET}")
            installer()
    
    print()
    success("Full installation complete!")
    check_all_tools()

def install_msf():
    if check_msf():
        success("Metasploit is already installed!")
        return True
    
    info("Installing Metasploit Framework...")
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > /tmp/msfinstall")
    os.system("chmod 755 /tmp/msfinstall")
    loading_bar("Installing Metasploit Framework", 5)
    os.system("/tmp/msfinstall 2>/dev/null")
    os.system("msfdb init 2>/dev/null")
    
    if check_msf():
        success("Metasploit installed successfully!")
        return True
    else:
        # Fallback to apt
        warning("Trying apt install...")
        os.system("apt-get install -y metasploit-framework 2>/dev/null")
        if check_msf():
            success("Metasploit installed via apt!")
            return True
        error("Installation failed. Manual install: https://www.metasploit.com/download")
        return False

def install_tool(name, cmd, checker):
    if checker():
        success(f"{name} is already installed!")
        return
    info(f"Installing {name}...")
    loading_bar(f"Installing {name}", 3)
    os.system(cmd + " 2>/dev/null")
    if checker():
        success(f"{name} installed!")
    else:
        error(f"Failed to install {name}")

def install_set():
    info("Installing Social Engineering Toolkit (SET)...")
    loading_bar("Installing SET", 3)
    os.system("apt-get install -y set 2>/dev/null")
    if shutil.which("setoolkit") or os.path.exists("/usr/share/set"):
        success("SET installed!")
    else:
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit /opt/set 2>/dev/null")
        success("SET cloned to /opt/set")

def install_burp():
    info("Burp Suite Community Edition...")
    warning("Burp Suite requires manual download:")
    print(f"    {Y}https://portswigger.net/burp/communitydownload{RESET}")

def install_tool_generic(name, install_cmd):
    install_tool(name, install_cmd, lambda: shutil.which(name))

def check_all_tools():
    print(f"\n  {C}{BRIGHT}📋 Tool Status:{RESET}\n")
    tools = {
        "msfconsole": "Metasploit Console",
        "msfvenom": "MSFVenom",
        "nmap": "Nmap Scanner",
        "sqlmap": "SQLMap",
        "hydra": "THC Hydra",
        "john": "John the Ripper",
        "tshark": "TShark",
        "setoolkit": "Social Engineering Toolkit",
        "curl": "cURL",
        "wget": "Wget",
        "git": "Git",
        "python3": "Python3",
        "ruby": "Ruby",
        "perl": "Perl",
        "nikto": "Nikto",
        "dirb": "Dirb",
        "gobuster": "Gobuster",
        "wfuzz": "Wfuzz",
        "sublist3r": "Sublist3r",
        "theHarvester": "theHarvester",
        "metagoofil": "Metagoofil",
        "responder": "Responder",
        "enum4linux": "enum4linux",
        "smbclient": "smbclient",
    }
    
    for cmd, name in tools.items():
        if shutil.which(cmd):
            print(f"    {G}{BRIGHT}  ✅ {name:30} {RESET}")
        else:
            print(f"    {R}{BRIGHT}  ❌ {name:30} {RESET}")
    print()

def fix_deps():
    info("Fixing dependencies...")
    loading_bar("Running apt-get update", 3)
    os.system("apt-get update -y 2>/dev/null")
    loading_bar("Upgrading packages", 3)
    os.system("apt-get upgrade -y 2>/dev/null")
    loading_bar("Installing build essentials", 2)
    os.system("apt-get install -y build-essential libreadline-dev libssl-dev libpq-dev libsqlite3-dev libpcap-dev ruby ruby-dev zlib1g-dev autoconf bison libyaml-dev libffi-dev libgdbm-dev libncurses5-dev 2>/dev/null")
    success("Dependencies fixed!")

def uninstall_msf():
    if not check_msf():
        warning("Metasploit is not installed!")
        return
    confirm = input(f"  {R}Are you sure? (y/n): {RESET}").strip().lower()
    if confirm == 'y':
        os.system("apt-get remove -y metasploit-framework 2>/dev/null")
        success("Metasploit uninstalled")
    else:
        info("Cancelled")
