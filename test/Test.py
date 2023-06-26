import requests
from bs4 import BeautifulSoup
import re
import json
# PATTERN_hls = re.compile(r'html5player.setVideoHLS\(\S+\)')
# PATTERN_360 = re.compile(r'hls-360p\S+m3u8')
# proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
# #url_favorite = "https://www.xvideos.com/favorite/98505705/korean"
# headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#            "Accept-Language": "en-us",
#            "Connection": "keep-alive",
#            "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
# def getxvideosm3u8(url):
#     res = requests.get(url, proxies=proxies, headers=headers)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     element = soup.select('#video-player-bg > script:nth-child(6)')
#     tagname = soup.find_all(attrs={"class": "page-title"})[0].text
from selenium import webdriver
import time
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
# chrome_options.add_argument("disable-infobars")
# #chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
# #chrome_options.add_argument("disable-javascript")
# chrome_options.add_argument("–incognito")
# chrome_options.add_argument('--ignore-certificate-errors')  # 主要是该条
# chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_experimental_option("prefs", prefs)
# #chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://spankbang.com/35wte/video/korean+beautiful+hd+spurting")
# time.sleep(20)
# print(driver.get_cookies())
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# import requests
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,ko;q=0.7",
#     "Connection": "keep-alive",
#     "sec-ch-ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-arch": "x86",
#     "viewport-width": "1092",
#     "sec-ch-ua-full-version": "114.0.5735.134",
#     "sec-ch-ua-platform": "Windows",
#     "sec-ch-ua-platform-version": "8.0.0",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-User": "?1",
#     "Sec-Fetch-Dest": "document",
#     "DNT": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "Referer": "https://koreanbj.club/chinese-amateur-cna20234153/",
#     "Host": "koreanbj.club",
# }
#
#
# proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
# cookies='''
# wordpress_logged_in_cc37954828159578f17c0fd06cf005c2=cejixi7862%7C1687955649%7Cglyr6IygbJP7UoUD12dJiMKioeoBxBTudZvOzdxixNj%7C79f0252dc58beb783ad478f142267673ddd6c3d8966f7f0f8b2790bf2278a7cb; wfwaf-authcookie-e64a2b79f43d21efdd0469cb89878f4d=1254%7Csubscriber%7Cread%7Cf46976436a46a9bb2b6a0c0ae46a1c6a53fa08733997cc7b4520d20e48c83bf1
#
#
# '''
# cookiedict = {}
# for cookies in cookies.strip().split(";"):
#     if len(cookies) != 0:
#         cookiestr = cookies.split("=")
#         cookiedict[cookiestr[0].strip()] = cookiestr[1]
# print(cookiedict)
#
# url = "https://koreanbj.club/chinese-amateur-cna20234153/"
#
# res = requests.get(url, proxies=proxies, headers=headers)
# print(res.text)



print(element)