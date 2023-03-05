import httpx, requests, random, time, os
from colorama import Fore

os.system("cls")

def getDict():
    proxy = random.choice(open("proxies.txt","r+").read().splitlines())
    return {'http://': f'http://{proxy}','https://': f'http://{proxy}'}

for token in open("tokens.txt","r+").read().splitlines():
    start_time = time.time()
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
            if str(dn["recipients"][0]["id"]) == "703886990948565003":
                getMSG = httpx.get(f"https://discord.com/api/v9/channels/{dn['id']}/messages?limit=2",headers=headers,timeout=15)
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
                                    "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.{random.randint(1000,5000)}.134 Safari/537.36 OPR/89.0.4447.83"
                                }

                                r = httpx.Client(proxies=getDict()).get(url,headers=headers,timeout=50)
                                if r.status_code == 200:
                                    time_elapsed = round(time.time() - start_time,3)
                                    print(f"{Fore.GREEN}BYPASSED Double counter in {time_elapsed} SEC USIN {token}")
                                else:
                                    print(f"{Fore.RED}FAILED SOMEHOW XD {r.status_code}")
    except Exception as e:
        print(str(e))