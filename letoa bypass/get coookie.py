import time

import undetected_chromedriver as uc

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

def get_cookie():
    options = uc.ChromeOptions()
    options.add_argument('--user-agent={}'.format(USER_AGENT))
    with uc.Chrome(options=options) as driver:
        driver.get("https://letoa.me")
        sync_cf_retry(driver)
        #  TODO solver the cloudflare hcaptcha
        return driver.get_cookie('cf_clearance')["value"]

    # use cf_clearance, must be same IP and UA


def sync_cf_retry(page, tries=10) -> bool:
    success = False
    counter = 0
    while counter < tries:
        if "Letoa" in page.title:
            success = True
            break
        else:
            time.sleep(10)
    return success

print(get_cookie())