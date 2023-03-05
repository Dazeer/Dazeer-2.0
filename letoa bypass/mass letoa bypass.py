from socket import timeout
import httpx, json, re, os, binascii, random, time, ssl, httpx, cloudscraper, base64, string, ssl
import undetected_chromedriver as uc

a = 0

guildid = input("guild id: ")

context = ssl.create_default_context()
context.minimum_version.TLSv1_3
time.sleep(0.1)

def getCookies(): return dict(httpx.get("https://discord.com/channels/@me", verify=context).cookies)

for token in open("tokens.txt","r+").read().splitlines():
    try:
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzg3MzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        r1 = httpx.post(f"https://discord.com/api/v9/oauth2/authorize?client_id=720720709927698433&response_type=code&redirect_uri=https%3A%2F%2Fletoa.me%2Fverification&scope=identify%20guilds%20guilds.join&state={guildid}", verify=context, json=payload, headers=headers, cookies=getCookies())

        print(r1.status_code)
        print(r1.text)
        print(r1.json()["location"])

        def cf_clearance():
            return "JKucOsS1j7CpPfaPxaSgMdYFXvU3VgX9YA74mzGa.II-1660577707-0-250"

        def getLetoaToken(authURL):
            #CREDIT TO LanLan#0001
            payload = {
                "app": True,
                "code": authURL.split("?code=")[1].split("&state")[0],
            }

            headers3 = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "cookie": f"cf_clearance={cf_clearance()}",
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
                "upgrade-insecure-httpx": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.91"
            }

            ans = httpx.post("https://letoa.me/api/v1/auth/exchange", verify=context,headers=headers3,timeout=100,json=payload,cookies={"cf_clearance":cf_clearance()})

            if ans.status_code == 200:
                return ans.json()["token"]
            else:
                return "Failed"

        letoa_token = str(getLetoaToken(r1.json()["location"]))

        print(letoa_token)

        headers2 = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "authorization": letoa_token,
                "content-length": "2",
                "content-type": "application/json", 
                "cookie": f"cf_clearance={cf_clearance()}",
                "origin": "https://letoa.me",
                "referer": r1.json()["location"],
                "sec-ch-ua": '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.91"
            }

        r = httpx.post(f"https://letoa.me/api/v1/verification/{guildid}", verify=context,timeout=100,headers=headers2,cookies={"cf_clearance":cf_clearance()},json={})

        print(r.status_code)
        if r.status_code == 200:
            print(r.text)
        a+=1
        os.system(f"title done: {a}")
    except Exception as e:
        print(str(e))