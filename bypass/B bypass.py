from urllib import request
import requests, time, string, random, os, threading, asyncio
from datetime import datetime
from decimal import Decimal, getcontext
from colorama import Fore
from discord.ext import commands
import discord

os.system("cls")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

intents = discord.Intents.all()
intents.members = True

kek = commands.Bot(command_prefix=".", case_sensitive=False, self_bot=True, intents=intents)

bot_id = "814014774990995496"
message_id = "968858015275024424"
channel_id = "928715732961869844"
guild_id = "903281957562122290"
custom_id = "verify"

@kek.event
async def on_message(message):
    if (str(message.guild.id) == guild_id and str(message.channel.id)== channel_id):
        print(message.id)
        print(message)
        #print(requests.get(f"https://discord.com/channels/{channel_id}/{message.id}",headers=headers, cookies=request_cookie()).text)
        await kek.close()


def getMSG(token): kek.run(token, bot=False)

for token in open("tokens.txt","r").read().splitlines():

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
            "custom_id": custom_id
        }
    }

    def request_cookie():
        response1 = requests.get("https://discord.com", headers=headers)
        cookie = response1.cookies.get_dict()
        cookie['locale'] = "us"
        return cookie

    threading.Thread(target=getMSG,args=[token]).start()
    time.sleep(4)
    r = requests.post("https://discord.com/api/v9/interactions", headers=headers, json=payload, cookies=request_cookie(), timeout=10)
    if r.ok:
        print(f"{Fore.GREEN}Success with {token}")

    else: print(f"{Fore.RED}Fail with {token} {r.text}"); print(r.text)