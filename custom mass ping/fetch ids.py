import httpx, threading, os

guild_id = input("guild id: ")

headers = {
    "Authorization": "OTkzMDgyMjQwOTIzODY5MjA1.GjCN7j.rbrbrqijYoyrwiWMadcn-MnL2SPz43QWHP3S7M",
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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDA3OTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
}

ids = []

def fetch(channel_id):
    global running
    try:
        r = httpx.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100",headers=headers)

        lastMSGid = r.json()[-1]["id"]

        for thing in r.json():
            if not thing["author"]["id"] in ids: ids.append(thing["author"]["id"])
            os.system(f"title fetched {str(len(ids))}")
    except:
        pass

    while running:
        try:
            r1 = httpx.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?before={lastMSGid}&limit=100",headers=headers)
            for thing in r1.json():
                if not thing["author"]["id"] in ids: ids.append(thing["author"]["id"])
                os.system(f"title fetched {str(len(ids))}")

            lastMSGid = r1.json()[-1]["id"]

        except:
            break

running = True
r = httpx.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels",headers=headers)

for thing in r.json():
    if thing["type"] == 0:
        threading.Thread(target=fetch,args=[thing["id"]]).start()
        
input("press enter to stop")
running = False
input("")