
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
"""Reporting & Export Module"""

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

def box_alias(title, icon="📊"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="report"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def reporting_menu():
    section_header("REPORTING & EXPORT", "📊")
    
    print(f"""
  {Y}═══ MSF DATABASE ═══{RESET}
  {M}[1]{RESET}   {G}Show All Hosts{RESET}
  {M}[2]{RESET}   {G}Show All Services{RESET}
  {M}[3]{RESET}   {G}Show All Vulnerabilities{RESET}
  {M}[4]{RESET}   {G}Show All Credentials{RESET}
  {M}[5]{RESET}   {G}Show All Loot{RESET}
  {M}[6]{RESET}   {G}Show Workspace{RESET}
  {M}[7]{RESET}   {G}List Workspaces{RESET}
  {M}[8]{RESET}   {G}Create Workspace{RESET}
  ─────────────────────────────────
  {Y}═══ NMAP INTEGRATION ═══{RESET}
  {M}[9]{RESET}   {G}Nmap Quick Scan (db_nmap){RESET}
  {M}[10]{RESET}  {G}Nmap Full Scan (db_nmap){RESET}
  {M}[11]{RESET}  {G}Nmap Service Version (-sV){RESET}
  {M}[12]{RESET}  {G}Nmap OS Detection (-O){RESET}
  {M}[13]{RESET}  {G}Nmap Script Scan (-sC){RESET}
  {M}[14]{RESET}  {G}Nmap Aggressive (-A){RESET}
  {M}[15]{RESET}  {G}Nmap All Ports (-p-){RESET}
  {M}[16]{RESET}  {G}Nmap Vuln Scan (--script vuln){RESET}
  ─────────────────────────────────
  {Y}═══ EXPORT ═══{RESET}
  {M}[17]{RESET}  {G}Export XML Report{RESET}
  {M}[18]{RESET}  {G}Export HTML Report{RESET}
  {M}[19]{RESET}  {G}Export CSV{RESET}
  {M}[20]{RESET}  {G}Export JSON{RESET}
  {M}[21]{RESET}  {G}Export Nmap XML{RESET}
  {M}[22]{RESET}  {G}Nmap to MSF (db_import){RESET}
  {M}[23]{RESET}  {G}Merge Multiple Scans{RESET}
  ─────────────────────────────────
  {Y}═══ REPORT GENERATION ═══{RESET}
  {M}[24]{RESET}  {G}Generate Full Report{RESET}
  {M}[25]{RESET}  {G}Executive Summary{RESET}
  {M}[26]{RESET}  {G}Technical Findings{RESET}
  {M}[27]{RESET}  {G}Network Topology{RESET}
  {M}[28]{RESET}  {G}Vulnerability Matrix{RESET}
  {M}[29]{RESET}  {G}Credential Report{RESET}
  {M}[30]{RESET}  {G}Custom Report{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-30]: {RESET}").strip()
    if choice == "0":
        return
    
    if choice in ["1", "2", "3", "4", "5"]:
        db_cmds = {
            "1": "hosts",
            "2": "services",
            "3": "vulns",
            "4": "creds",
            "5": "loot",
        }
        generate_rc_and_run([db_cmds[choice]], f"db_query_{choice}")
    
    elif choice == "6":
        generate_rc_and_run(["workspace"], "workspace")
    elif choice == "7":
        generate_rc_and_run(["workspace -l"], "workspace_list")
    elif choice == "8":
        ws = get_ip("Workspace name: ", "default")
        generate_rc_and_run([f"workspace -a {ws}"], "workspace_create")
    
    elif choice in ["9", "10", "11", "12", "13", "14", "15", "16"]:
        target = get_ip("Target IP/CIDR: ")
        nmap_map = {
            "9": f"db_nmap {target}",
            "10": f"db_nmap -sV -sC -O -A {target}",
            "11": f"db_nmap -sV {target}",
            "12": f"db_nmap -O {target}",
            "13": f"db_nmap -sC {target}",
            "14": f"db_nmap -A {target}",
            "15": f"db_nmap -p- {target}",
            "16": f"db_nmap --script vuln {target}",
        }
        generate_rc_and_run([nmap_map[choice]], f"nmap_{choice}")
    
    elif choice in ["17", "18", "19", "20", "21"]:
        outfile = get_ip("Output path: ", f"/root/report")
        export_map = {
            "17": f"db_export -f xml --output {outfile}.xml",
            "18": f"db_export -f html --output {outfile}.html",
            "19": f"db_export -f csv --output {outfile}.csv",
            "20": f"db_export -f json --output {outfile}.json",
            "21": f"db_export -f xml --output {outfile}_nmap.xml",
        }
        generate_rc_and_run([export_map[choice]], f"export_{choice}")
    
    elif choice == "22":
        xml_path = get_ip("Nmap XML path: ", "/root/scan.xml")
        generate_rc_and_run([f"db_import {xml_path}"], "db_import")
    
    elif choice == "23":
        info("Merging scans is automatic in MSF - all scans go to same DB")
    
    elif choice in ["24", "25", "26", "27", "28", "29", "30"]:
        info("Report generation:")
        cmds = [
            "hosts -c address,name,os_name,os_flavor,os_sp",
            "services -c port,proto,name,info,state",
            "vulns -c host,port,name,risk,info",
            "creds -c user,pass,type,host,port",
        ]
        generate_rc_and_run(cmds, f"report_{choice}")
