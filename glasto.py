import time
from worker import worker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading

if __name__ == '__main__':
    WORKER_COUNT = 1
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.1 (X11; Linux x86_64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/60.0.3112.51 Safari/537.37")
    #opts.add_argument("headless")
    #opts.add_argument("user-data-dir=C:\\Users\\Byrne\\AppData\\Local\\Google\\Chrome\\User Data\\Default");

    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "none"

    proxys = [
    #"46.5.252.70:8080",
    #"170.0.112.234:58586",
    #"190.131.249.214:36127",
    "localhost",
    "localhost",
    "localhost",
    "localhost"
    ]


    jobs = []

    for i in range(0, WORKER_COUNT):
        p = threading.Thread(target=worker, args=(opts, proxys[i], caps))
        jobs.append(p)
        p.start()

    while True:
        time.sleep(100)
