import re
import sys
import json
import time
import js2py
import random
import requests
from tqdm import tqdm
from lxml import etree
from pyquery import PyQuery as pq


class PornHub(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-us",
                        "Connection": "keep-alive",
                        "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}

    def get_keys(self, category, start_page, end_page):
        """
        Query based on incoming parameters
        :param category: video category(e.g., ht:最热门, mv:最多次观看...)
        :param start_page: the start page
        :param end_page: the end page
        :return: json file
        """
        base_url = "https://cn.pornhub.com/video"
        for page in tqdm(range(start_page, end_page + 1), ncols=80):
            params = {
                "o": category,
                "page": page
            }
            try:
                self.session.proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
                response = self.session.get(url=base_url, params=params, headers=self.headers, timeout=45, )
                if response.status_code == 200:
                    doc = pq(response.text)
                    rows = doc("ul#videoCategory li.pcVideoListItem .wrap")
                    # to save lists
                    box_lists = []
                    for row in rows.items():
                        tag_a = row(".phimage a")
                        link_url = "https://pornhub.com" + str(tag_a.attr("href"))
                        title = tag_a("img").attr("alt")
                        cover = tag_a("img").attr("data-src")
                        media_book = tag_a("img").attr("data-mediabook")
                        duration = tag_a(".marker-overlays .duration").text()
                        quality = tag_a(".marker-overlays .hd-thumbnail").text()
                        tag_msg = row(".thumbnail-info-wrapper")
                        author = tag_msg(".usernameWrap a").text()
                        link_author = "https://pornhub.com" + str(tag_msg(".usernameWrap a").attr("href"))
                        views = row(".videoDetailsBlock .views var").text()
                        likes = row(".videoDetailsBlock .rating-container .value").text()
                        info = {
                            "title": title,
                            "link_url": link_url,
                            "cover": cover,
                            "media": {
                                "media_book": media_book,
                                "duration": duration,
                                "quality": quality,
                                "author": author,
                                "link_author": link_author
                            },
                            "views": {
                                "views": views,
                                "likes": likes
                            }
                        }
                        # push to list
                        box_lists.append(info)
                    # save to json file
                    with open("./pornhubs/pornhub-{}-{}.json".format(category, page), "w", encoding="utf-8") as f:
                        f.write(json.dumps(box_lists, ensure_ascii=False))
                    time.sleep(random.randint(2, 5))
            except Exception as e:
                print(e)

    def get_video(self):
        """
        Way to parse encrypt signal video url
        use proxies or you can directly surfer outer-net
        :return: video-object
        """
        self.session.proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
        res = self.session.get(url=self.url, headers=self.headers, timeout=40, )
        if res.status_code == 200:
            try:
                html = etree.HTML(res.text)
                doc = html.xpath('.//div[@id="player"]/script[1]/text()')[0]
                doc = str(doc.split("playerObjList")[0]).strip()
                # find the object of property
                flash_vars = re.findall('flashvars_\d+', doc)[0]
                message = js2py.eval_js("".join(doc) + flash_vars).to_dict()
                # default to choose the best quality
                cover = message["image_url"]
                title = message["video_title"]
                quality = []
                if message["mediaDefinitions"]:
                    video_url = message["mediaDefinitions"][-1]["videoUrl"]
                    result = self.session.get(url=video_url, headers=self.headers, timeout=40)
                    quality = json.loads(result.text)
                else:
                    quality.append('parse url error')
                info = {
                    "title": title,
                    "cover": cover,
                    "quality": quality
                }
                return json.dumps(info, ensure_ascii=False)
            except Exception as e:
                return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
        else:
            return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)


if __name__ == '__main__':
    pornhub = PornHub("https://cn.pornhub.com/view_video.php?viewkey=ph639c60f524f29")
    urls = json.loads(pornhub.get_video())
    if len((urls["quality"][3])) != 0:
        print(urls["quality"][3]["videoUrl"])
    elif ((len((urls["quality"][3])) == 0) & (len((urls["quality"][2])) != 0)):
        print(urls["quality"][2]["videoUrl"])
    else:
        print(urls["quality"][1]["videoUrl"])
