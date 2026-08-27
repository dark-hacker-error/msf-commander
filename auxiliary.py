
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
"""Auxiliary Modules - Scanners, Fuzzers, DoS, Info Gathering"""

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

def box_alias(title, icon="🔍"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="aux"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def auxiliary_menu():
    section_header("AUXILIARY MODULES (SCAN/FUZZ/DOS)", "🔍")
    
    print(f"""
  {M}[1]{RESET}   {G}TCP Port Scanner{RESET}
  {M}[2]{RESET}   {G}SYN Port Scanner{RESET}
  {M}[3]{RESET}   {G}UDP Port Scanner{RESET}
  {M}[4]{RESET}   {G}Nmap Integration (db_nmap){RESET}
  {M}[5]{RESET}   {G}Service Version Detection{RESET}
  {M}[6]{RESET}   {G}OS Detection{RESET}
  {M}[7]{RESET}   {G}SMB Scanner{RESET}
  {M}[8]{RESET}   {G}SSH Scanner{RESET}
  {M}[9]{RESET}   {G}FTP Scanner{RESET}
  {M}[10]{RESET}  {G}HTTP Title Scanner{RESET}
  {M}[11]{RESET}  {G}HTTP Version Scanner{RESET}
  {M}[12]{RESET}  {G}SNMP Scanner{RESET}
  {M}[13]{RESET}  {G}DNS Enumeration{RESET}
  {M}[14]{RESET}  {G}LDAP Enumeration{RESET}
  {M}[15]{RESET}  {G}NetBIOS Enumeration{RESET}
  {M}[16]{RESET}  {G}SMB Enumeration{RESET}
  {M}[17]{RESET}  {G}VNC Authentication Check{RESET}
  {M}[18]{RESET}  {G}RDP Scanner{RESET}
  {M}[19]{RESET}  {G}MySQL Scanner{RESET}
  {M}[20]{RESET}  {G}PostgreSQL Scanner{RESET}
  {M}[21]{RESET}  {G}MSSQL Scanner{RESET}
  {M}[22]{RESET}  {G}Telnet Scanner{RESET}
  {M}[23]{RESET}  {G}SMTP Enumeration{RESET}
  {M}[24]{RESET}  {G}SNMP Community Brute{RESET}
  {M}[25]{RESET}  {G}HTTP PUT/DELETE Check{RESET}
  {M}[26]{RESET}  {G}SSL/TLS Scanner{RESET}
  {M}[27]{RESET}  {G}XSS Scanner{RESET}
  {M}[28]{RESET}  {G}SQL Injection Scanner{RESET}
  {M}[29]{RESET}  {G}LDAP Injection{RESET}
  {M}[30]{RESET}  {G}SSL Certificate Check{RESET}
  ────────────────────────────────
  {Y}FUZZERS:{RESET}
  {M}[31]{RESET}  {G}HTTP POST Fuzzer{RESET}
  {M}[32]{RESET}  {G}SMTP Fuzzer{RESET}
  {M}[33]{RESET}  {G}SSH Fuzzer{RESET}
  {M}[34]{RESET}  {G}FTP Fuzzer{RESET}
  {M}[35]{RESET}  {G}SMB Fuzzer{RESET}
  ────────────────────────────────
  {Y}DoS:{RESET}
  {M}[36]{RESET}  {G}Slowloris (HTTP){RESET}
  {M}[37]{RESET}  {G}SYN Flood{RESET}
  {M}[38]{RESET}  {G}UDP Flood{RESET}
  {M}[39]{RESET}  {G}ICMP Flood{RESET}
  {M}[40]{RESET}  {G}TCP Flood{RESET}
  ────────────────────────────────
  {Y}FUZZING:{RESET}
  {M}[41]{RESET}  {G}HTTP Path Fuzzer{RESET}
  {M}[42]{RESET}  {G}HTTP Header Fuzzer{RESET}
  {M}[43]{RESET}  {G}SMB Fuzz{RESET}
  {M}[44]{RESET}  {G}SSH Auth Fuzz{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-44]: {RESET}").strip()
    if choice == "0":
        return
    
    target = get_ip("RHOSTS (target IP/CIDR): ")
    port = get_ip("RPORT (optional): ", "")
    
    aux_map = {
        "1": f"use auxiliary/scanner/portscan/tcp\nset RHOSTS {target}\nrun",
        "2": f"use auxiliary/scanner/portscan/syn\nset RHOSTS {target}\nrun",
        "3": f"use auxiliary/scanner/portscan/udp\nset RHOSTS {target}\nrun",
        "4": f"db_nmap -sV -sC {target}",
        "5": f"use auxiliary/scanner/discovery/version_db\nset RHOSTS {target}\nrun",
        "6": f"use auxiliary/scanner/discovery/udp_sweep\nset RHOSTS {target}\nrun",
        "7": f"use auxiliary/scanner/smb/smb_version\nset RHOSTS {target}\nrun",
        "8": f"use auxiliary/scanner/ssh/ssh_version\nset RHOSTS {target}\nrun",
        "9": f"use auxiliary/scanner/ftp/ftp_version\nset RHOSTS {target}\nrun",
        "10": f"use auxiliary/scanner/http/http_version\nset RHOSTS {target}\nrun",
        "11": f"use auxiliary/scanner/http/http_header\nset RHOSTS {target}\nrun",
        "12": f"use auxiliary/scanner/snmp/snmp_enum\nset RHOSTS {target}\nrun",
        "13": f"use auxiliary/gather/dns_enum\nset RHOSTS {target}\nrun",
        "14": f"use auxiliary/scanner/ldap/ldap_enum\nset RHOSTS {target}\nrun",
        "15": f"use auxiliary/scanner/netbios/netbios_smb\nset RHOSTS {target}\nrun",
        "16": f"use auxiliary/scanner/smb/smb_enumshares\nset RHOSTS {target}\nrun",
        "17": f"use auxiliary/scanner/vnc/vnc_auth_none\nset RHOSTS {target}\nrun",
        "18": f"use auxiliary/scanner/rdp/rdp_scanner\nset RHOSTS {target}\nrun",
        "19": f"use auxiliary/scanner/mysql/mysql_version\nset RHOSTS {target}\nrun",
        "20": f"use auxiliary/scanner/postgres/postgres_version\nset RHOSTS {target}\nrun",
        "21": f"use auxiliary/scanner/mssql/mssql_ping\nset RHOSTS {target}\nrun",
        "22": f"use auxiliary/scanner/telnet/telnet_version\nset RHOSTS {target}\nrun",
        "23": f"use auxiliary/scanner/smtp/smtp_enum\nset RHOSTS {target}\nrun",
        "24": f"use auxiliary/scanner/snmp/snmp_login\nset RHOSTS {target}\nrun",
        "25": f"use auxiliary/scanner/http/http_put\nset RHOSTS {target}\nrun",
        "26": f"use auxiliary/scanner/ssl/ssl_version\nset RHOSTS {target}\nrun",
        "27": f"use auxiliary/scanner/http/xss Scanner\nset RHOSTS {target}\nrun",
        "28": f"use auxiliary/scanner/http/sql_injection\nset RHOSTS {target}\nrun",
        "29": f"use auxiliary/scanner/ldap/ldap_search\nset RHOSTS {target}\nrun",
        "30": f"use auxiliary/scanner/ssl/ssl_cert\nset RHOSTS {target}\nrun",
        "31": f"use auxiliary/fuzzers/http/http_post\nset RHOSTS {target}\nrun",
        "32": f"use auxiliary/fuzzers/smtp/smtp_fuzzer\nset RHOSTS {target}\nrun",
        "33": f"use auxiliary/fuzzers/ssh/ssh_version_2\nset RHOSTS {target}\nrun",
        "34": f"use auxiliary/fuzzers/ftp/ftp_fuzzer\nset RHOSTS {target}\nrun",
        "35": f"use auxiliary/fuzzers/smb/smb_fuzzer\nset RHOSTS {target}\nrun",
        "36": f"use auxiliary/dos/http/slowloris\nset RHOSTS {target}\nset RPORT 80\nrun",
        "37": f"use auxiliary/dos/tcp/synflood\nset RHOSTS {target}\nrun",
        "38": f"use auxiliary/dos/network/udp_flood\nset RHOSTS {target}\nrun",
        "39": f"use auxiliary/dos/network/icmp_flood\nset RHOSTS {target}\nrun",
        "40": f"use auxiliary/dos/tcp/tcp_flood\nset RHOSTS {target}\nrun",
        "41": f"use auxiliary/fuzzers/http/http_path\nset RHOSTS {target}\nrun",
        "42": f"use auxiliary/fuzzers/http/http_header_fuzz\nset RHOSTS {target}\nrun",
        "43": f"use auxiliary/fuzzers/smb/smb2_fuzz\nset RHOSTS {target}\nrun",
        "44": f"use auxiliary/fuzzers/ssh/ssh_auth_fuzz\nset RHOSTS {target}\nrun",
    }
    
    if choice in aux_map:
        cmds = aux_map[choice].split("\n")
        if port and choice in ["1","2","3","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]:
            cmds.append(f"set RPORT {port}")
        generate_rc_and_run(cmds, f"aux_{choice}")
    else:
        error("Invalid choice!")
