from bs4 import BeautifulSoup
import re
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


    def GetVideo(self):
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
        driver = webdriver.Chrome(options=chrome_options)
        driver.minimize_window()

        driver.get(self.url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'container')))
        urls = soup.find(id="container").find_all('script', {'type': "text/javascript"})[0].get_text()
        m3u8_1080p = self.PATTERN_1080p.findall(urls)
        m3u8_720p = self.PATTERN_720p.findall(urls)
        m3u8_480p = self.PATTERN_480p.findall(urls)
        if len(m3u8_1080p) != 0:
            driver.close()
            return m3u8_1080p[0]
        elif ((len(m3u8_1080p) == 0) & (len(m3u8_720p) != 0)):
            driver.close()
            return m3u8_720p[0]
        else:
            driver.close()
            return m3u8_480p[0]


if __name__ == '__main__':
    Spankbang = Spankbang("https://spankbang.com/35wte/video/korean+beautiful+hd+spurting")
    print(Spankbang.GetVideo())
