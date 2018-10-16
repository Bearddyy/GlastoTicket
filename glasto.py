import time
from worker import worker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import multiprocessing




if __name__ == '__main__':
    WORKER_COUNT = multiprocessing.cpu_count()
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.1 (X11; Linux x86_64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/60.0.3112.51 Safari/537.37")
    #opts.add_argument("headless")
    #opts.add_argument("user-data-dir=C:\\Users\\Byrne\\AppData\\Local\\Google\\Chrome\\User Data\\Default");

    proxys = [
    "46.5.252.70:8080",
    "170.0.112.234:58586",
    "190.131.249.214:36127",
    "localhost"
    ]


    jobs = []
    return_que = multiprocessing.Queue()

    #Test code
    driver = webdriver.Firefox(firefox_options=opts)
    driver.get("www.google.com")

    for i in range(0, WORKER_COUNT):
        p = multiprocessing.Process(target=worker, args=(opts, return_que, proxys[i]))
        jobs.append(p)
        p.start()

    notDone = True
    while notDone:
        try:
            cookie = return_que.get()
            print(cookie)
            cookie = cookie[0]
            notDone = False
        except:
            continue

    print("Got cookie")
    print(cookie)

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.1 (X11; Linux x86_64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/60.0.3112.51 Safari/537.37")

    driver = webdriver.Firefox(path, firefox_options=opts)
    driver.get("http://www.google.com")
    driver.add_cookie(cookie)
    #Get the raw page first to check if it changes
    base_page_html = driver.get('https://glastonbury.seetickets.com/content/extras');
