import requests
import time
import random
import datetime
import logging

urls = [
    "http://192.168.71.135",
    "http://192.168.71.135/login",
    "http://192.168.71.135/about",
    "http://192.168.71.135/contact",
    "http://192.168.71.135/help",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
]

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)'
]

while True:
    url = random.choice(urls)
    headers = {'User-Agent': random.choice(user_agents)}

    try:
        if "login" in url:
            r = requests.post(url, data={"username": "test", "password": "123"}, headers=headers)
        else:
            r = requests.get(url, headers=headers, timeout=3)
        print(f"[{datetime.datetime.now()}] ✓ 訪問 {url}，狀態碼：{r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.datetime.now()}] x 無法連線到 {url}，錯誤：{e}")

    time.sleep(random.uniform(5, 10))
