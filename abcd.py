import httpx, re

def getClientData():
    asset = re.compile(r'([a-zA-z0-9]+)\.js', re.I).findall(httpx.get('https://discord.com/app', headers={'User-Agent': 'Mozilla/5.0'}).text)[-1]
    
    assetFileRequest = httpx.get(f'https://discord.com/assets/{asset}.js', headers={'User-Agent': 'Mozilla/5.0'}).text

    build_info_regex = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+')
    build_info_strings = build_info_regex.findall(assetFileRequest)[0].replace(' ', '').split(',')
    build_num = build_info_strings[0].split(':')[-1]

    return build_num

print(str(getClientData()))