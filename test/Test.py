import requests
from bs4 import BeautifulSoup
import re
import json
# PATTERN_hls = re.compile(r'html5player.setVideoHLS\(\S+\)')
# PATTERN_360 = re.compile(r'hls-360p\S+m3u8')
# PATTERN_480 = re.compile(r'hls-480p\S+m3u8')
# PATTERN_720 = re.compile(r'hls-720p\S+m3u8')
# PATTERN_1080 = re.compile(r'hls-1080p\S+m3u8')
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

from app.pornHub import PornHub

pornhub = PornHub("https://cn.pornhub.com/view_video.php?viewkey=ph639c60f524f29")
urls = json.loads(pornhub.get_video())
if len((urls["quality"][3])) != 0:
    print(urls["quality"][3]["videoUrl"])
elif ((len((urls["quality"][3])) == 0) & (len((urls["quality"][2])) != 0)):
    print(urls["quality"][2]["videoUrl"])
else:
    print(urls["quality"][1]["videoUrl"])


