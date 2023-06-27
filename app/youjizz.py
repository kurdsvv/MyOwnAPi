import requests
from bs4 import BeautifulSoup
import re
import time

class youjizz:
    def __init__(self,URL):
        self.URL=URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,ko;q=0.7",
            "Connection": "keep-alive",
            "sec-ch-ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-arch": "x86",
            "viewport-width": "1092",
            "sec-ch-ua-full-version": "114.0.5735.134",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "8.0.0",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Referer":"https://www.google.com.tw/"
        }

        self.proxies = {'http': 'host.docker.internal:7677', 'https': 'host.docker.internal:7677'}
        self.cookies = '''
        '''
        self.PATTERN_data = re.compile(r'dataEncodings = (.*);')
        self.PATTERN_480p = re.compile(r'quality\"\:\"480\"\,\"filename\"\:\"(.*?)\"')
        self.PATTERN_720p = re.compile(r'quality\"\:\"720\"\,\"filename\"\:\"(.*?)\"')
        self.PATTERN_1080p = re.compile(r'quality\"\:\"1080\"\,\"filename\"\:\"(.*?)\"')
    def cookedict(self):

        cookiedict = {}
        for cookies in self.cookies.strip().split(";"):
            if len(cookies) != 0:
                cookiestr = cookies.split("=")
                cookiedict[cookiestr[0].strip()] = cookiestr[1]
        print(cookiedict)

    def GetVideo(self):
        res = requests.get(self.URL, headers=self.headers, proxies=self.proxies)
        soup = BeautifulSoup(res.text, 'html.parser')
        element = soup.find("div", {"id": "content"})


        try:
            urllist = (self.PATTERN_data.findall(str(element))[0]).replace("\/", "/")
            result720 = self.PATTERN_720p.findall(urllist)
            if len(self.PATTERN_1080p.findall(urllist)) != 0:
                return ("https:" + self.PATTERN_1080p[0])
            elif ((len(self.PATTERN_1080p.findall(urllist)) == 0) & (len(self.PATTERN_720p.findall(urllist)) != 0)):
                return ("https:" + self.PATTERN_720p.findall(urllist)[0])
            else:
                return ("https:" + self.PATTERN_480p[0])
        except IndexError:
            pass


if __name__ == '__main__':
    url = "https://www.youjizz.com/videos/korean-beautiful-hd-spurting-part2-39734271.html"
    youjizz=youjizz(url)
    print(youjizz.GetVideo())