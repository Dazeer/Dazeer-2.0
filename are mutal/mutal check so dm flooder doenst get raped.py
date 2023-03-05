import httpx


headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "NjY1NTQyMzgwOTA4NDQ1NzA2.YcS3HA.LnGXBv6c0DmsK6iuRvGyLMAvRWs",
    "content-type": "application/json",
    "cookie": "__dcfduid=3e4554d010cb11ed9edc3d3a01dbe8a7; __sdcfduid=3e4554d110cb11ed9edc3d3a01dbe8a79d542cb236d2419f9b8d1452db89c758cbe38dc867880750b8f38175fd7aedbd; __cfruid=510faadda754705afa9eb696e1d8fdbc5c8012ad-1659274216; _ga=GA1.2.1518444816.1659284612; __stripe_mid=0c95d42e-15a9-40ed-b1f3-192ab0940fd3179f38; _gid=GA1.2.1372090103.1660072103; OptanonConsent=isIABGlobal=false&datestamp=Wed+Aug+10+2022+18%3A56%3A49+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=de",
    "origin": "https://discord.com",
    "referer": f"https://discord.com/channels/@me/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDA3OTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
}

r = httpx.get("https://discord.com/api/v9/users/1005574566938157157/profile",headers=headers)
print(r.text)
print(r.status_code)

#400 = invalid user id

#404 unkown person

#403 no mutals with them

#200 = got mutals