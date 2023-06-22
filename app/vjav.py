from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import re

import time
class Vjav:
    def __init__(self, URL):
        self.URL = URL

    def GetVideo(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        #chrome_options.add_argument("disable-infobars")
        #chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        #chrome_options.add_argument("disable-javascript")
        chrome_options.add_argument("–incognito")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)
        driver.minimize_window()

        driver.get(str(self.URL))
        try:
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            element = soup.find("video", {"class": "jw-video jw-reset"})["src"]
            m3u8 = "https://vjav.com" + element
            return m3u8
        except TypeError:
            pass
        finally:
            driver.close()



if __name__ == '__main__':
    Vjav = Vjav("https://vjav.com/videos/192984/korean-beautiful-hd-spurting-part2")
    print(Vjav.GetVideo())
