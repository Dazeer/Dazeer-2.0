import base64
import http
import dazutils
dazutils.initializeDazeer()
import binascii





from ast import arg
from email import header, message
from colorama import Fore
from msvcrt import getch
from selenium import webdriver
from capmonster_python import HCaptchaTask
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from websocket import WebSocket
from json import dumps
from pypresence import Presence
from datetime import datetime, date
import threading, time, os, random, requests, sys, hashlib, keyboard, websocket, urllib.parse, webbrowser, json, urllib, os, colorama, httpx
from keyauth import api
import pygetwindow as gw
from anticaptchaofficial.hcaptchaproxyless import *
import discum
from discum.start.superproperties import SuperProperties
import ssl, string, ctypes
from decimal import Decimal, getcontext

colorama.init()
os.system('cls')

config = json.load(open('lib/config.json'))

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H.%M.%S")
if not os.path.isdir("logs"):
    os.mkdir("logs")
with open(f"logs/{dt_string}.txt","w") as e:
    e.write("BUY DAZEER AT https://discord.gg/KamUuus3M3")
logFilename = f"logs/{dt_string}.txt"

ended = False
endedd = False
name = "N/A"
v = 0
cpm = 0
timeelapsed = ""
hottit = 0
key_auth_version = "2.9.9"
version = "2.9.9DN+"
dtype = "Public"

__lock__ = threading.Lock()
def logPrint(message,end):
    __lock__.acquire()
    print(message, flush=True, end=end)
    __lock__.release()

emp = "ㅤ"+" "*91



def getColor(color):
    if color == "blue": return Fore.BLUE
    elif color == "green": return Fore.GREEN
    elif color == "cyan": return Fore.CYAN
    elif color == "light_black": return Fore.LIGHTBLACK_EX
    elif color == "light_blue": return Fore.LIGHTBLUE_EX
    elif color == "light_cyan": return Fore.LIGHTCYAN_EX
    elif color == "light_green": return Fore.LIGHTGREEN_EX
    elif color == "light_magenta": return Fore.LIGHTMAGENTA_EX
    elif color == "light_red": return Fore.LIGHTRED_EX
    elif color == "light_yellow": return Fore.LIGHTYELLOW_EX
    elif color == "light_white": return Fore.LIGHTWHITE_EX
    elif color == "magenta": return Fore.MAGENTA
    elif color == "red": return Fore.RED
    elif color == "white": return Fore.WHITE
    elif color == "yellow": return Fore.YELLOW
    elif color == "cyan": return Fore.CYAN

dazutils.logIt("Getting Theme")
color1, color2, color3, color1_title, color2_title = dazutils.getColors()
dazutils.logIt("Got theme")

def getDict():
    proxy = random.choice(open("lib/proxies.txt","r+").read().splitlines())
    if config["proxies"]:
        return {'http://': f'http://{proxy}','https://': f'http://{proxy}'}
    else:
        return None

def elapsed():
    try:
        global timeelapsed, ended
        dazutils.logIt("Started elapsed time")
        second = 0
        minute = 0
        hours = 0
        while ended == False:
            second+=1
            if second == 60:
                second = 0
                minute+=1
            if minute == 60:
                minute = 0
                hours+=1;
            timeelapsed = f"{str(hours).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
            time.sleep(1)
    except Exception as e:
        dazutils.logIt(str(e))

def checker():
    dazutils.logIt("Running the checker module")
    global checked, locked, valid, invalid, lines, timeelapsed, ended, checked, tokenzz, filename, fullCap, remFlag
    checked = 0
    valid = 0
    invalid = 0
    locked = 0
    tokenzz = []
    dazutils.onlyText()
    ended = False
    for token in open("lib/tokens.txt", "r+").read().splitlines(): tokenzz.append(token.strip())
    lines = len(tokenzz)
    
    avMode = input(f"                    {color2}[Advanced Mode]{color1} y/n > ")

    filename = None

    if avMode == "y":
        fullCap = input(f"                    {color2}[Full capture]{color1} y/n > ")
        remFlag = input(f"                    {color2}[Remove Flagged]{color1} y/n > ")
        if fullCap == "y":
            filename = f"checker/Hits "+datetime.now().strftime("%d-%m-%Y %H.%M.%S"+".txt")
            with open(filename,"w"): pass
        else:
            with open("lib/tokens.txt", "w"): pass
    else:
        fullCap = "n"
        remFlag = "n"
        with open("lib/tokens.txt", "w"): pass

    dazutils.logIt(f"Imported {lines} Tokens")
    input(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens {color2}(Press enter to continue)")
    
    dazutils.onlyText()
    time.sleep(0.5)
    threads = []
    for token in tokenzz:
        checked += 1
        t = threading.Thread(target=checkToken,args=[token.strip()])
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    
    ended = True
    input(f"\n                    {color2}[Done]{color1} {valid}{color2}/{color1}{lines} {color2}Valid{color1}")
    dazutils.logIt(f"{valid}/{lines} Valid")
    dazutils.logIt("Exited Checker")
    main()

def checkFlag(headers,cookie,proxy,timeout):
    try:
        req1 = requests.get('https://discord.com/api/v9/users/@me',cookies=cookie, headers=headers, proxies=proxy, timeout=timeout)
        if req1.json()["public_flags"] == 1048576: return True
        else: return False
    except: return True

def checkToken(token):
    global checked, locked, valid, invalid, lines, filename, fullCap, remFlag
    while True:
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                headers = dazutils.getHeaders(token,proxy,timeout)
                cookie = dazutils.request_cookie(proxy,timeout)
                req = requests.get('https://discord.com/api/v9/users/@me/settings',cookies=cookie, headers=headers, proxies=proxy, timeout=timeout)
                if remFlag == "y": flagStatus = checkFlag(headers,cookie,proxy,timeout)
                else: flagStatus = False
                break
            except requests.exceptions.Timeout:
                if config["proxies"]:
                    logPrint(f'                    {color3}[Timeout]{color1} {proxy["https"]}',"\n")
                    continue
                else:
                    logPrint(f'                    {color3}[Timeout]{color1} 127.0.0.1',"\n")
                    continue

            except requests.exceptions.ProxyError:
                if config["proxies"]:
                    logPrint(f'                    {color3}[ProxyError]{color1} {proxy["https"]}',"\n")
                    continue
                else:
                    logPrint(f'                    {color3}[ProxyError]{color1} 127.0.0.1',"\n")
                    continue
                
            except Exception as e:
                logPrint(f'                    {color3}[Unknown Error]{color1} {str(e)}',"\n")
                continue
        if req.status_code == 401:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}"
            logPrint(f'                    {color3}[Invalid]{color1} {hidden_tok}',"\n")
            invalid += 1
            tokenzz.remove(token)
            break

        elif req.status_code == 200 and not flagStatus:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color2}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}"
            logPrint(f'                    {color2}[Valid]{color1} {hidden_tok}',"\n")
            valid += 1
            if fullCap == "n":
                with open("lib/tokens.txt", "a+") as f:
                    f.write(f"{token}\n")
                break
            else:

                req1 = requests.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',cookies=cookie,headers=headers, proxies=proxy, timeout=timeout)

                used = 0
                boosts = 0

                for a in req1.json():
                    if a["cooldown_ends_at"] == None: pass
                    else: used+=1
                    boosts = len(req1.json())

                req2 = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources',cookies=cookie,headers=headers, proxies=proxy, timeout=timeout)
                if "id" in req2.text: billing = True
                else: billing = False

                req3 = requests.get('https://discord.com/api/v9/users/@me',cookies=cookie,headers=headers, proxies=proxy, timeout=timeout).json()

                b = int(req3["id"])/4194304+1420070400000

                date_format = "%Y:%m:%d"
                a = datetime.strptime(date.today().strftime("%Y:%m:%d"), date_format)
                b = datetime.strptime(datetime.fromtimestamp(b//1000).strftime('%Y:%m:%d'), date_format)
                delta = a - b

                req4 = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions',cookies=cookie,headers=headers, proxies=proxy, timeout=timeout)

                if "id" in req4.text: nitro = True
                else: nitro = False

                try:
                    with open(filename, "a+") as f:
                        f.write(f"{token} -> Token Hit! Username: {req3['username']}#{req3['discriminator']} | Email : {req3['email']}  | Phone : {req3['phone']} | Age : {delta.days} Days | Nitro : {nitro} | Billing : {billing} | Boosts Used : {used}/{boosts} | 2FA : {req3['mfa_enabled']}\n")
                    break
                except:
                    break

        elif req.status_code == 200 and flagStatus:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}"
            logPrint(f'                    {color3}[Flagged]{color1} {hidden_tok}',"\n")
            break

        elif req.status_code == 403:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}"
            logPrint(f'                    {color3}[Locked]{color1} {hidden_tok}',"\n")
            locked +=1
            tokenzz.remove(token)
            break

        elif req.status_code == 429:
            rtime = req.json()["retry_after"]
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}"
            logPrint(f'                    {color3}[Ratelimited]{color1} {hidden_tok}',"\n")
            dazutils.logIt(f"Ratelimited for {rtime}s, sleeping..")
            time.sleep(float(rtime))
            continue

#def passwordinput(prompt):
#    print(prompt, end='', flush=True)
#    buf = b''
#    while True:
#        ch = getch()
#        if ch in {b'\n', b'\r', b'\r\n'}:
#            logPrint('',"\n")
#            break
#        elif ch == b'\x08': # Backspace
#            buf = buf[:-1]
#            print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{"●" * len(buf)}', end='', flush=True)
#        elif ch == b'\x03': # Ctrl+C
#            raise KeyboardInterrupt
#        else:
#            buf += ch
#            print('●', end='', flush=True)
#    return buf.decode(encoding='utf-8')

memberFetchDone = False

def update_title_and_text_dmer():
    try:
        global user_id, lines, ended, dmFailed, sent, dmRatelimited, cpm, timeelapsed, createdDM
        while ended == False:
            dazutils.setTitle(f"Dazeer '{version}' │ {user_id} │ Created DM: {createdDM} │ Sent: {sent} │ Failed: {dmFailed} │ Ratelimited: {dmRatelimited} │ Mpm: {cpm} │ Elapsed: {timeelapsed} │ Tokens: {lines}")
            logPrint(f"    {color2}[Dazeer]{color1} Sent: {color2}{sent}{color1} │ Failed: {color2}{dmFailed}{color1} │ Ratelimited: {color2}{dmRatelimited}{color1} │ Elapsed: {color2}{timeelapsed}{color1} │ Tokens: {color2}{str(lines)}{color1} │ Mpm: {color2}{cpm}{color1}         ","\r")
    except Exception as e:
        dazutils.logIt(str(e))

def dmflooda():
    global user_id, lines, ended, dmFailed, sent, dmRatelimited, createdDM, delay, message, ended
    dazutils.logIt("Running DM Flooder")
    ended = False
    dazutils.onlyText()
    createdDM = 0
    dmFailed = 0
    sent = 0
    lines = 0
    dmRatelimited = 0
    user_id = input(f"                    {color2}[ID]{color1} > ")
    message = str(input(f"                    {color2}[Message]{color1} > "))
    delay = float(input(f"                    {color2}[Delay]{color1} > "))
    lines = len(open("lib/tokens.txt", "r").read().splitlines())
    dazutils.logIt(f"Imported {lines} Tokens")
    input(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens {color2}(Press enter to continue)")
    dazutils.onlyText()
    threading.Thread(target=cpm_counter).start()
    threading.Thread(target=elapsed).start()
    threading.Thread(target=update_title_and_text_dmer).start()
    threading.Thread(target=quiter).start()
    for token in open("lib/tokens.txt","r").read().splitlines():
        dazutils.logIt(f"Created a thread for {token.strip()} (DM Flooder)")
        threading.Thread(target=create_dm, args=[token]).start()

def flooderlol(token, dmChannel):
    global delay, message, ended, sent, dmRatelimited, dmFailed
    dazutils.logIt(f"Flooding {user_id}'s DMs lol")

    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            cookie = dazutils.request_cookie(proxy,timeout)
            context = ssl.create_default_context()
            context.minimum_version.TLSv1_3
            time.sleep(0.1)
            break
        except:
            continue

    while ended == False:
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "authorization": token,
            "content-type": "application/json",
            "cookie": f"__dcfduid={cookie['__dcfduid']}; __sdcfduid={cookie['__sdcfduid']}",
            "origin": "https://discord.com",
            "referer": f"https://discord.com/channels/@me/{dmChannel}",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDA3OTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = httpx.post(f"https://discord.com/api/v9/channels/{dmChannel}/messages", verify=context, headers=headers, json={"content":message}, cookies=cookie, proxies=proxy, timeout=timeout)
                break
            except:
                continue

        if r.status_code == 200:
            dazutils.logIt(f"Sent DM To {user_id} in {dmChannel} using {token}")
            sent += 1
            time.sleep(delay)

        elif r.status_code == 429:
            dmRatelimited += 1
            try:
                rtime = r.json()["retry_after"]
                dazutils.logIt(f"Ratelimited for {rtime}s, sleeping..")
                time.sleep(float(rtime))
            except:
                time.sleep(10)

        else:
            dazutils.logIt(f"DM Failed because of {r.text}")
            dmFailed += 1
            break

def create_dm(token):
    global createdDM, dmFailed, user_id

    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            headers = dazutils.getHeaders(token,proxy,timeout)
            cookie = dazutils.request_cookie(proxy,timeout)
            context = ssl.create_default_context()
            context.minimum_version.TLSv1_3
            time.sleep(0.1)
            break
        except:
            continue

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/json",
        "cookie": f"__dcfduid={cookie['__dcfduid']}; __sdcfduid={cookie['__sdcfduid']}",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "x-context-properties": "e30=",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzk4MDMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

    antiLOCK = httpx.get(f"https://discord.com/api/v9/users/{user_id}/profile", verify=context,headers=headers,cookies=cookie, proxies=proxy, timeout=timeout)

    if antiLOCK.status_code == 200:
        r = httpx.post("https://discord.com/api/v9/users/@me/channels", verify=context, headers=headers,json={"recipients": [user_id]},cookies=cookie, proxies=proxy, timeout=timeout)

        if r.status_code == 200:
            dazutils.logIt(f"Created a DM with {user_id} using {token}")
            createdDM += 1
            idd = r.json()["id"]
            threading.Thread(target=flooderlol, args=[token, idd]).start()
        else:
            dazutils.logIt(f"Failed to create a DM with {user_id} using {token} because {r.text}")
            dmFailed += 1

    elif antiLOCK.status_code == 403:
        dazutils.logIt(f"Failed to create a DM with {user_id} using {token} because it had no mutals with the user or was locked")
        dmFailed += 1

    elif antiLOCK.status_code == 403 or antiLOCK.status_code == 400:
        dazutils.logIt(f"Failed to create a DM with {user_id} using {token} because its an invalid user id")
        dmFailed += 1

def acceptRules():
    global accepted
    dazutils.onlyText()
    dazutils.logIt(f"Running Rules accepter")
    lines = 0
    accepted = 0
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    guild_id = int(input(f"                    {color2}[Guild ID]{color1} > "))
    dazutils.onlyText()
    threads = []
    for token in open("lib/tokens.txt", "r").read().splitlines():
        t = threading.Thread(target=acceptReq, args=[token.strip(),guild_id])
        threads.append(t)
        t.start()
    for x in threads:
        x.join()
    input(f"                    {color2}[Done]{color1} {accepted}/{lines}{color2} Accepted Rules")
    dazutils.logIt("Quit Rules accepter")
    main()

def acceptReq(token,guild_id):
    global accepted
    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            get_rules = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false", headers = dazutils.getHeaders(token,proxy,timeout), cookies=dazutils.request_cookie(proxy,timeout), proxies=proxy, timeout=timeout).json()
            response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", headers = dazutils.getHeaders(token,proxy,timeout), cookies=dazutils.request_cookie(proxy,timeout), json=get_rules, proxies=proxy, timeout=timeout)
            break
        except:
            continue
    short_tok = token.strip().split(".")[0]
    if response2.status_code == 201 or response2.status_code == 204:
        accepted += 1
        logPrint(f"                    {color2}[Accepted]{color1} {short_tok}","\n")
    else:
        logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")






def nicker():
    global nicked, guild_id, nick
    dazutils.onlyText()
    dazutils.logIt("Running the nicker")
    nicked = 0
    lines = 0
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    guild_id = input(f"                    {color2}[Guild]{color1} > ")
    nick = str(input(f"                    {color2}[Nick]{color1} > "))
    dazutils.onlyText()
    
    threads = []
    for token in open("lib/tokens.txt", "r").read().splitlines():
        t = threading.Thread(target=nickReq,args=[token.strip()])
        threads.append(t)
        t.start()
    for x in threads:
        x.join()
    input(f"                    {color2}[Done]{color1} {nicked}/{lines} Nicked")
    dazutils.logIt("Quit the nicker")
    main()


def nickReq(token):
    global nicked, guild_id, nick
    while True:
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/%40me/nick",cookies=dazutils.request_cookie(proxy,timeout), headers = dazutils.getHeaders(token,proxy,timeout), json={"nick": nick}, proxies=proxy, timeout=timeout)
                break
            except:
                continue
        short_tok = token.strip().split(".")[0]
        if r.status_code == 200:
            nicked += 1
            logPrint(f"                    {color2}[Nicked]{color1} {short_tok}","\n")
            break

        elif r.status_code == 429:
            logPrint(f"                    {color3}[Ratelimited]{color1} {short_tok}","\n")
            time.sleep(float(r.json()["retry_after"]))
            continue

        else:
            logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")
            break

def update_title_and_text_joiner():
    global lines, join, invite, failed, ended, timeelapsed
    
    while ended == False:
        time.sleep(0.05)
        dazutils.setTitle(f"Dazeer '{version}'│ {invite} │ Joined: {join} │ Failed: {failed} │ Elapsed: {timeelapsed} │ Tokens: {lines}")

def vcLeave(token):
    global v, guild_id, channel_id, keep_in_vc
    keep_in_vc = False
    time.sleep(4)
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    ws.send(dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": channel_id, "self_mute": True,"self_deaf": True}}))
    for _ in range(3):
        time.sleep(0.2)
        ws.close()

def vcJoin(token):
    global v, guild_id, channel_id, keep_in_vc
    while keep_in_vc:
        ws = WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        ws.send(dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
        ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": channel_id, "self_mute": True,"self_deaf": True}}))
        dazutils.logIt("Pinged the VC")
        time.sleep(2)

def vcLeaver():
    global v, guild_id, channel_id, ws
    lines = 0
    dazutils.onlyText()
    dazutils.logIt("Running the VC Leaver")
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    guild_id = input(f"                    {color2}[Guild]{color1} > ")
    channel_id = input(f"                    {color2}[Voice Chat]{color1} > ")
    dazutils.onlyText()
    
    for token in open("lib/tokens.txt", "r").read().splitlines():
        threading.Thread(target=vcLeave, args=[token.strip()]).start()
    input(f"                    {color2}[Done]{color1} Tokens {color2}: {lines} {color1}Disconnected From {color2}{guild_id}")
    dazutils.logIt("Quit VC Leaver")
    main()

def vcjoiner():
    global v, guild_id, channel_id, ws, keep_in_vc
    keep_in_vc = True
    lines = 0
    dazutils.onlyText()
    dazutils.logIt("Running the VC Joiner")
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    guild_id = input(f"                    {color2}[Guild]{color1} > ")
    channel_id = input(f"                    {color2}[Voice Chat]{color1} > ")
    dazutils.onlyText()
    for token in open("lib/tokens.txt", "r").read().splitlines():
        threading.Thread(target=vcJoin, args=[token.strip()], daemon=True).start()
    input(f"                    {color2}[Done]{color1} Tokens {color2}: {lines} {color1}Connected To {color2}{guild_id}")
    dazutils.logIt("Quit the VC Joiner")
    main()

def cpm_counter():
    dazutils.logIt("Running CPM Counter")
    global sent, cpm, ended
    while ended == False:
        previous = sent
        time.sleep(2)
        after = sent
        cpm = (after-previous) * 30

def captcha_bypass(url, key):
    if config["serviceToUse"] == "capmonster":
        dazutils.logIt("Bypassing Captcha using capmonster")
        capmonster = HCaptchaTask(config["capmonster_key"])
        task_id = capmonster.create_task(url, key)
        result = capmonster.join_task_result(task_id)
        response = result.get("gRecaptchaResponse")
        logPrint(f"                    {color3}[Captcha]{color1} Captcha solved {color3}{response[0:10]}{color2}","\n")
        dazutils.logIt(f"Got captcha key {response}")
        return response

    elif config["serviceToUse"] == "anticaptcha":
        solver = hCaptchaProxyless()
        solver.set_key(config["anticaptcha_key"])
        solver.set_website_url(url)
        solver.set_website_key(key)
        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            logPrint(f"                    {color2}[Captcha]{color1} Captcha solved {color2}{g_response[0:10]}{color1}","\n")
        return g_response

    else:
        dazutils.logIt("Bypassing Captcha using 2captcha")
        api_key = config["2captcha_key"]
        captcha_id = requests.post(f"http://2captcha.com/in.php?key={api_key}&method=hcaptcha&sitekey={key}&pageurl={url}").text.split("|")[1]
        recaptcha_answer = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}").text
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            time.sleep(5)
            recaptcha_answer = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}").text
        key = recaptcha_answer.split("|")[1]
        logPrint(f"                    {color2}[Captcha]{color1} Captcha solved {color2}{key[0:10]}{color1}","\n")
        dazutils.logIt(f"Got captcha key {key}")
        return key

def stop():
    global ended
    ended = True
    dazutils.logIt("Quit an task by holding down 'ESCAPE'")
    main()

def quiter():
    global ended
    while ended == False:
        if keyboard.is_pressed("escape"): stop(); break
        else: time.sleep(1)

def update_title_and_text_flooder():
    global lines, ratelimited, ended
    while ended == False:
        dazutils.setTitle(f"Dazeer '{version}' │ Sent: {sent} │ Failed: {failed} │ Ratelimited: {ratelimited} │ Mpm: {cpm} │ Elapsed: {timeelapsed} │ Tokens: {lines}")
        logPrint(f"    {color2}[Dazeer]{color1} Sent: {color2}{sent}{color1} │ Failed: {color2}{failed}{color1} │ Ratelimited: {color2}{ratelimited}{color1} │ Elapsed: {color2}{timeelapsed}{color1} │ Tokens: {color2}{str(lines)}{color1} │ Mpm: {color2}{cpm}{color1}         ","\r")

def fetch(channel_id,headers):
    global running
    try:
        r = httpx.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100",headers=headers)

        lastMSGid = r.json()[-1]["id"]

        for thing in r.json():
            if not thing["author"]["id"] in ids: ids.append(thing["author"]["id"])
            dazutils.setTitle(f"Dazeer '{version}' │ Fetched : {str(len(ids))}")
    except:
        pass

    while running:
        try:
            r1 = httpx.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?before={lastMSGid}&limit=100",headers=headers)
            for thing in r1.json():
                if not thing["author"]["id"] in ids: ids.append(thing["author"]["id"])
                dazutils.setTitle(f"Dazeer '{version}' │ Fetched : {str(len(ids))}")

            lastMSGid = r1.json()[-1]["id"]

        except:
            break

def flooderShit():
    global version, sent, failed, ratelimited, cpm, timeelapsed, ended, lines, tokenn, logg, want_to_rply__to_msg, channelz, mutlitChjaennel, messages, ids, running, masspingenabled, pings
    dazutils.logIt("Running Flooder")
    sent = 0
    failed = 0
    ratelimited = 0
    dazutils.onlyText()
    lines = 0
    msgid = 0
    ids = []
    channel = 0
    want_to_rply__to_msg = "n"
    channelz = []
    pings = 0

    masspingenabled = input(f"                    {color2}[MassPing]{color1} y/n > ")
    if masspingenabled == "y":
        ids = open("lib/ids.txt","r").read().splitlines()
        logPrint(f"                    {color2}[MassPing]{color1} Scraped {color2}{str(len(ids))}{color1} Members","\n")
        dazutils.setTitle(f"{emp}            Dazeer            ")
        pings = int(input(f"                    {color2}[Pings]{color1} > "))

    mutlitChjaennel = input(f"                    {color2}[Multi]{color1} y/n > ")
    if mutlitChjaennel == "n":
        channel = input(f"                    {color2}[Channel]{color1} > ")
        dazutils.logIt(f"Choose channel as {channel}")
        channelz.append(channel)
        want_to_rply__to_msg = input(f"                    {color2}[Replyer]{color1} y/n > ")
        dazutils.logIt(f"Enabled Repyler")
        if want_to_rply__to_msg == "y":
            msgid = input(f"                    {color2}[Message ID]{color1} > ")
            dazutils.logIt(f"Choose message ID as {msgid}")
    else:
        dazutils.logIt(f"Enabled Mutli mode")

        guild_id = input(f"                    {color2}[Guild]{color1} > ")
        dazutils.logIt(f"Choose guild as {guild_id}")

        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels",cookies=dazutils.request_cookie(proxy,timeout), headers={'Authorization': random.choice(open("lib/tokens.txt",'r').read().splitlines()).strip(), 'Content-Type': 'application/json'}, proxies=proxy, timeout=timeout)
                break
            except Exception as e:
                dazutils.logIt(str(e))

        for thing in r.json():
            if thing["type"] == 0:
                channelz.append(thing["id"])
        logPrint(f"                    {color2}[Channels]{color1} Found {color2}{str(len(channelz))}{color1} Channels","\n")

        dazutils.logIt(f"Fetched Channels {str(channelz)}")

    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")

    messages = []

    messageType = str(input(f"                    {color2}[Messages from file]{color1} y/n > "))
    if messageType == "y":
        msgs = open('lib/messages.txt',encoding='utf-8').read().splitlines()
        logPrint(f"                    {color2}[Tokens]{color1} Imported {color2}{len(msgs)}{color1} Messages","\n")
        for message in msgs:
            messages.append(message)

    else:
        message = str(input(f"                    {color2}[Message]{color1} > "))
        dazutils.logIt(f"Choose message as {message}")
        messages.append(message)

    delay = float(input(f"                    {color2}[Delay]{color1} > "))
    dazutils.logIt(f"Put Float Delay to {delay}")
    bypass_antispam = str(input(f"                    {color2}[Bypass AntiSpam]{color1} y/n > "))

    dazutils.onlyText()
    
    ended = False
    for token in open("lib/tokens.txt", "r").read().splitlines():
        threading.Thread(target=req, args=[token, delay, channel, bypass_antispam, msgid]).start()

    threading.Thread(target=cpm_counter).start()
    threading.Thread(target=elapsed).start()
    threading.Thread(target=update_title_and_text_flooder).start()
    threading.Thread(target=quiter).start()

def req(token, delay, channel, bypass_antispam, msgid):
    global version, sent, failed, ratelimited, cpm, timeelapsed, ended, want_to_rply__to_msg, channelz, mutlitChjaennel, messages, ids, masspingenabled, pings
    timeout=int(config["timeout"])
    proxy=getDict()
    headers = dazutils.getHeaders(token,proxy,timeout)
    while ended == False:
        if masspingenabled == "y":
            msgPings = ""
            for _ in range(pings):
                msgPings = msgPings + f"<@{random.choice(ids)}>"
            message = random.choice(messages).replace('<down>','\n')+" "+msgPings
        else:
            message =  random.choice(messages).replace('<down>','\n')

        random_channel = random.choice(channelz)
        if bypass_antispam == "y" and want_to_rply__to_msg == "n":
            while True:
                try:
                    r = httpx.post(f"https://discord.com/api/v9/channels/{random_channel}/messages",cookies=dazutils.request_cookie(proxy,timeout), headers=headers, json={"content": message+" | "+ "".join(random.sample(" qwerty uiop asdfghjklzxcvbnm QWERTYU IOPASDFG HJKLZXCVB NM1234567 89",6))}, proxies=proxy, timeout=timeout)
                    break
                except:
                    continue

        elif bypass_antispam == "n" and want_to_rply__to_msg == "n":
            while True:
                try:
                    r = httpx.post(f"https://discord.com/api/v9/channels/{random_channel}/messages",cookies=dazutils.request_cookie(proxy,timeout), headers=headers, json={"content": message}, proxies=proxy, timeout=timeout)
                    break
                except:
                    continue

        elif bypass_antispam == "y" and want_to_rply__to_msg == "y":
            while True:
                try:
                    r = httpx.post(f"https://discord.com/api/v9/channels/{random_channel}/messages",cookies=dazutils.request_cookie(proxy,timeout), headers=headers, json={"content": message +" | "+ "".join(random.sample(" qwerty uiop asdfghjklzxcvbnm QWERTYU IOPASDFG HJKLZXCVB NM1234567 89",6)),"message_reference": {"channel_id": channel,"message_id": msgid}}, proxies=proxy, timeout=timeout)
                    break
                except:
                    continue

        elif bypass_antispam == "n" and want_to_rply__to_msg == "y":
            while True:
                try:
                    r = httpx.post(f"https://discord.com/api/v9/channels/{random_channel}/messages",cookies=dazutils.request_cookie(proxy,timeout), headers=headers, json={"content": message,"message_reference": {"channel_id": channel,"message_id": msgid}}, proxies=proxy, timeout=timeout)
                    break
                except:
                    continue

        if r.status_code == 429:
            ratelimited += 1
            try:
                time.sleep(float(r.json()["retry_after"]))
            except:
                time.sleep(5)
        elif r.status_code == 200:
            sent += 1
            time.sleep(delay)
        else:
            failed += 1
            dazutils.logIt(f"Failed to send message on {token.strip()} because {r.text}")
            if mutlitChjaennel == "n":
                time.sleep(100)

def leaver():
    global lines, ratelimited, ended, left, failed, guild_id, timeelapsed
    dazutils.onlyText()
    dazutils.logIt("Started Leaver")
    ended = False
    left = 0
    failed = 0
    ratelimited = 0
    lines = 0
    guild_id = input(f"                    {color2}[Guild]{color1} > ")
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    threading.Thread(target=elapsed).start()
    threading.Thread(target=update_title_and_text_leaver).start()
    dazutils.onlyText()
    
    threads = []
    for token in open("lib/tokens.txt", "r").read().splitlines():
        t = threading.Thread(target=leaveReq, args=[token.strip()])
        threads.append(t)
        t.start()
    for x in threads:
        x.join()
    ended = True
    input(f"                    {color2}[Done]{color1} {left}/{lines} {color2}Left")
    dazutils.logIt("Quit Leaver")
    main()

def leaveReq(token):
    global lines, ratelimited, ended, left, failed, guild_id, timeelapsed
    while True:
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}",cookies=dazutils.request_cookie(proxy,timeout), headers = dazutils.getHeaders(token,proxy,timeout), proxies=proxy, timeout=timeout)
                break
            except:
                continue
        short_tok = token.strip().split(".")[0]
        if r.status_code == 204:
            logPrint(f"                    {color2}[Left]{color1} {short_tok}","\n")
            left+=1
            break

        elif r.status_code == 429:
            logPrint(float(r.json()["retry_after"]),"\n")
            ratelimited+=1
            continue
            
        elif r.status_code == 404:
            logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")
            dazutils.logIt(f"Failed to leave on {token.strip()} because {r.text}")
            failed+=1
            break

def reactor():
    global channel_id, message_id, emoji_converted, react, unreact
    dazutils.onlyText()
    dazutils.logIt("Started Reactor")
    react = 0
    lines = 0
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    reactType = input(f"                    {color2}[Put/Rem]{color1} > ")
    if reactType == "Put":
        logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
        channel_id = int(input(f"                    {color2}[Channel ID]{color1} > "))
        message_id = int(input(f"                    {color2}[Message ID]{color1} > "))
        emoji_type = input(f"                    {color2}[Emoji Type]{color1} discord/nitro > ")

        if emoji_type == "discord":
            webbrowser.open("https://emojis.wiki/discord/)")
            emoji_converted = urllib.parse.quote(input(f"                    {color2}[Emoji]{color1} > "))
        elif emoji_type == "nitro":
            emoji_converted = urllib.parse.quote(input(f"                    {color2}[Emoji]{color1} Emojiname:ID > "))

        dazutils.onlyText()

        for token in open("lib/tokens.txt", "r").read().splitlines():
            threads = []
            for token in open("lib/tokens.txt", "r").read().splitlines():
                t = threading.Thread(target=reactReq,args=[token.strip()])
                threads.append(t)
                t.start()
            for x in threads:
                x.join()
            input(f"                    {color2}[Done]{color1} {react}/{lines} {color2}Reacted")
            main()
    else:
        unreact = 0
        lines = 0
        for token in open("lib/tokens.txt", "r").read().splitlines():
            lines += 1
        dazutils.logIt(f"Imported {lines} Tokens")
        logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
        channel_id = int(input(f"                    {color2}[Channel ID]{color1} > "))
        message_id = int(input(f"                    {color2}[Message ID]{color1} > "))
        emoji_type = input(f"                    {color2}[Emoji Type]{color1} discord/nitro > ")

        if emoji_type == "discord":
            webbrowser.open("https://emojis.wiki/discord/)")
            emoji_converted = urllib.parse.quote(input(f"                    {color2}[Emoji]{color1} > "))
        elif emoji_type == "nitro":
            emoji_converted = urllib.parse.quote(input(f"                    {color2}[Emoji]{color1} Emojiname:ID > "))
        dazutils.onlyText()

        threads = []
        for token in open("lib/tokens.txt", "r").read().splitlines():
            t = threading.Thread(target=unreactReq,args=[token.strip()])
            threads.append(t)
            t.start()
        for x in threads:
            x.join()
        input(f"                    {color2}[Done]{color1} {unreact}/{lines} {color2}Unreacted")
        dazutils.logIt("Quit Reactor")
        main()

def unreactReq(token):
    global channel_id, message_id, emoji_converted, unreact
    while True:
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me", headers = dazutils.getHeaders(token,proxy,timeout), cookies=dazutils.request_cookie(proxy,timeout), proxies=proxy, timeout=timeout)
                break
            except:
                continue
        short_tok = token.strip().split(".")[0]
        if r.status_code == 204:
            unreact += 1
            logPrint(f"                    {color2}[Unreacted]{color1} {short_tok}","\n")
            break
        elif r.status_code == 429:
            logPrint(f"                    {color3}[Ratelimited]{color1} {short_tok}","\n")
            time.sleep(float(r.json()["retry_after"]))
            continue
        else:
            logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")
            dazutils.logIt(f"Failed to unreact on {token.strip()} because {r.text}")
            break


def reactReq(token):
    global channel_id, message_id, emoji_converted, react
    while True:
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me", headers = dazutils.getHeaders(token,proxy,timeout), cookies=dazutils.request_cookie(proxy,timeout), proxies=proxy, timeout=timeout)
                break
            except:
                continue
        short_tok = token.strip().split(".")[0]
        if r.status_code == 204:
            react += 1
            logPrint(f"                    {color2}[Reacted]{color1} {short_tok}","\n")
            break
        elif r.status_code == 429:
            logPrint(f"                    {color3}[Ratelimited]{color1} {short_tok}","\n")
            time.sleep(float(r.json()["retry_after"]))
            continue
        else:
            logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")
            dazutils.logIt(f"Failed to react on {token.strip()} because {r.text}")
            break

def update_title_and_text_leaver():
    global lines, ratelimited, ended, left, failed, guild_id, timeelapsed
    while ended == False:
        dazutils.setTitle(f"Dazeer '{version}' │ {guild_id} │Left: {left} │ Failed: {failed} │ Ratelimited: {ratelimited}│ Elapsed: {timeelapsed} │ Tokens: {lines}")

def joiner():
    global lines, join, invite, failed, ended, skipCap
    dazutils.logIt("Started Joiner")
    dazutils.onlyText()
    ended = False
    invite = input(f"                    {color2}[Invite]{color1} > discord.gg/{color2}")
    avMode = input(f"                    {color2}[Advanced Mode]{color1} y/n > ")

    if avMode == "y":
        delayMini = int(input(f"                    {color2}[Minimum Delay]{color1} > "))
        delayMax = int(input(f"                    {color2}[Maximum Delay]{color1} > "))


    skipCap = str(input(f"                    {color2}[Skip captcha]{color1} y/n > "))

    failed = 0
    join = 0
    lines = 0
    for token in open("lib/tokens.txt", "r").read().splitlines(): lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    input(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens {color2}(Press enter to continue)")
    dazutils.onlyText()
    threading.Thread(target=elapsed).start()
    threading.Thread(target=update_title_and_text_joiner).start()

    guild_info = httpx.get(f"https://discord.com/api/v9/invites/{invite}").json()
    guild_id,channel_id = guild_info["guild"]["id"], guild_info["channel"]["id"]

    if avMode == "n":
        threads = []
        for token in open("lib/tokens.txt", "r").read().splitlines():
            short_tok = token.strip().split(".")[0]
            start_time = time.time()
            t = threading.Thread(target=joinn, args=[token.strip(),short_tok,start_time,guild_id,channel_id])
            threads.append(t)
            t.start()
        for x in threads:
            x.join()
    else:
        for token in open("lib/tokens.txt", "r").read().splitlines():
            short_tok = token.strip().split(".")[0]
            start_time = time.time()
            time.sleep(random.randint(delayMini,delayMax))
            joinn(token.strip(),short_tok,start_time,guild_id,channel_id)

    ended = True
    time.sleep(1)
    input(f"                    {color2}[Done]{color1} {join}/{lines} {color2}Joined")
    dazutils.logIt("Quit Joiner")
    main()

def getCf():
    a = httpx.get("https://discord.com/register").text
    return httpx.post("https://discord.com/cdn-cgi/bm/cv/result?req_id=" + a.split("r:'")[1].split("',s")[0], json={
        "m": a.split(",m:'")[1].split("',s:")[0],
        "results": [
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
        ],
        "timing": random.randint(40, 180),  # Execution time
        "fp": {
            "id": 3,
            "e": {
                "r": [
                    1920,  # Height
                    1080   # Width
                ],
                "ar": [
                    1054,  # availHeight
                    1920   # availWidth
                ],
                "pr": 1,   # Pixel Ratio
                "cd": 24,     # Color Depth
                "wb": False,  # Web-driver
                "wp": False,  # PhantomCall
                "wn": False,  # NightMare
                "ch": True,   # Chrome
                "ws": False,  # Selenium
                "wd": False   # domAutomation
            }
        }
    }).cookies.get("__cf_bm")

def getCookies(channel_id, user_token):
    #__dcfduid __sdcfduid __cfruid
    main_cookies = dict(httpx.get("https://discord.com", headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en-US;q=0.9,en;q=0.8",
        "authorization": user_token,
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": f"https://discord.com/channels/@me/{channel_id}",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }).cookies)

    main_cookies["locale"] = "en-SE"
    main_cookies["__stripe_mid"] = "8a96af44-688c-45d4-af23-b842b4a7f644697e45" #same for everyoine i thnik
    main_cookies["_ga"] = f"GA1.2.{str(time.time())}"
    main_cookies["_gid"] = f"GA1.2.{str(time.time())}"

    main_cookies["__cf_bm"] = getCf()

    time_rn = datetime.today().strftime("%a+%b+%d+%Y")
    clock_rn = urllib.parse.quote(datetime.today().strftime("%H:%M:%S"))

    main_cookies["OptanonConsent"] = f"isIABGlobal=false&datestamp={time_rn}+{clock_rn}+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false"
    return main_cookies

def get_client(header_token, channel_id=""):
    cookie = getCookies(channel_id, header_token)

    return {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'en-GB',
                'authorization': header_token,
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'cookie': f"__dcfduid={cookie['__dcfduid']}; __sdcfduid={cookie['__sdcfduid']}; _ga={cookie['_ga']}; __stripe_mid={cookie['__stripe_mid']}; _gid={cookie['_gid']}; __cfruid={cookie['__cfruid']}; OptanonConsent={cookie['OptanonConsent']}; locale={cookie['locale']}; __cf_bm={cookie['__cf_bm']}",
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'te': 'trailers',
    }, cookie

def joinn(token,short_tok,start_time,guild_id,channel_id):
    global lines, join, invite, failed, ended, skipCap

    headers, cookie = get_client(token, channel_id)
    headers["x-context-properties"] = "eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9"
    headers["content-type"] = "application/json"

    while True:
        try:
            context = ssl.create_default_context(); context.minimum_version.TLSv1_3
            timeout=int(config["timeout"]); proxy=getDict()

            join_req = httpx.post(
                f"https://discord.com/api/v9/invites/{invite}",
                    verify=context,
                    json={},
                    cookies=cookie,
                    headers=headers,
                    proxies=proxy,
                    timeout=timeout
                ); break
                
        except Exception as e: 
            print(str(e))
            continue

    while True:
        try:
            if join_req.status_code == 400 and skipCap == "n":
                logPrint(f"                    {color3}[Captcha]{color1} Captcha Detected Solving..","\n")
                while True:
                    try: 
                        response_captcha = httpx.post(
                            f"https://discord.com/api/v9/invites/{invite}",
                                verify=context,
                                json={"captcha_key": captcha_bypass(f"https://discord.com", join_req.json()['captcha_sitekey'])},
                                cookies=cookie,
                                headers=headers,
                                proxies=proxy,
                                timeout=timeout
                            ); break

                    except Exception as e:
                        print(str(e))
                        continue

                end_time = time.time()
                time_elapsed = round(end_time - start_time,3)
                if response_captcha.status_code == 200:
                    logPrint(f"                    {color2}[Joined]{color1} {short_tok} in {color2}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}(captcha){color1}","\n")
                    dazutils.logIt(f"Joined discord.gg/{invite} using {token.strip()} with captcha in {time_elapsed}")
                    join+=1; break

                elif response_captcha.status_code == 429:
                    print("ratelimited use proxies")
                    time.sleep(float(response_captcha.json()["retry_after"]))
                    continue

                else:
                    error_msg = response_captcha.text
                    dazutils.logIt(f"Failed to join because {error_msg}")
                    logPrint(f"                    {color3}[Failed]{color1} {short_tok} in {color3}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}({error_msg}){color1}","\n")
                    failed +=1; break

            elif join_req.status_code == 200:
                end_time = time.time()
                time_elapsed = round(end_time - start_time,3)
                logPrint(f"                    {color2}[Joined]{color1} {short_tok} in {color2}{time_elapsed}{color1}s","\n")
                dazutils.logIt(f"Joined discord.gg/{invite} using {token.strip()} without captcha in {time_elapsed}")
                join +=1
                break

            elif join_req.status_code == 429:
                print("ratelimited use proxies")
                time.sleep(float(join_req.json()["retry_after"]))
                continue
                
            elif join_req.status_code == 400 and skipCap == "y":
                logPrint(f"                    {color3}[Captcha]{color1} Captcha Detected Skipping..","\n")
                break

            else:
                end_time = time.time()
                time_elapsed = round(end_time - start_time,3)
                error_msg = join_req.json()["message"]
                logPrint(f"                    {color3}[Failed]{color1} {short_tok} in {color3}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}({error_msg}){color1}","\n")
                dazutils.logIt(f"Failed to join because {error_msg}")
                failed +=1; break
                
        except Exception as b:
            end_time = time.time()
            time_elapsed = round(end_time - start_time,3)
            dazutils.logIt(f"Failed to join because {b}")
            failed += 1
            logPrint(f"                    {color3}[Failed]{color1} {short_tok} in {color3}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}({b}){color1}","\n")
            break

def loginToToken():
    dazutils.onlyText()
    dazutils.logIt("Started Login to token")
    token = str(input(f"                    {color2}[Token]{color1} > "))
    j = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"}).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(path = r"drivers").install()), options=opts)

    logPrint(f"                    {color2}[Login]{color1} Logged into {color2}{user}{color1}","\n")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)
    time.sleep(4)
    input(f"                    {color2}[Main]{color1} Continue To Main")
    dazutils.logIt("Quit Login to Token")
    main()

def onliner():
    dazutils.onlyText()
    lines = 0
    dazutils.logIt("Started Onliner")
    type = str(input(f"                    {color1}[{color2}Playing{color1} | {color2}Streaming{color1} | {color2}Watching{color1} | {color2}Listening{color1}] > "))
    game = str(input(f"                    {color1}[{color2}Status{color1}] > "))
    for token in open("lib/tokens.txt","r+").read().splitlines():
        threading.Thread(target=lambda : online(token.replace("\n",""), game, type, "random")).start()
    os.system("cls")
    dazutils.onlyText()
    
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Done]{color1} Tokens {color2}: {lines} {color1}Is Now {color2}Online","\n")

def online(token, game, type, status):
    ws = websocket.WebSocket()
    if status == "random":
        stat = ['online', 'dnd', 'idle']
        status = random.choice(stat)
    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    if type == "Playing":
        gamejson = {
            "name": game,
            "type": 0
        }
    elif type == 'Streaming':
        gamejson = {
            "name": game,
            "type": 1,
            "url": "https://discord.gg/spammer"
        }
    elif type == "Listening":
        gamejson = {
            "name": game,
            "type": 2
        }
    elif type == "Watching":
        gamejson = {
            "name": game,
            "type": 3
        }
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": sys.platform,
                "$browser": "RTB",
                "$device": f"{sys.platform} Device"
            },
            "presence": {
                "game": gamejson,
                "status": status,
                "since": 0,
                "afk": False
            }
        },
        "s": None,
        "t": None
    }
    ws.send(json.dumps(auth))
    ack = {
        "op": 1,
        "d": None
    }
    while True:
        time.sleep(heartbeat_interval / 1000)
        try:
            ws.send(json.dumps(ack))
        except Exception as e:
            break

def friender():
    dazutils.onlyText()
    lines = 0
    friendtype = input(f"                    {color2}[Add/Rem]{color1} > ").lower()
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
    dazutils.logIt(f"Imported {lines} Tokens")
    dazutils.logIt(f"Choose {friendtype}")
    if friendtype == "add":
        name,tag = input(f"                    {color2}[Name]{color1} > ").split("#")
        full = name + "#" + tag
        dazutils.logIt(f"Friending {full} with {lines} Tokens")
        dazutils.onlyText()
        threads = []
        for token in open("lib/tokens.txt","r").read().splitlines():
            t = threading.Thread(target=addSomeone,args = [token.strip(),name,tag,full])
            threads.append(t)
            t.start()
        for x in threads:
            x.join()

        dazutils.logIt(f"Added '{full}' (x{lines})")
        input(f"                    {color2}[Done]{color1} Added {color3}'{full}'{color1} {Fore.LIGHTBLACK_EX}(x{lines})")
        main()

    else:
        lines = 0
        remID = input(f"                    {color2}[ID]{color1} > ")
        dazutils.onlyText()
        threads = []
        for token in open("lib/tokens.txt", "r").read().splitlines():
            lines += 1
        dazutils.logIt(f"Imported {lines} Tokens")

        for token in open("lib/tokens.txt","r").read().splitlines():
            t = threading.Thread(target=removeSomeone,args = [token.strip(),remID])
            threads.append(t)
            t.start()
        for x in threads:
            x.join()

        dazutils.logIt(f"Unfriending {remID} with {lines} Tokens")
        input(f"                    {color2}[Done]{color1} Removed {color3}'{remID}'{color1} {Fore.LIGHTBLACK_EX}(x{lines})")
        main()

def hide_token(token):
    return token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●●"

def removeSomeone(token,remID):
    agent,superProps = dazutils.ans()
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token.strip(),
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": agent,
        "x-context-properties": "eyJsb2NhdGlvbiI6IkZyaWVuZHMifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": superProps
    }
    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            r = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{remID}", headers=headers, cookies=dazutils.request_cookie(proxy,timeout), proxies=proxy, timeout=timeout)
            break
        except:
            continue
    while True:
        if r.status_code == 204:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color2}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({remID})"
            logPrint(f"                    {color2}[Removed]{color1} {hidden_tok}","\n")
            break

        elif r.status_code == 429:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({remID})"
            logPrint(f"                    {color3}[Ratelimited]{color1} {hidden_tok}","\n")
            time.sleep(float(r.json()["retry_after"]))
            continue

        else:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({remID})"
            logPrint(f"                    {color3}[Failed]{color1} {hidden_tok}","\n")
            break

def buttons():
    dazutils.onlyText()
    global pressed_success

    pressed_success = 0
    
    guild_id = str(input(f"                    {color2}[Guild]{color1} > "))
    channel_id = str(input(f"                    {color2}[Channel]{color1} > "))
    message_id = str(input(f"                    {color2}[Message ID]{color1} > "))
    bot_id = str(input(f"                    {color2}[Bot ID]{color1} > "))
    button_name = str(input(f"                    {color2}[Button Name]{color1} > "))

    lines = str(len(open('lib/tokens.txt', 'r+').read().splitlines()))
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    dazutils.onlyText()

    threads = []
    for token in open("lib/tokens.txt", "r+").read().splitlines():

        start_time = time.time()

        t = threading.Thread(target=pressButton,args=[token, guild_id, channel_id, message_id, bot_id, button_name, start_time])
        threads.append(t)
        t.start()
    for x in threads:
        x.join()
    input(f"                    {color2}[Done]{color1} Succesfully pressed {color2}{pressed_success}/{lines}{color2} Times")
    dazutils.logIt("Quit Reactor")
    main()

def pressButton(token, guild_id, channel_id, message_id, bot_id, button_name, start_time):
    global pressed_success

    timeout=int(config["timeout"])
    proxy=getDict()

    nouce = str(Decimal(time.time()*1000-1420070400000)*4194304).split(".")[0]

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC4xMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAuNDY2NC4xMTAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vY2hhbm5lbHMvQG1lIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzgwNDYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

    payload = {
        "type": 3,
        "nonce": str(nouce),
        "guild_id": guild_id,
        "channel_id": channel_id,
        "message_flags": 0,
        "message_id": message_id,
        "application_id": bot_id,
        "session_id": "".join(random.sample(string.ascii_lowercase+string.digits,32)),
        "data": {
            "component_type": 2,
            "custom_id": button_name
        }
    }

    def request_cookie():
        response1 = requests.get("https://discord.com",proxies=proxy, timeout=timeout, headers=headers)
        cookie = response1.cookies.get_dict()
        cookie['locale'] = "us"
        return cookie

    r = requests.post("https://discord.com/api/v9/interactions",proxies=proxy, timeout=timeout, headers=headers, json=payload, cookies=request_cookie())
    short_tok = token.split(".")[0]
    end_time = time.time()
    time_elapsed = round(end_time - start_time,3)
    if r.ok:
        logPrint(f"                    {color2}[Pressed]{color1} {short_tok} in {color2}{time_elapsed}{color1}s ","\n")

    else: logPrint(f"                    {color3}[Failed]{color1} {short_tok} in {color2}{time_elapsed}{color3}s {Fore.LIGHTBLACK_EX}{r.text}","\n")

def addSomeone(token,name,tag,full):
    agent,superProps = dazutils.ans()
    timeout=int(config["timeout"])
    proxy=getDict()
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": agent,
        "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-fingerprint": dazutils.request_fingerprint(proxy,timeout),
        "x-super-properties": superProps
    }
    payload = {
        "discriminator": tag,
        "username": name
    }
    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            r = requests.post("https://discord.com/api/v9/users/@me/relationships", json=payload, headers=headers, cookies=dazutils.request_cookie(proxy,timeout), proxies=proxy, timeout=timeout)
            break
        except:
            continue
    while True:
        if r.status_code == 204:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color2}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({full})"
            logPrint(f"                    {color2}[Added]{color1} {hidden_tok}","\n")
            break

        elif r.status_code == 429:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({full})"
            logPrint(f"                    {color3}[Ratelimited]{color1} {hidden_tok}","\n")
            time.sleep(float(r.json()["retry_after"]))

        else:
            hidden_tok = token.split(".")[0] + "." + token.split(".")[1] + f"{color3}.●●●●●●●●●●●●●●●●●●●●●●●●●●● {Fore.LIGHTBLACK_EX}({full})"
            logPrint(f"                    {color3}[Failed]{color1} {hidden_tok}","\n")
            break

def extract():
    dazutils.onlyText()
    dazutils.logIt("Running extracter")
    tokenennenz = []
    lines = 0
    for token in open("lib/tokens.txt", "r").read().splitlines():
        lines += 1
        tokenennenz.append(token.strip())
    dazutils.logIt(f"Imported {lines} Tokens")
    logPrint(f"                    {color2}[Tokens]{color1} Loaded {color2}{lines}{color1} Tokens","\n")
    with open("lib/tokens.txt",'w') as f:
        pass
    for tokenShit in tokenennenz:
        for thing in tokenShit.strip().split(":"):
            if "." in thing.strip() and not "@" in thing.strip() and not "?" in thing.strip() and not "!" in thing.strip() and not "/" in thing.strip():
                with open("lib/tokens.txt","a+") as e:
                    e.write(thing.strip() + "\n")
    cleanedTokens = list(dict.fromkeys(open("lib/tokens.txt","r").read().splitlines()))
    with open("lib/tokens.txt",'w') as f:
        pass
    for token in cleanedTokens:
        with open("lib/tokens.txt",'a+') as f:
            f.write(token.strip() + "\n")
    logPrint(f"                    {color2}[Tokens]{color1} Extracted {color2}{lines}{color1}","\n")
    dazutils.logIt(f"Extracted {lines} Tokens")
    dupsRemoved = str(len(cleanedTokens)-lines).replace("-","")
    dazutils.logIt(f"Removed {dupsRemoved} Duplicates")
    input(f"                    {color2}[Tokens]{color1} Removed {color2}{dupsRemoved}{color1} Duplicates")
    dazutils.logIt("Quit extracter")
    main()

def getLetoaToken(authURL):
    #CREDIT TO LanLan#0001 FOR THE /api/v1/auth/exchange PART
    
    payload = {
        "app": True,
        "code": authURL.split("?code=")[1].split("&state")[0],
    }

    headers3 = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "cookie": f"cf_clearance={config['cf_clearance']}",
        "sec-ch-ua": '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "content-type": "application/json",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-site": "same-origin",
        "origin": "https://letoa.me",
        "authorization": "null",
        "referer": authURL,
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    while True:
        try:
            timeout=int(config["timeout"])
            proxy=getDict()
            ans = httpx.post("https://letoa.me/api/v1/auth/exchange",proxies=proxy, timeout=timeout,headers=headers3,json=payload,cookies={})
            break
        except:
            continue

    if ans.status_code == 200:
        return ans.json()["token"]
    else:
        return "Failed"

def bypassDoubleCounter():
    global DBverified
    DBverified = 0
    dazutils.onlyText()
    guild_id = str(input(f"                    {color2}[Guild]{color1} > "))
    channel_id = str(input(f"                    {color2}[Channel]{color1} > "))
    message_id = str(input(f"                    {color2}[Message ID]{color1} > "))
    lines = open("lib/tokens.txt","r+").read().splitlines()
    input(f"                    {color2}[Tokens]{color1} Loaded {color2}{str(len(lines))}{color1} Tokens {color2}(Press enter to continue)")
    dazutils.logIt(f"Imported {str(len(lines))} Tokens")

    dazutils.onlyText()
    time.sleep(0.5)

    bot_id = "703886990948565003"
    button_name = "verification_button"

    for token in lines:
        start_time = time.time()
        DBverify(token, guild_id, channel_id, message_id, bot_id, button_name, start_time)
        time.sleep(1)

    input(f"\n                    {color2}[Done]{color1} {DBverified}{color2}/{color1}{str(len(lines))} {color2}Verified{color1}")
    dazutils.logIt(f"{DBverified}/{str(len(lines))} Verified")
    dazutils.logIt("Exited Double counter bypass")
    main()

def DBverify(token, guild_id, channel_id, message_id, bot_id, button_name, start_time):
    global DBverified

    pressButton(token, guild_id, channel_id, message_id, bot_id, button_name, start_time)
    time.sleep(2)

    try:
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "authorization": token,
            "referer": "https://discord.com/channels/@me",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzg3MzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        dns = httpx.get("https://discord.com/api/v9/users/@me/channels",headers=headers,timeout=15)

        for dn in dns.json():
            if str(dn["recipients"][0]["id"]) == bot_id:
                getMSG = httpx.get(f"https://discord.com/api/v9/channels/{dn['id']}/messages?limit=1",headers=headers,timeout=15)
                for message in getMSG.json():
                    for embed in message["embeds"]:
                        for field in embed["fields"]:
                            if "Click me to verify!" in field["value"]:
                                url = field["value"].split("verify!](")[1].split(")")[0]

                                headers = {
                                    "Referer": "https://verify.dcounter.space/",
                                    "sec-ch-ua": '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-ch-ua-platform": '"Windows"',
                                    "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,100)}.0.{random.randint(1000,5000)}.134 Safari/537.36 OPR/89.0.4447.83"
                                }

                                r = httpx.Client(proxies=getDict()).get(url,headers=headers,timeout=50)
                                
                                short_tok = token.split(".")[0]
                                if r.status_code == 200:
                                    time_elapsed = round(time.time() - start_time,3)
                                    logPrint(f"                    {color2}[Verified]{color1} {short_tok} in {color2}{time_elapsed}{color1}s ","\n")
                                    dazutils.logIt(f"{token} Successfully bypassed Double counter in {time_elapsed}s")
                                    DBverified += 1
                                else:
                                    logPrint(f"                    {color3}[Failed]{color1} An unknown error occured {Fore.LIGHTBLACK_EX}({str(r.json())})","\n")
                                    dazutils.logIt(str(r.json()))
    except Exception as e:
        logPrint(f"                    {color3}[Failed]{color1} An unknown error occured {Fore.LIGHTBLACK_EX}({str(e)})","\n")
        dazutils.logIt(str(e))

def bypassLetoaMain():
    global letoaVerified
    letoaVerified = 0
    dazutils.onlyText()
    guild_id = str(input(f"                    {color2}[Guild ID]{color1} > "))
    lines = open("lib/tokens.txt","r+").read().splitlines()
    input(f"                    {color2}[Tokens]{color1} Loaded {color2}{str(len(lines))}{color1} Tokens {color2}(Press enter to continue)")
    dazutils.logIt(f"Imported {str(len(lines))} Tokens")

    dazutils.onlyText()
    time.sleep(0.5)
    threads = []

    for token in lines:
        start_time = time.time()
        t = threading.Thread(target=LetoaVerifyToken,args=[guild_id,token,start_time])
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

    input(f"\n                    {color2}[Done]{color1} {letoaVerified}{color2}/{color1}{str(len(lines))} {color2}Verified{color1}")
    dazutils.logIt(f"{letoaVerified}/{str(len(lines))} Verified")
    dazutils.logIt("Exited Letoa bypass")
    main()

def LetoaVerifyToken(guild_id,token,start_time):
    global letoaVerified
    try:
        short_tok = token.split(".")[0]
        
        payload = {
            "permissions": "0",
            "authorize": True
        }

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": str(len(json.dumps(payload))),
            "authorization": token,
            "referer": "https://discord.com/channels/@me",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzg3MzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r1 = httpx.post(f"https://discord.com/api/v9/oauth2/authorize?client_id=720720709927698433&response_type=code&redirect_uri=https%3A%2F%2Fletoa.me%2Fverification&scope=identify%20guilds%20guilds.join&state={guild_id}",proxies=proxy, timeout=timeout, json=payload, headers=headers, cookies=dazutils.request_cookie(proxy,timeout))
                if r1.status_code == 403:
                    logPrint(f"                    {color3}[Failed]{color1} Blocked by cloudflare {Fore.LIGHTBLACK_EX}({short_tok})","\n")
                break
            except Exception as e:
                dazutils.logIt(str(e))
                continue

        letoa_token = str(getLetoaToken(r1.json()["location"]))

        headers2 = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "authorization": letoa_token,
                "content-length": "2",
                "content-type": "application/json",
                "cookie": f"cf_clearance={config['cf_clearance']}",
                "origin": "https://letoa.me",
                "referer": r1.json()["location"],
                "sec-ch-ua": '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
            }

        while True:
            try:
                timeout=int(config["timeout"])
                proxy=getDict()
                r = httpx.post(f"https://letoa.me/api/v1/verification/{guild_id}",proxies=proxy, headers=headers2,cookies={},json={}, timeout=30)
                break
            except Exception as e:
                dazutils.logIt(str(e))
                continue

        end_time = time.time()
        time_elapsed = round(end_time - start_time,3)

        if r.status_code == 200:
            logPrint(f"                    {color2}[Verified]{color1} {short_tok} in {color2}{time_elapsed}{color1}s ","\n")
            letoaVerified+=1
        elif r.status_code == 403:
            logPrint(f"                    {color3}[Failed]{color1} Blocked by cloudflare {Fore.LIGHTBLACK_EX}({short_tok})","\n")
        else:
            logPrint(f"                    {color3}[Failed]{color1} Unknown error {Fore.LIGHTBLACK_EX}({r.status_code})","\n")
            dazutils.logIt(r.text)
    except Exception as e:
        logPrint(f"                    {color3}[Failed]{color1} An unknown error occured {Fore.LIGHTBLACK_EX}({str(e)})","\n")

def bypassMenu():
    dazutils.onlyText()
    dazutils.setTitle(f"{emp}            Dazeer            ")

    with open("lib/tokens.txt","r") as e: loadedTokens = len(e.read().splitlines())

    try:
        expires = 3
    except:
        logPrint("                    [Error] Not able to load expired date","\n")
        expires = "Unknown"

    logPrint(f"""                               
                  {color3}M{color1}ode {color2}[{version}]{color1} │ {color3}T{color1}okens Loaded : {color2}{loadedTokens}{color1} │ {color3}Ex{color1}pires : {color2}{expires}
                  {color2}╭────────────────────────────────────────────────────────────────╮
                  │  [1]{color1} Letoa           {color2}[2]{color1} Buttons           {color2}[3]{color1} Double counter{color2}  │
                  ╰────────────────────────────────────────────────────────────────╯""","\n")
    dazutils.setTitle(f"{emp}            Dazeer            ")
    option = str(input(f"                      {color2}[Choose]{color1} > "))
    if option == "1":
        bypassLetoaMain()

    elif option == "2":
        buttons()

    elif option == "3":
        bypassDoubleCounter()

def main():
    global hottit, ended
    dazutils.logIt("Running the main screen")
    try:
        with open("lib/tokens.txt","r") as e: loadedTokens = len(e.read().splitlines())
    except:
        logPrint(f"                    {color3}[Error]{color1} Not able to load tokens","\n")
        time.sleep(15)
    dazutils.onlyText()

    try:
        expires = 3

    except:
        expires = "NULL"
        
    logPrint(f"""                               
              {color3}M{color1}ode {color2}[{version}]{color1} │ {color3}T{color1}okens Loaded : {color2}{loadedTokens}{color1} │ {color3}Ex{color1}pires : {color2}{expires}
              {color2}╭────────────────────────────────────────────────────────────────╮
              │ [01]{color1} Joiner            {color2}[06]{color1} VC Joiner            {color2}[11]{color1} Extract  {color2}│
              │ [02]{color1} Leaver            {color2}[07]{color1} VC Leaver            {color2}[12]{color1} Checker  {color2}│
              │ [03]{color1} Flooder           {color2}[08]{color1} Reactor              {color2}[13]{color1} Login    {color2}│
              │ [04]{color1} Accept rules      {color2}[09]{color1} DM Flooder           {color2}[14]{color1} Friender {color2}│
              │ [05]{color1} Onliner           {color2}[10]{color1} Nicker               {color2}[15]{color1} Bypass   {color2}│
              ╰────────────────────────────────────────────────────────────────╯""","\n")
    dazutils.setTitle(f"{emp}            Dazeer            ")
    option = str(input(f"                      {color2}[Choose]{color1} > "))
    try:
        if option == str(0):
            webbrowser.open("https://www.youtube.com/watch?v=PDJLvF1dUek")
        if option == str(1):
            joiner()
        elif option == str(2):
            leaver()
        elif option == str(3):
            flooderShit()
        elif option == str(4):
            acceptRules()
        elif option == str(5):
            onliner()
        elif option == str(6):
            vcjoiner()
        elif option == str(7):
            vcLeaver()
        elif option == str(8):
            reactor()
        elif option == str(9):
            dmflooda()
        elif option == str(10):
            nicker()
        elif option == str(11):
            extract()
        elif option == str(12):
            checker()
        elif option == str(13):
            loginToToken()
        elif option == str(14):
            friender()
        elif option == str(15):
            bypassMenu()
            #sys.exit()
        else:
            main()
    except Exception as e:
        dazutils.logIt(f"Error in main, running {option}\n{e}")

dazutils.removeDups("lib/tokens.txt")
dazutils.setTitle(f"{emp}            Dazeer            ")
try:
    main()
except Exception as e:
    logPrint(e,"\n")
    input()
    
