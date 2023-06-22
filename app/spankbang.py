from bs4 import BeautifulSoup
import re
import json
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Spankbang:
    def __init__(self, url):
        self.url = url
        self.PATTERN_480p = re.compile(r'\'480p\': \[\'(.*?)\'\]')
        self.PATTERN_720p = re.compile(r'\'720p\': \[\'(.*?)\'\]')
        self.PATTERN_1080p = re.compile(r'\'1080p\': \[\'(.*?)\'\]')

        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        self.chrome_options.add_argument("disable-javascript")
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.minimize_window()

    def get_video(self):
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.ID, 'container')))
        urls = soup.find(id="container").find_all('script', {'type': "text/javascript"})[0].get_text()
        m3u8_1080p = self.PATTERN_1080p.findall(urls)
        m3u8_720p = self.PATTERN_720p.findall(urls)
        m3u8_480p = self.PATTERN_480p.findall(urls)
        if len(m3u8_1080p) != 0:
            self.driver.close()
            return m3u8_1080p[0]
        elif ((len(m3u8_1080p) == 0) & (len(m3u8_720p) != 0)):
            self.driver.close()
            return m3u8_720p[0]
        else:
            self.driver.close()
            return m3u8_480p[0]


if __name__ == '__main__':
    Spankbang = Spankbang("https://spankbang.com/35wte/video/korean+beautiful+hd+spurting")
    print(Spankbang.get_video())
