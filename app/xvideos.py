import requests
from bs4 import BeautifulSoup
import re

#url_favorite = "https://www.xvideos.com/favorite/98505705/korean"
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-us",
           "Connection": "keep-alive",
           "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
class Xvideos:
    def __init__(self,url):
        self.url = url
        self.session = requests.Session()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-us",
                        "Connection": "keep-alive",
                        "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
        self.proxies= {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
        self.PATTERN_hls= re.compile(r'html5player.setVideoHLS\(\S+\)')
        self.PATTERN_360 = re.compile(r'hls-360p\S+m3u8')
        self.PATTERN_480 = re.compile(r'hls-480p\S+m3u8')
        self.PATTERN_720 = re.compile(r'hls-720p\S+m3u8')
        self.PATTERN_1080 = re.compile(r'hls-1080p\S+m3u8')

    def GetVideo(self):
        res = requests.get(self.url, proxies=self.proxies, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        element = soup.select('#video-player-bg > script:nth-child(6)')
        tagname = soup.find_all(attrs={"class": "page-title"})[0].text
        m3u8url = str(self.PATTERN_hls.findall(str(element))).split("'")[1]
        m3u8url_clarity_1080 = self.PATTERN_1080.findall(requests.get(m3u8url, proxies=self.proxies).text)
        m3u8url_clarity_720 = self.PATTERN_720.findall(requests.get(m3u8url, proxies=self.proxies).text)
        m3u8url_clarity_480 = self.PATTERN_480.findall(requests.get(m3u8url, proxies=self.proxies).text)
        m3u8url_clarity_360 = self.PATTERN_360.findall(requests.get(m3u8url, proxies=self.proxies).text)
        if (len(m3u8url_clarity_1080) != 0):
            return m3u8url.replace("hls.m3u8", str(m3u8url_clarity_1080[0]))
        elif (len(m3u8url_clarity_1080) == 0) & (len(m3u8url_clarity_720) != 0):
            return m3u8url.replace("hls.m3u8", str(m3u8url_clarity_720[0]))
        elif (len(m3u8url_clarity_720) == 0 & len(m3u8url_clarity_480) != 0):
            return m3u8url.replace("hls.m3u8", str(m3u8url_clarity_480[0]))
        else:
            return m3u8url.replace("hls.m3u8", str(m3u8url_clarity_360[0]))
if __name__ == '__main__':
    Xvideos = Xvideos("https://www.xvideos.com/video75914763/stepsisraw_-_stepbrother_cums_on_his_stepsister_s_feet")
    print(Xvideos.get_video())