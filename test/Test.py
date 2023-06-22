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

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
chrome_options.add_argument("disable-javascript")
chrome_options.add_argument("–incognito")
chrome_options.add_argument('--ignore-certificate-errors')  # 主要是该条
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# 利用stealth.min.js隐藏浏览器指纹特征
# stealth.min.js下载地址：https://github.com/berstend/puppeteer-extra/tree/stealth-js
with open('stealth.min.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": f.read()
    })

driver.get("https://spankbang.com/35wte/video/korean+beautiful+hd+spurting")
print(driver.page_source)

