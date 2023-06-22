from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup
import re
from get.GetSelenium import GetSelenium


class Vjav:
    def __init__(self, URL):
        self.URL = URL

    def GetVideo(self):
        driver = GetSelenium().GetDriver()
        driver.get(self.URL)
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CLASS_NAME, "videoplayer")))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        element = soup.find("video", {"class": "jw-video jw-reset"})["src"]
        m3u8 = "https://vjav.com" + element
        return m3u8


if __name__ == '__main__':
    Vjav = Vjav("https://vjav.com/videos/192984/korean-beautiful-hd-spurting-part2/")
    print(Vjav.GetVideo())
