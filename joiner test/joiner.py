import httpx, time
from capmonster_python import HCaptchaTask

def get_fingerprint():
    response2 = httpx.get("https://discord.com/api/v9/experiments").json()
    return response2["fingerprint"]

def getCookies():
    return dict(httpx.get("https://discord.com").cookies)

def get_headers(token):
    cookie = getCookies()
    headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'cookie': f'__dcfduid={cookie["__dcfduid"]}; __sdcfduid={cookie["__sdcfduid"]}; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-fingerprint': get_fingerprint(),
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
    return headers

def solve(sitekey):
    for i in range(10):
        try:
            cap = HCaptchaTask("bf46c9663ae2b8fb7cf69b2636f08079")
            task = cap.create_task("https://discord.com/channels/@me", sitekey)
            time.sleep(1)
            solution = cap.get_task_result(task)["gRecaptchaResponse"]
            print("solved captcha")
            break
        except TypeError:
            continue
    return solution

def join(invite, headers):
    session = httpx.Client(headers=headers)
    r = session.post(f"https://discord.com/api/v9/invites/{invite}", json={})
    if r.status_code == 200:
        guild_id = r.json()["guild"]["id"]
        join_outcome = True

    if "captcha_sitekey" in r.text:
        sitekey = r.json()['captcha_sitekey']
        solution = solve(sitekey)
    r = session.post(f"https://discord.com/api/v9/invites/{invite}", json={"captcha_key": solution})
    if r.status_code == 200:
        guild_id = r.json()["guild"]["id"]
        join_outcome = True
        
    else:
        print(r.text)
        
    return join_outcome

join("xt7zeCw3", get_headers("MTAzMTE5MjY1MTA0NDc2OTgxMg.Gan0Zu.PoXVr4gQjjwuCJmGlJ3thDV43l4TttXY-SWxFo"))