import time, urllib.parse

time_rn = time.strftime("%a+%b+%d+%Y+", time.localtime())+urllib.parse.quote_plus(time.strftime("%H:%M:%S",time.localtime())+"+GMT+0200")+"+(Central+European+Summer+Time)"

f"isIABGlobal=false&datestamp={time_rn}&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0"