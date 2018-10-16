import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def worker(opts, PROXY):
    print("Creating Driver")
    opts.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Firefox(firefox_options=opts)

    while True:
        try:
            current_site = driver.get('https://glastonbury.seetickets.com/content/extras')
            if "buy" in current_site:
                break
        except:
            continue

    print("Page Loaded")
    while True:
        do = None
    print("done")
