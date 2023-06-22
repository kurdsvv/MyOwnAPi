from bs4 import BeautifulSoup
import re
import requests


class KoreanBjClub:
    def __init__(self,URL):
        self.URL=URL
        self.PATTERN = re.compile(r'\"contentURL\"\: \"(.*)\"')
        self.proxies= {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
        self.header= {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-us",
           "Connection": "keep-alive",
           "Accept-Charset": "utf-8;q=0.7,*;q=0.7"}
    def GetVideo(self):
        res=requests.get(self.URL,headers=self.header,proxies=self.proxies)
        soup = BeautifulSoup(res.text,'html.parser')
        element = soup.find("header", {"class": "entry-header"})
        m3u8 = element.find("script", {"type": "application/ld+json"}).get_text()
        return self.PATTERN.findall(m3u8)[0]

if __name__ == '__main__':
    url="https://koreanbj.club/chinese-amateur-cna20234153/"
    print(KoreanBjClub(url).GetVideo())
