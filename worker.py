import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def worker(path, opts, return_que, PROXY):
    print("Creating Driver")
    opts.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(path, chrome_options=opts)

    while True:
        try:
            current_site = driver.get('https://glastonbury.seetickets.com/content/extras')
            if "buy" in current_site:
                break
        except e:
            print(e)
            continue

    print("Page Loaded")
    while True:
        do = None

    cookies = driver.get_cookies()
    return_que.put(cookies)
    print("done")
