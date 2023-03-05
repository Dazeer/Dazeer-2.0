import base64, os, sys, requests, time, ctypes, pygetwindow as gw, json, random, colorama, threading, wmi, subprocess, winreg, uuid, re, requests, urllib.parse, httpx
from base64 import b64encode
from urllib.request import Request, urlopen
from datetime import datetime

dtype = "Public"

def logIt(event):
    global logFilename
    dt_string = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(logFilename,"a") as e: e.write(f"[{dt_string}]    {event}\n")

def resizeWindow(width, height):
    os.system(f'mode con: cols={width} lines={height}')

def crash(type="unknown"):
    logIt(f"Crashed: {type}")
    p = ctypes.pointer(ctypes.c_char.from_address(5)); p[0] = b'x'

def checkForDebuggers():
    while True:
        programs = [
            "httpdebuggerui","wireshark","fiddler","regedit","vboxservice","df5serv","vboxtray","vmtoolsd","vmwaretray",
            "ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc",
            "prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver""dnSpy",
            "ExtremeDumper","ExtremeDumper-x86","HTTP Debugger","HTTPDebuggerSvc","HTTPDebuggerUI","Process Hacker","procexp64",
            "debug","crack","dump","snif","http","hack","steal","memory","http","dbg","leak","vmware","pycdc","vm","analyze",
            "network","vm","spy","inject","clone"
        ]
        current_programs = gw.getAllTitles()
        for program in programs:
            for sex in current_programs:
                if program.lower() in str(sex).lower():
                    try:
                        logIt(f"Detected keyword '{program}' retard in '{sex}'")
                        time.sleep(0.2)
                        crash(type="Anti Debug")
                    except: crash(type="Anti Debug")
        time.sleep(1)

def checkVM():
    # 1
    # if len(wmi.WMI().Win32_PortConnector()) == 0: 
    #     crash(type=f"antiVM 1 - {len(wmi.WMI().Win32_PortConnector())}")

    # 2
    try:
        gpu = subprocess.check_output(r"wmic path win32_VideoController get name", creationflags=0x08000000).decode().strip("Name\n").strip()
    except Exception:
        gpu = "N/A"
    blackListedGPU = [
        "Microsoft Remote Display Adapter", "Microsoft Hyper-V Video", "Microsoft Basic Display Adapter", "VMware SVGA 3D", "Standard VGA Graphics Adapter",
        "NVIDIA GeForce 840M", "NVIDIA GeForce 9400M", "UKBEHH_S", "ASPEED Graphics Family(WDDM)", "H_EDEUEK", "VirtualBox Graphics Adapter", "K9SC88UK",
        "Стандартный VGA графический адаптер",
    ]
    for black_gpu in blackListedGPU:
        if black_gpu.strip() in gpu.split('\n'): crash(type="antiVM 2")

    # 3
    vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
    virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")
    time.sleep(2)

    if os.path.exists(vmware_dll): 
        crash(type="antiVM 3")
    elif os.path.exists(virtualbox_dll): 
        crash(type="antiVM 3.5")

    # 4
    reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
    reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
    if reg1 != 1 and reg2 != 1: 
        crash(type="antiVM 4")

    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
    try:
        reg_val = winreg.QueryValueEx(handle, '0')[0]
        if ("VMware" or "VBOX") in reg_val: crash(type="antiVM 4.5")
    finally:
        winreg.CloseKey(handle)

    # 5
    vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
    virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")

    if os.path.exists(vmware_dll):crash(type="antiVM 5")
    elif os.path.exists(virtualbox_dll):crash(type="antiVM 5.5")

    #6
    if hasattr(sys, 'real_prefix'):crash(type="antiVM 6")

    #7
    if str(uuid.UUID(int=uuid.getnode())) == "00000000-0000-0000-0000-000000000000":crash(type="antiVM 7")

def initializeDazeer():
    global logFilename, buildNumber
    os.system("cls")
    print(f"{colorama.Fore.LIGHTWHITE_EX}Initializing Dazeer")
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H.%M.%S")
    logFilename = f"logs/{dt_string}.txt"
    #checkVM()
    #time.sleep(0.2)
    #threading.Thread(target=checkForDebuggers, daemon=True).start()
    try:
        # if (os.path.exists("requests.py") or os.path.exists("keyauth.py") or os.path.exists("auth.py")) and not os.path.exists("dazeer.py"):
        #     sys.exit()
        try:
            if not os.path.isdir("logs"):
                os.mkdir("logs")
        except:
            print("Error creating logs folder")
            time.sleep(15)
            sys.exit()
        try:
            if not os.path.isdir("lib"):
                os.mkdir("lib")
        except:
            print("Error creating lib folder")
            time.sleep(15)

        try:
            if not os.path.isdir("checker"):
                os.mkdir("checker")
        except:
            print("Error creating checker folder")
            time.sleep(15)
            
        try:
            if not os.path.exists("lib/config.json"):
                print(".", end="", flush=True)
                with open("lib/config.json", "w") as f:
                    print(".", end="", flush=True)
                    f.write("""{
	"serviceToUse": "capmonster",
    "2captcha_key": "",
    "anticaptcha_key": "",
    "capmonster_key": "",
	
    "theme": "Hell",
	
    "themes_avalible": [
        "Classic",
        "BlackNWhite",
        "Hell",
        "Custom"
    ],
    "colors": [
        "blue",
        "green",
        "cyan",
        "light_black",
        "light_blue",
        "light_cyan",
        "light_green",
        "light_magenta",
        "light_red",
        "light_white",
        "light_yellow",
        "magenta",
        "red",
        "white",
        "yellow",
        "cyan"
    ],
	"first_color_title": "light_white",
	"second_color_title": "blue",
	
    "first_color_text": "light_blue",
    "second_color_text": "light_white",
	"third_color_text": "blue",
	
    "proxies": false,
	"timeout": 5,
	
    "rpc": true,

    "cf_clearance": "PUT IN UR CLOUDFLARE COOKIE HERE (ONLY REQUIRED FOR THE LEOTA BYPASS)"
}""")
        except:
            print("Error creating config file")
            time.sleep(15)
            sys.exit()
            
        try:
            try:
                path = os.path.join(os.getenv("APPDATA"), "dazeer")
                if not os.path.exists(path):
                    os.mkdir(path)
            except:
                print(f"Failed to create folder {path}, please check your permissions.")
                input()
                
            try:
                path = os.path.join(os.getenv("APPDATA"), "dazeer", "license.txt")
                if not os.path.exists(path):
                    open(path, "w").close()
            except:
                print(f"Failed to create file {path}, please check your permissions.")
                input()
            config = getConfig()
            if "license" in config:
                with open(os.path.join(os.getenv("APPDATA"), "dazeer", "license.txt"), "w") as f:
                    f.write(config["license"])
                del config["license"]
                with open("lib/config.json", "w") as f:
                    json.dump(config, f, indent=4)
            
            
        except Exception as e:
            print("Error creating themes folder")

        try:
            if not os.path.exists("lib/tokens.txt"):
                with open("lib/tokens.txt", "w") as f:
                    f.write("")
        except:
            print("Error creating tokens.txt")
            time.sleep(15)
            sys.exit()
        try:
            if not os.path.exists("lib/proxies.txt"):
                with open("lib/proxies.txt", "w") as f:
                    f.write("use paid proxies NOT FREE ONES in this format username:password@host:port or ip:port")
        except:
            print("Error creating proxies.txt")
            time.sleep(15)
            sys.exit()

        try:
            if not os.path.exists("lib/messages.txt"):
                with open("lib/messages.txt", "w") as f:
                    f.write("select random message from file in the flooder module will select a random messgae here. Note to do go down like\nthis\nlol you put <down>")
        except:
            print("Error creating messages.txt")
            time.sleep(15)
            sys.exit()
            
    except Exception as e:
        logs.error("Not able to initialize Dazeer - " + str(e))

def getHeaders(token,proxy,timeout):
    agent,superProps = ans()
    return {
            "Authorization": token.strip(),
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": agent,
            "X-Super-Properties": superProps,
            "x-fingerprint": request_fingerprint(proxy,timeout)
        }



def getCf():
    a = requests.get("https://canary.discord.com/register").text
    return requests.post("https://canary.discord.com/cdn-cgi/bm/cv/result?req_id=" + a.split("r:'")[1].split("',s")[0], json={
        "m": a.split(",m:'")[1].split("',s:")[0],
        "results": [
            "7164c983523706caccbb62458b75c956",
            "9817e8e50c9c14a4bb4806b4b70f65d6"
        ],
        "timing": random.randint(100,130),
        "fp": {
            "id": 3,
            "e": {
                "r": [
                    2560,
                    1440
                ],
                "ar": [
                    1400,
                    2560
                ],
                "pr": 1,
                "cd": 24,
                "wb": False,
                "wp": False,
                "wn": False,
                "ch": True,
                "ws": False,
                "wd": False
            }
        }
    }).cookies.get("__cf_bm")
    
def ans():
    user_agent = random.choice([
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
			"Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
			"Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
			"Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
			"Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
		])
    sprops = (base64.b64encode(str({
        "os":"Windows",
        "browser":"Chrome",
        "device":"",
        "system_locale":"en-US",
        "browser_user_agent":user_agent,
        "browser_version":user_agent.split("Chrome/")[1].split(" ")[0],
        "os_version":"10",
        "referrer":"https://www.bing.com/",
        "referring_domain":"www.bing.com",
        "search_engine":"bing",
        "referrer_current":"",
        "referring_domain_current":"",
        "release_channel":"stable",
        "client_build_number":138429,
        "client_event_source":None
    }).encode("ascii"))).decode()
    return user_agent, sprops

def getClientData():
    client_request = (urlopen(Request(f'https://discord.com/app', headers={'User-Agent': 'Mozilla/5.0'})).read()).decode('utf-8')
    jsFileRegex = re.compile(r'([a-zA-z0-9]+)\.js', re.I)
    asset = jsFileRegex.findall(client_request)[-1]
    assetFileRequest = (urlopen(Request(f'https://discord.com/assets/{asset}.js', headers={'User-Agent': 'Mozilla/5.0'})).read()).decode('utf-8')
    try:
        build_info_regex = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+')
        build_info_strings = build_info_regex.findall(assetFileRequest)[0].replace(' ', '').split(',')
    except (RuntimeError, TypeError, NameError):
        print(RuntimeError or TypeError or NameError)
    build_num = build_info_strings[0].split(':')[-1]
    return build_num

def request_fingerprint(proxy,timeout):
    agent,superProps = ans()
    try:
        logIt("Trying to get fingerprint")
        regheaders = {
            "accept": "*/*",
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/auth/register",
            "scheme": "https",
            "origin": "discord.com",
            "referer": "discord.com/register",
            "x-debug-options": "bugReporterEnabled",
            "accept-language": "en-US,en;q=0.9",
            "connection": "keep-alive",
            "content-Type": "application/json",
            "user-agent": agent,
            "x-super-properties": superProps,
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        response2 = requests.get("https://discord.com/api/v9/experiments", headers=regheaders, proxies=proxy, timeout=timeout).json()
        fingerprint = response2["fingerprint"]
        logIt(f"Got fingerprint {fingerprint}")
        return fingerprint
    except:
        logIt("Failed to get fingerprint")
        return ""

def request_cookie(proxy,timeout):
    logIt("Getting Cookie")
    return dict(httpx.get("https://discord.com/", proxies=proxy, timeout=timeout).cookies)

import ctypes
def setTitle(title):
    try:
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")
        if os.name == "posix":
            print(f'\33]0;{title}\a', end='', flush=True)
    except:
        pass
    


def removeDups(file):
    lines=open(file, 'r').readlines()
    lines_set = set(lines)
    out=open(file, 'w')
    for line in lines_set:
        out.write(line)


def getConfig():
    with open("lib/config.json", "r") as f:
        return json.load(f)



def getColor(color):
    if color == "blue": return colorama.Fore.BLUE
    elif color == "green": return colorama.Fore.GREEN
    elif color == "cyan": return colorama.Fore.CYAN
    elif color == "light_black": return colorama.Fore.LIGHTBLACK_EX
    elif color == "light_blue": return colorama.Fore.LIGHTBLUE_EX
    elif color == "light_cyan": return colorama.Fore.LIGHTCYAN_EX
    elif color == "light_green": return colorama.Fore.LIGHTGREEN_EX
    elif color == "light_magenta": return colorama.Fore.LIGHTMAGENTA_EX
    elif color == "light_red": return colorama.Fore.LIGHTRED_EX
    elif color == "light_yellow": return colorama.Fore.LIGHTYELLOW_EX
    elif color == "light_white": return colorama.Fore.LIGHTWHITE_EX
    elif color == "magenta": return colorama.Fore.MAGENTA
    elif color == "red": return colorama.Fore.RED
    elif color == "white": return colorama.Fore.WHITE
    elif color == "yellow": return colorama.Fore.YELLOW
    elif color == "cyan": return colorama.Fore.CYAN
    
def onlyText():
    os.system("cls")
    color1, color2, color3, color1_title, color2_title = getColors()
    if dtype == "Public":
        print(f"""
                   {color1_title} ██████{color2_title}╗{color1_title}   █████{color2_title}╗{color1_title}  ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ██████{color2_title}╗{color1_title}
                    ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}███{color2_title}╔{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title}
                    ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ███████{color2_title}║{color1_title}   ███{color2_title}╔{color1_title}{color2_title}╝{color1_title}  █████{color2_title}╗{color1_title}   █████{color2_title}╗{color1_title}   ██████{color2_title}╔{color1_title}{color2_title}╝{color1_title}
                    ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}║{color1_title}  ███{color2_title}╔{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title}
                    ██████{color2_title}╔{color1_title}{color2_title}╝{color1_title} ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title}
                    {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}""")
    elif dtype == "Beta":
        print(f"""
                {color1_title} ██████{color2_title}╗{color1_title}   █████{color2_title}╗{color1_title}  ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ██████{color2_title}╗{color1_title}
                 ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}███{color2_title}╔{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title}
                 ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ███████{color2_title}║{color1_title}   ███{color2_title}╔{color1_title}{color2_title}╝{color1_title}  █████{color2_title}╗{color1_title}   █████{color2_title}╗{color1_title}   ██████{color2_title}╔{color1_title}{color2_title}╝{color1_title}
                 ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}║{color1_title}  ███{color2_title}╔{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}   ██{color2_title}╔{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}██{color2_title}╗{color1_title}
                 ██████{color2_title}╔{color1_title}{color2_title}╝{color1_title} ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ███████{color2_title}╗{color1_title} ██{color2_title}║{color1_title}  ██{color2_title}║{color1_title}
                 {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title} {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝{color1_title}  {color2_title}╚{color1_title}{color2_title}═{color1_title}{color2_title}╝ {color2_title}[{color1_title}Beta{color2_title}]""")

def hideToken(token):
    color1, color2, color3, color1_title, color2_title = getColors()
    return token.split(".")[0]+"."+token.split(".")[1]+f"{color2}."+len(token.split(".")[2])*"●"

from colorama import Fore
def getColors():
    if getConfig()["theme"] == "Classic":
        color1 = colorama.Fore.LIGHTWHITE_EX
        color2 = colorama.Fore.LIGHTMAGENTA_EX
        color3 = colorama.Fore.MAGENTA
        color1_title = colorama.Fore.LIGHTMAGENTA_EX
        color2_title = colorama.Fore.MAGENTA
        
    elif getConfig()["theme"] == "BlackNWhite":
        color1 = colorama.Fore.LIGHTWHITE_EX
        color2 = colorama.Fore.LIGHTBLACK_EX
        color3 = colorama.Fore.LIGHTBLACK_EX
        color1_title = colorama.Fore.LIGHTWHITE_EX
        color2_title = colorama.Fore.LIGHTBLACK_EX

    elif getConfig()["theme"] == "Hell":
        color1 = colorama.Fore.LIGHTWHITE_EX
        color2 = colorama.Fore.LIGHTRED_EX
        color3 = colorama.Fore.RED
        color1_title = colorama.Fore.LIGHTRED_EX
        color2_title = colorama.Fore.RED

    elif getConfig()["theme"] == "Custom":
        color1 = getColor(getConfig()["first_color_text"])
        color2 = getColor(getConfig()["second_color_text"])
        color3 = getColor(getConfig()["third_color_text"])

        color1_title = getColor(getConfig()["first_color_title"])
        color2_title = getColor(getConfig()["second_color_title"])
        
    return color1, color2, color3, color1_title, color2_title