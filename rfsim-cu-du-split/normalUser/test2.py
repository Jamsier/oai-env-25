import requests
import time
import random
import datetime
import socket

# 預設目標資料
urls_get = [
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/",
    "http://192.168.71.135/about",
    "http://192.168.71.135/news",
    "http://192.168.71.135/api/data",
    "https://openai.com/chatgpt/overview/",
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://github.com/",
    "https://about.gitlab.com/",
    "https://www.facebook.com/",
    "https://scholar.google.com/",
    "https://i.ntust.edu.tw/student",
    "https://www.ntust.edu.tw/",
    "https://moodle2.ntust.edu.tw/",
    "https://mail.ntust.edu.tw/cgi-bin/login?index=1"
]

url_post = "http://192.168.71.135/login"
post_data = {
    "username": "test_user",
    "password": "123456"
}

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)'
]

dns_domains = [
    "google.com", "openai.com", "ntust.edu.tw", "wikipedia.org"
]

img_url = "https://picsum.photos/200"

# 定義任務
def task_http_get():
    url = random.choice(urls_get)
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"[GET] {url} | 狀態碼：{r.status_code}")
    except Exception as e:
        print(f"[x] GET 請求失敗：{e}")

def task_http_post():
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        r = requests.post(url_post, data=post_data, headers=headers, timeout=5)
        print(f"[POST] {url_post} | 狀態碼：{r.status_code}")
    except Exception as e:
        print(f"[x] POST 請求失敗：{e}")

def task_dns_query():
    domain = random.choice(dns_domains)
    try:
        ip = socket.gethostbyname(domain)
        print(f"[DNS] 查詢 {domain} → {ip}")
    except socket.gaierror as e:
        print(f"[x] DNS 查詢失敗：{e}")

def task_download_image():
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        r = requests.get(img_url, headers=headers, timeout=5)
        print(f"[IMG] 成功下載圖片 ({len(r.content)} bytes)")
    except Exception as e:
        print(f"[x] 圖片下載失敗：{e}")

# 任務清單
tasks = [task_http_get, task_http_get, task_http_get, task_http_get, task_http_post, task_dns_query, task_download_image]

# 主執行迴圈
while True:
    print(f"[{datetime.datetime.now()}] 執行一次隨機任務", end=" | ")
    
    task = random.choice(tasks)
    task()

    delay = random.uniform(10, 30)
    time.sleep(delay)
