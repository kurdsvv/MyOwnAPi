from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import re


class Vjav:
    def __init__(self, URL):
        self.URL = URL

    def GetVideo(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        chrome_options.add_argument("disable-javascript")
        chrome_options.add_argument("–incognito")
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)
        driver.minimize_window()


        driver.get(str(self.URL))
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "videoplayer")))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        element = soup.find("video", {"class": "jw-video jw-reset"})["src"]
        m3u8 = "https://vjav.com" + element
        driver.close()
        return m3u8


if __name__ == '__main__':
    Vjav = Vjav("https://vjav.com/videos/192984/korean-beautiful-hd-spurting-part2/")
    print(Vjav.GetVideo())
