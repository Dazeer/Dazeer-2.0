#!/usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import list2cmdline
import dazutils
dazutils.resizeWindow(95, 25)
dazutils.setTitle(f"Dazeer - Loading...")
dazutils.initializeDazeer()

from ast import arg
from cmath import log
from email import message
from colorama import Fore
from tasksio import TaskPool
from msvcrt import getch
from selenium import webdriver
from capmonster_python import HCaptchaTask
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from websocket import WebSocket
from json import dumps
from pypresence import Presence
import pystyle, dazeerExceptions
from datetime import datetime
import threading, time, os, random, requests, sys, hashlib, keyboard, discum, websocket, base64, urllib.parse, webbrowser, json, urllib, os, uuid, colorama, logs, asyncio
from keyauth import api
colorama.init()
os.system('cls')

__lock__ = threading.Lock()

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path): path = path[:-2] + "exe"
	md5_hash = hashlib.md5(); a_file = open(path,"rb"); content = a_file.read(); md5_hash.update(content); digest = md5_hash.hexdigest(); return digest

auth = api(
    name = "dazeer BETA",
    ownerid = "Qh04HRgKe2",
    secret = "dae68397da9beefc63df87011c02d5ecf315b7bfb56a1fa95a387cf15f4163c6",
    version = "1.0",
    hash_to_check = getchecksum()
)



class Printing:
    def __init__(self):
        self.color1, self.color2, self.color3 = dazutils.getColors()
    def mainMenu(self):
        expires = datetime.utcfromtimestamp(int(auth.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S')
        dazutils.onlyText()
        dazutils.setTitle(f"Dazeer - {mainClass.get_version()}")
        print(f"""                               
                {self.color3}M{self.color1}ode {self.color2}[v3]{self.color1} │ {self.color3}T{self.color1}okens Loaded : {self.color2}{len(mainClass.get_tokens())}{self.color1} │ {self.color3}Ex{self.color1}pires : {self.color2}{expires}
              {self.color2}╔════════════════════════════════════════════════════════════════╗
              ║ [01]{self.color1} Joiner            {self.color2}[06]{self.color1} VC Joiner            {self.color2}[11]{self.color1} Extract  {self.color2}║
              ║ [02]{self.color1} Leaver            {self.color2}[07]{self.color1} VC Leaver            {self.color2}[12]{self.color1} Checker  {self.color2}║
              ║ [03]{self.color1} Flooder           {self.color2}[08]{self.color1} Reactor              {self.color2}[13]{self.color1} Login    {self.color2}║
              ║ [04]{self.color1} Accept rules      {self.color2}[09]{self.color1} DM Flooder           {self.color2}[14]{self.color1} Friender {self.color2}║
              ║ [05]{self.color1} Onliner           {self.color2}[10]{self.color1} Nicker               {self.color2}[15]{self.color3} Exit     {self.color2}║
              ╚════════════════════════════════════════════════════════════════╝""")
    def ask(self, n=1, question="uhhh", msg=""):
        return input("\n"*n+" "*20+f"{self.color2}[{question}]{self.color1} > {msg}")

    def centeredMessage(self, message, end="\n"):
        print(pystyle.Center.XCenter(f"         {self.color2}{message}{self.color1}"), end=end)
    
    def getColors(self):
        return self.color1, self.color2, self.color3
        
    def logPrint(self, n=1, message="uhhh", end="\n"):
        __lock__.acquire()
        print("\n"*n+pystyle.Center.XCenter(message), end=end)
        __lock__.release()


class Tokens:
    def __init__(self):
        self.tokens = []
        self.load_tokens()
        
        #Joiner
        self.joiner_join = 0
        self.joiner_failed = 0
        self.joiner_captcha = 0
        self.joiner_invalid = 0
        self.joiner_sent = 0
        
        #Leaver
        self.leaver_left = 0
        self.leaver_failed = 0
        self.leaver_invalid = 0
        self.leaver_ratelimited = 0
        self.leaver_sent = 0
        
        #Flooder
        self.flooder_msgs_sent = 0
        self.flooder_failed = 0
        self.flooder_invalid = 0
        self.flooder_ratelimited = 0
        self.flooder_sent = 0
        
    
    def get_joiner_info(self):
        return (self.joiner_join, self.joiner_failed, self.joiner_captcha, self.joiner_invalid, self.joiner_sent)

    def get_leaver_info(self):
        return (self.leaver_left, self.leaver_failed, self.leaver_invalid, self.leaver_ratelimited, self.leaver_sent)
    
    def get_flooder_info(self):
        return (self.flooder_msgs_sent, self.flooder_failed, self.flooder_invalid, self.flooder_ratelimited, self.flooder_sent)
    
    
    def load_tokens(self):
        with open("lib/tokens.txt", "r") as f: return f.readlines()



    def update_title_joiner(self):
        color1, color2, color3 = dazutils.getColors()
        while not mainClass.isRunning():
            joiner_join, joiner_failed, joiner_captcha, joiner_invalid, joiner_sent = tokenClass.get_joiner_info()
            dazutils.setTitle(f"Dazeer - {mainClass.get_version()} - Joiner - Joined :{joiner_join} | Failed to join : {joiner_failed} | Captchas : {joiner_captcha} | Invalid tokens : {joiner_invalid} | Requests sent : {joiner_sent}")
            logging.logPrint(f"    {color2}[Dazeer]{color1} Joined: {color2}{joiner_join}{color1} │ Failed: {color2}{joiner_failed}{color1} │ Captcha: {color2}{joiner_captcha}{color1} │ Elapsed: {color2}{timeelapsed}{color1} │ Tokens: {color2}{str(len(self.tokens))}{color1} │ Mpm: {color2}{cpm}{color1}         ","\r")

    def update_title_leaver(self):
        color1, color2, color3 = dazutils.getColors()
        while not mainClass.isRunning():
            leaver_left, leaver_failed, leaver_invalid, leaver_sent = tokenClass.get_leaver_info()
            dazutils.setTitle(f"Dazeer - {mainClass.get_version()} - Leaver - Left :{leaver_left} | Failed to leave : {leaver_failed} | Invalid tokens : {leaver_invalid} | Requests sent : {leaver_sent}")

    def update_title_flooder(self):
        color1, color2, color3 = dazutils.getColors()
        while not mainClass.isRunning():
            flooder_msgs_sent, flooder_failed, flooder_invalid, flooder_ratelimited, flooder_sent = tokenClass.get_flooder_info()
            dazutils.setTitle(f"Dazeer - {mainClass.get_version()} - Flooder - Messages sent :{flooder_msgs_sent} | Failed to send : {flooder_failed} | Invalid tokens : {flooder_invalid} | Ratelimited : {flooder_ratelimited} | Requests sent : {flooder_sent}")
            logging.logPrint(f"    {color2}[Dazeer]{color1} Sent: {color2}{flooder_msgs_sent}{color1} │ Failed: {color2}{flooder_failed}{color1} │ Ratelimited: {color2}{flooder_invalid}{color1} │ Elapsed: {color2}{timeelapsed}{color1} │ Tokens: {color2}{str(len(self.tokens))}{color1} │ Mpm: {color2}{cpm}{color1}         ","\r")








    def set_all_to_zero(self):
        #Joiner
        self.joiner_join = 0
        self.joiner_failed = 0
        self.joiner_captcha = 0
        self.joiner_invalid = 0
        self.joiner_sent = 0
        
        #Leaver
        self.leaver_left = 0
        self.leaver_failed = 0
        self.leaver_invalid = 0
        self.leaver_ratelimited = 0
        self.leaver_sent = 0
        
        
        


    def joinServer(self, token, invite, bypassRulesScreen=False): 
        try:
            color1, color2, color3 = dazutils.getColors()
            headers = dazutils.getJoinHeaders(token)
            hidden_token = dazutils.hideToken(token) 
            start_time = time.time()
            with requests.Session() as session:
                self.joiner_sent += 1
                with session.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, cookies=dazutils.request_cookie(), timeout=5) as r:
                    data = r.json()
                    
                    if r.status_code == 200: logging.logPrint(0,f"{color2}[Joined]{color1} {hidden_token} in {color2}{time_elapsed}{color1}s"); dazutils.logIt(f"Joined discord.gg/{invite} using {token} without captcha")
                    elif r.status_code == 403: logging.logPrint(0,f"{color2}[Already] {hidden_token}{color1} is already in the server")
                    elif r.status_code == 400:
                        self.joiner_captcha += 1
                        logging.logPrint(0,f"                    {color3}[Captcha]{color1} Captcha Detected Solving..")
                        sitekey = data['captcha_sitekey']
                        response_captcha = session.post(f"https://discord.com/api/v9/invites/{invite}", json={"captcha_key": dazutils.captcha_bypass(f"https://discord.com", sitekey)}, headers=headers, cookies=dazutils.request_cookie(), timeout=5)
                        if response_captcha.status_code == 200:
                            end_time = time.time()
                            time_elapsed = round(end_time - start_time,3)
                            logging.logPrint(0,f"                    {color2}[Joined]{color1} {hidden_token} in {color2}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}(captcha){color1}")
                            dazutils.logIt(f"Joined discord.gg/{invite} using {token} with captcha")
                            self.joiner_join+=1
                        else:
                            end_time = time.time()
                            time_elapsed = round(end_time - start_time,3)
                            error_msg = response_captcha.json()
                            dazutils.logIt(f"Failed to join because {error_msg}")
                            logging.logPrint(0,f"                    {color3}[Failed]{color1} {hidden_token} in {color3}{time_elapsed}{color1}s {Fore.LIGHTBLACK_EX}({error_msg}){color1}")
                            self.joiner_failed +=1
                    elif r.status_code == 429:
                        logging.logPrint(0,f"{hidden_token} is rate limited!")    
                        
                    if "message" not in data:
                        if r.status_code == 200:
                            self.joiner_join += 1
                            if bypassRulesScreen == True:
                                with session.get("https://discord.com/api/v9/guilds/" + data['guild'][ 'id'] + "/member-verification?with_guild=false&invite_code=" + invite) as req2:
                                    if req2.status_code == 200:
                                        j = req2.json()
                                        with session.put("https://discord.com/api/v9/guilds/" + data['guild'][ 'id'] + "/requests/@me", json=j) as req3:
                                            if req3.status_code == 201 or 200 or 204:
                                                logs.success(f"{hidden_token} bypassed membership screening!")
                                            else:
                                                logging.logPrint(0,f"{hidden_token} failed to bypass membership screening!")
                                    else:
                                        logging.logPrint(0,f"{hidden_token} failed to bypass membership screening!")
                    
                    elif 'Unauthorized' in data['message']:
                        self.joiner_invalid += 1
                        logging.logPrint(0,f"{hidden_token} is NOT a real token, removing from list!")
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif 'Unknown Invite' in data['message']:
                        logging.logPrint(0,f"{hidden_token} is an invalid invite!")
                        raise dazeerExceptions.InvalidInvite("Invalid Invite")
                    elif "banned" in json['message']:
                        logging.logPrint(0,f"{hidden_token} is banned!")
        except Exception as e:
            print(e)
            
    def leaveServer(self, token, guild_id):
        color1, color2, color3 = dazutils.getColors()
        while True:
            while True:
                try:
                    r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers = dazutils.getHeaders(token), proxies=dazutils.getDict(), timeout=int(dazutils.getConfig()["timeout"]))
                    break
                except:
                    continue
            short_tok = token.strip().split(".")[0]
            if r.status_code == 204:
                dazutils.logPrint(f"                    {color2}[Left]{color1} {short_tok}","\n")
                self.leaver_left+=1
                break

            elif r.status_code == 429:
                dazutils.logPrint(float(r.json()["retry_after"]),"\n")
                self.leaver_ratelimited+=1
                continue
                
            elif r.status_code == 404:
                dazutils.logPrint(f"                    {color3}[Failed]{color1} {short_tok}","\n")
                dazutils.logIt(f"Failed to leave on {token.strip()} because {r.text}")
                self.leaver_failed+=1
                break
            
    def sendMessage(self, token, channelid, msg, replyMsg = None):
        headers = dazutils.getHeaders(token)
        tk = token
        try: tk = token[:25] + "*" * 34
        except: tk = "*" * len(token)
        j = {"content": msg}
        if replyMsg != None:
            j['message_reference'] = {
                "channel_id": channelid,
                "message_id": replyMsg
            }
        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies) - 1)]
        with requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages",json=j, proxies=randomProxy, headers=headers) as req:
            if req.status == 429:
                logging.logPrint(0,f"{tk} is ratelimited!")
            elif req.status == 200:
                logging.logPrint(0,f"{tk} sent message!")
            else:
                json = req.json()
                if 'message' in json:
                    if 'verify' in json['message']:
                        logging.logPrint(0,f"{tk} is not verified and removed!")
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif 'Unauthorized' in json['message']:
                        logging.logPrint(0,f"{tk} is NOT a real token, removing from list!")
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif 'Missing Access' in json['message']:
                        logging.logPrint(0,f"{tk} does not have access to the channel!")
                    else:
                        logging.logPrint(0,f"{tk} Failed to send the message!")        
    
    
    def channeFlooder(self, token, channel_ids, message):
        random_channel = random.choice(channel_ids)
        
            

            
                
                
            
            
            
    def serverJoiner(self, tokens, invite, bypassRulesScreen=False, delay=2):
        try:
            threading.Thread(target=self.update_title_joiner).start()
            for token in tokens:
                threading.Thread(target=self.joinServer, args=(token, invite, bypassRulesScreen)).start()
                time.sleep(delay)
                    
        except dazeerExceptions.InvalidInvite:
            time.sleep(3)
            mainClass.start()
            
    
    def serverLeaver(self, tokens, guild_id):
        try:
            threading.Thread(target=self.update_title_leaver).start()
            for token in tokens:
                threading.Thread(target=self.leaveServer, args=(token, guild_id,)).start()
                    
        except dazeerExceptions.InvalidInvite:
            time.sleep(3)
            mainClass.start()
    
    def serverFlooder(self, tokens, channel_ids, message, delay=2):
        try:
            threading.Thread(target=self.update_title_leaver).start()
            for token in tokens:
                threading.Thread(target=self.channelFlooder, args=(token, channel_ids, message,)).start()
                time.sleep(delay)
                    
        except dazeerExceptions.InvalidInvite:
            time.sleep(3)
            mainClass.start()

    


class Main:
    def __init__(self):
        # Setting up the variables
        self.settings = dazutils.getConfig()
        self.running = False
        with open("lib/tokens.txt", "r") as f: 
            self.tokens = f.read().splitlines() 
        
        #Checker
        self.checker_valid = 0
        self.checker_invalid = 0
        self.checker_locked = 0
        self.checker_checked = 0
        self.checker_lines  = 0
        

        
        
        self.version = "3.0.0"
        
    def get_tokens(self):
        return self.tokens
    def get_version(self):
        return self.version
    def isRunning(self):
        return self.running
    
    def start(self):
        self.expires = datetime.utcfromtimestamp(int(auth.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S')
        dazutils.resizeWindow(95, 25)
        logging.mainMenu()
        
        tokenClass.set_all_to_zero()
        
        def askChoice(self):
            choice = logging.ask(0,f"Choose","")
            if choice.__eq__('1'):
                self.screen1()
            elif choice.__eq__('2'):
                self.screen2()
            elif choice.__eq__('3'):
                self.screen3()
            elif choice.__eq__('4'):
                self.screen4()
            elif choice.__eq__('5'):
                self.screen5()
            elif choice.__eq__('6'):
                self.screen6()
            elif choice.__eq__('7'):
                self.screen7()
            elif choice.__eq__('8'):
                self.screen8()
            elif choice.__eq__('9'):
                self.screen9()
            elif choice.__eq__('10'):
                self.screen10()
            elif choice.__eq__('11'):
                self.screen11()
            elif choice.__eq__('12'):
                self.screen12()
            elif choice.__eq__('13'):
                self.screen13()
            elif choice.__eq__('14'):
                self.screen14()
            elif choice.__eq__('15'):
                logs.print(f"{self.color1}[{self.color2}Dazeer{self.color1}]{self.color2} > {self.color3}Exiting...")
                sys.exit()
            else:
                askChoice(self=None)

        askChoice(self)
    
    
    def screen1(self):
        self.running = True
        dazutils.onlyText()
        logging.centeredMessage("Server Joiner")
        invite = logging.ask(1, "Invite","discord.gg/")
        delay = logging.ask(0, "Delay","")
        bypassRuleScreen = logging.ask(0, "Accept Rules","(y/n) ")
        if bypassRuleScreen.__eq__("y"): sex = True
        elif bypassRuleScreen.__eq__("n"): sex = False
        else: self.start()
        
        if invite == "": self.start()
        
        tokenClass.serverJoiner(tokens=self.tokens, invite=invite, bypassRulesScreen=sex, delay=int(delay))
        self.running = False
        self.start()
        
        
        
    def screen2(self):
        self.running = True
        dazutils.onlyText()
        logging.centeredMessage("Server Leaver")
        guild_id = logging.ask(question="Guild ID")
        delay = logging.ask(question="Delay")
        
        if guild_id == "": self.start()
        
        tokenClass.serverLeaver(tokens=self.tokens, guild_id=guild_id, delay=int(delay))
        self.running = False
        self.start()
    def screen3(self):
        self.running = True
        dazutils.onlyText()
        logging.centeredMessage("Channel Flooder")
        



class Auth:
    def askForKey(self):
        dazutils.onlyText()
        lic = logging.ask(question="License Key")
        with open("lib/config.json", "r") as f:
            data = json.load(f)
            data["license"] = lic
            with open("lib/config.json", "w") as f:
                json.dump(data, f, indent=4)
        self.start()
    
    def start(self):
        dazutils.setTitle("Dazeer - Authenticating")
        color1, color2, color3 = dazutils.getColors()
        dazutils.onlyText()
        logging.logPrint(0,f"{color3}[Auth] {color1}Working")
        config = dazutils.getConfig()
        lic = dazutils.getConfig()["license"]
        if lic == "":
            self.askForKey()
        else:
            authRequest = auth.license(lic)
            if authRequest["success"]:
                try:
                    data = {"content": "","embeds": [{"title": "Someone just logged in!","description": f"**License** : ```{lic}``` **Hwid** : ```{auth.user_data.hwid}``` **Dazeer Beta Version** : ```{mainClass.get_version()}```","color": 9450676,"thumbnail": {"url": "https://cdn.discordapp.com/attachments/986676412176031844/986988700581908490/dazeer2-0.png"}}],"username": "Dazeer Auth","avatar_url": "https://cdn.discordapp.com/attachments/986676412176031844/986988700581908490/dazeer2-0.png","attachments": []}
                    webhook = "https://discord.com/api/webhooks/987113886522150982/3Gj-Ycg8bUkyK9FnmA8o3mDAyZ5uYdjz_EH93OZDNsg7yAqivRKPJ8vzpTaZi_KWtJyG"
                    requests.post(webhook,json=data)
                except:
                    pass
                logging.logPrint(0, f"{color3}[Auth] {color1}Success!")
                time.sleep(2)
                mainClass.start()
            else:
                if "not found" in authRequest['message']:
                    self.askForKey()
                else:
                    color1, color2, color3 = dazutils.getColors()
                    logging.logPrint(0,f"      {color3}Failed!\nReason: {color2}{authRequest['message']}")
                    time.sleep(2)
                    self.askForKey()
    
logging = Printing()
mainClass = Main()
tokenClass = Tokens()
    
try:
    sex = Auth()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sex.start())
except Exception as e:
    print(e)
    input()