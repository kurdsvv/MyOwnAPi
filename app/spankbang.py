from bs4 import BeautifulSoup
import re
import requests
import json
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Spankbang:
    def __init__(self, url):
        self.url = url
        self.PATTERN_480p = re.compile(r'\'480p\': \[\'(.*?)\'\]')
        self.PATTERN_720p = re.compile(r'\'720p\': \[\'(.*?)\'\]')
        self.PATTERN_1080p = re.compile(r'\'1080p\': \[\'(.*?)\'\]')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-us",
            "Connection": "keep-alive",
            "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
            "device-memory": "8",
            "sec-ch-ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-arch": "x86",
            "viewport-width": "1092",
            "sec-ch-ua-full-version": "114.0.5735.134",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "8.0.0",
            "Host": "spankbang.com",
            "Origin": "https://spankbang.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document"
        }
        self.proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
        self.cookiestr = '''coe=ww; age_pass=1; age_pass=1; ana_vid=ec4c59a2b79ef7afc4bd56b3f93154eaaaed6b21f5eadb5eebf2a4eea7f9f38b; cfc_ok=00|2|ww|www|master|0; cor=Unknown; backend_version=main; preroll_skip=1; cf_chl_2=8ac59c7e389d335; cf_clearance=N1WyC9.MEWGGGdMr6zGTz8hJiwF46.4UbTYwKhLc80U-1687778455-0-250; pg_interstitial_v5=1; ana_sid=ed9de9e2607dd46fef67c1393d6ad38469856e59535675d2c40495afed0ad032; sb_session=eyJfcGVybWFuZW50Ijp0cnVlfQ.ZJl2LQ.ZN0PEtl4zD0Fl_KL-9-yzd9q3B4; __cf_bm=4wZb_0Rwi2_7Sh3C9ZHsYgzs4a8ZVo7SV63hO0kgpMw-1687778862-0-AQ3xTowp7vOI/cc/tv4Hhh27S3Hrj51sFLKlUKWnKnSVB8z77HEeyEOXYyG42hI9x9E4URW2nYAE9taexTKYu+lCmKsgsf5uyU6vfTPkWFtd
        '''


    def getcookedict(self):
        cookiedict = {}
        for cookies in self.cookiestr.strip().split(";"):
            if len(cookies) != 0:
                cookiestr = cookies.split("=")
                cookiedict[cookiestr[0]] = cookiestr[1]
        return cookiedict


    def GetVideo(self):
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        # chrome_options.add_argument("disable-javascript")
        # chrome_options.add_argument("–incognito")
        # chrome_options.add_argument('--ignore-certificate-errors')  # 主要是该条
        # chrome_options.add_argument('--ignore-ssl-errors')
        # chrome_options.add_experimental_option("prefs", prefs)
        # driver = webdriver.Chrome(options=chrome_options)
        # driver.minimize_window()
        #
        # driver.get(self.url)
        res = requests.get(self.url, proxies=self.proxies, headers=self.headers, cookies=self.getcookedict())
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            # WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'container')))
            urls = soup.find(id="container").find_all('script', {'type': "text/javascript"})[0].get_text()
            m3u8_1080p = self.PATTERN_1080p.findall(urls)
            m3u8_720p = self.PATTERN_720p.findall(urls)
            m3u8_480p = self.PATTERN_480p.findall(urls)
        except TypeError:
            pass
        if len(m3u8_1080p) != 0:
            # driver.close()
            return m3u8_1080p[0]
        elif ((len(m3u8_1080p) == 0) & (len(m3u8_720p) != 0)):
            # driver.close()
            return m3u8_720p[0]
        else:
            # driver.close()
            return m3u8_480p[0]


if __name__ == '__main__':
    Spankbang = Spankbang("https://spankbang.com/642qi/video/hot+korean+girl+play+squirt+game+with+friends")
    print(Spankbang.GetVideo())
