import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def worker(opts, PROXY, caps):
    print("Creating Driver")
    opts.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Firefox(firefox_options=opts, desired_capabilities=caps)

    while True:
        try:
            driver.get('https://glastonbury.seetickets.com/content/extras')
            current_site = driver.page_source
            if "buy" in current_site:
                break
        except:
            continue

    print("Page Loaded")
    while True:
        do = None
    print("done")
