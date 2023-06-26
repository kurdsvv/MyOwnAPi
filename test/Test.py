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
# }
#
#
# proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
# cookies='''
# '''
# cookiedict = {}
# for cookies in cookies.strip().split(";"):
#     if len(cookies) != 0:
#         cookiestr = cookies.split("=")
#         cookiedict[cookiestr[0].strip()] = cookiestr[1]
# print(cookiedict)
#
# url = "https://www.youjizz.com/videos/korean-beautiful-hd-spurting-part2-39734271.html"
# res = requests.get(url, headers=headers,proxies=proxies)
# print(res.text)
soup = BeautifulSoup(open("index.html",encoding="utf-8"))
element=soup.find("div",{"id":"content"})
PATTERN_data=re.compile(r'dataEncodings = (.*);')
urllist=(PATTERN_data.findall(str(element))[0]).replace("\/","/")
PATTERN_480p=re.compile(r'quality\"\:\"480\"\,\"filename\"\:\"(.*?)\"')
PATTERN_720p=re.compile(r'quality\"\:\"720\"\,\"filename\"\:\"(.*?)\"')
PATTERN_1080p=re.compile(r'quality\"\:\"1080\"\,\"filename\"\:\"(.*?)\"')
result720=PATTERN_720p.findall(urllist)
if len(PATTERN_1080p.findall(urllist))!=0:
    print("https"+PATTERN_1080p[0])
elif ((len(PATTERN_1080p.findall(urllist))==0) & (len(PATTERN_720p.findall(urllist))!=0)):
    print("https"+PATTERN_720p.findall(urllist)[0])
else:
    print("https"+PATTERN_480p[0])