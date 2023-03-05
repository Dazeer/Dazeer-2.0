import requests, json, re, os, binascii, random, time, ssl, httpx, cloudscraper, base64, string
import undetected_chromedriver as uc

guildid = "1005221246390259832"#input("guild id: ")
token = "OTg2NzU1MTEzNTU1MjE0NDA3.GRicRQ.zhldOu9OeLhZ6R21DQ2B9bgh7FtLRHkInWo3dA"

def getCookies(): return dict(httpx.get("https://discord.com/channels/@me").cookies)

payload = {
    "authorize": True,
    "permissions": "0"
}

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "authorization": token,
    "content-type": "application/json",
    "cookie": "__dcfduid=ab2a2da01a9911edac9791d1bba92f55; __sdcfduid=ab2a2da11a9911edac9791d1bba92f55897dc0713849cd8811f4d94fc6801c90ecc21d21703e327c231cb37804bf669e; locale=en-US; _ga=GA1.2.1677205843.1660404364; _gid=GA1.2.232159114.1660404364; __cf_bm=LKJypKcnNijLIqkzKjf5PEOVoALy7DZ5d6kF0clYQ_k-1660412205-0-AT2dxOTohgFimM6xit2SSzCVTZYZuC9C/3Ff3tEHPVIr6Jv4hQ6JbQ4zNzBUxaDEDS9Z4RYI1XmW3ou/TswGkoH2FtkMRCKGPRUWffYwGTltb3Bw/BwGHv5v+rfkBfMgPQ==; OptanonConsent=isIABGlobal=false&datestamp=Sat+Aug+13+2022+19%3A36%3A44+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MTQ3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
}

context = ssl.create_default_context()
context.minimum_version.TLSv1_3
time.sleep(0.1)
r1 = httpx.post(f"https://discord.com/api/v9/oauth2/authorize?client_id=720720709927698433&response_type=code&redirect_uri=https%3A%2F%2Fletoa.me%2Fverification&scope=identify%20guilds%20guilds.join&state={guildid}", verify=context, json=payload, headers=headers, cookies=getCookies())

print(r1.text)
print(r1.json()["location"])

def cf_clearance():
    return "O5KxNXFsIWsGrCmq5_JrM4a8SpX6Y1EcsR0f8xXz9zs-1660326712-0-250"

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
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    ans = httpx.post("https://letoa.me/api/v1/auth/exchange",headers=headers3,json=payload,cookies={"cf_clearance":cf_clearance()})

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
        "cookie": "cf_clearance=O5KxNXFsIWsGrCmq5_JrM4a8SpX6Y1EcsR0f8xXz9zs-1660326712-0-250",
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

r = httpx.post(f"https://letoa.me/api/v1/verification/{guildid}",headers=headers2,cookies={"cf_clearance":cf_clearance()},json={}, timeout=20)

print(r.status_code)
if r.status_code == 200:
    print(r.text)