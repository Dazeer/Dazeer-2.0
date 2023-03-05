import discum,sys,os
from colorama import Fore
from time import sleep

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")
    
print(f'''{Fore.RED}
 ░█▀▄░▀█▀░█▀▀░█▀▀░█▀█░█▀▄░█▀▄
 ░█░█░░█░░▀▀█░█░░░█░█░█▀▄░█░█
 ░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░
 ░█▀▀░█▀▀░█▀▄░█▀█░█▀█░█▀▀░█▀▄
 ░▀▀█░█░░░█▀▄░█▀█░█▀▀░█▀▀░█▀▄
 ░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░░░▀▀▀░▀░▀ {Fore.RESET}Online IDs Scraper''')

TOKEN = "OTg1NzU0NzI2NjAxNzUyNjM3.GjgNIl.v0Yp0noMBMsdW91FcqK7e7zQ-jq_zPAftUXYVk"
SERVER_ID = 993538516472565890
CHANNEL_ID = 993560110456635402

if (TOKEN == "" or SERVER_ID == "" or CHANNEL_ID == ""):
    print(f"{Fore.RED} Your provided an invalid token, server or channel id!{Fore.RESET}")
    sys.exit()

discord = discum.Client(token=TOKEN, log=False)
discord.gateway.log = False

def close(resp, guild_id):
    if discord.gateway.finishedMemberFetching(guild_id):
        discord.gateway.removeCommand({'function': close, 'params': {'guild_id': guild_id}})
        discord.gateway.close()

def fetch(guild_id, channel_id):
    discord.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=.1)
    discord.gateway.command({'function': close, 'params': {'guild_id': guild_id}})
    discord.gateway.run()
    discord.gateway.resetSession()
    return discord.gateway.session.guild(guild_id).members

members_list = fetch(SERVER_ID, CHANNEL_ID)
id_list = []

for lol in members_list:
    id_list.append(lol)
print(str(len(id_list)))