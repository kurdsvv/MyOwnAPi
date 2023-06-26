import requests
from bs4 import BeautifulSoup




# jar = requests.cookies.RequestsCookieJar()
# jar.set(domain='.xhamster.com', expiry=1687785625, httpOnly='False', name='video_view_count', path= '/',
#            sameSite='Lax', secure= 'False', value=0)


class xhamster:
    def __init__(self,URL):
        self.URL= URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": '''zh-CN,zh;q=0.9,zh-TW;q=0.8,ko;q=0.7''',
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
        }

        self.proxies = {'http': '127.0.0.1:7677', 'https': '127.0.0.1:7677'}
        self.cookiestr = '''stats_uid=64669ddb037359.53176685a75; x_fst_ts=1684446683; parental-control=yes; stats_id=582612; lang=zh; x_content_preference_index=straight; xh_v2_exp_7011=%7B%22n%22%3A%22exp_7011%22%2C%22g%22%3A%22b%22%2C%22jt%22%3A1687771228%2C%22ver%22%3A3%7D; xh_v2_exp_7013=%7B%22n%22%3A%22exp_7013%22%2C%22g%22%3A%22a%22%2C%22jt%22%3A1687771228%2C%22ver%22%3A1%7D; x_retn=1; settings=eyJpc1dlYm1TdXBwb3J0ZWQiOnRydWUsImlzV2VicFN1cHBvcnRlZCI6dHJ1ZSwiZXh0RGV0ZWN0ZWRWMiI6ZmFsc2UsImV4cGlyZXMiOnsiZXh0RGV0ZWN0ZWRWMiI6MTY4Nzc3MTIzM319; stats_src_last=google.com.tw; x_viewes=%5B22545030%2C21914754%5D; stats_h_v4_straight=%7B%22v%22%3A%5B21914754%5D%2C%22l%22%3A%5B%5D%2C%22f%22%3A%5B%5D%7D; contest_region=easternAsia; video_view_count=0; stats_ssn=1687783687%3Babdd628ad23cbfde7b9238c4d7872460bd5135dd; xh_v2_exp_7006=%7B%22n%22%3A%22exp_7006%22%2C%22g%22%3A%22c%22%2C%22jt%22%3A1687783749%2C%22ver%22%3A11%7D; prs=--; _id=cf4a3271dfdc0debb01b07c3cbdb26a8f01a513b; x_tgt=%7B%22login%22%3A%2226-06-2023%22%7D; x_x_after_signup_step=1; UID=121854496
'''

    def getcookedict(self):
        cookiedict = {}
        for cookies in self.cookiestr.strip().split(";"):
            if len(cookies) != 0:
                cookiestr = cookies.split("=")
                cookiedict[cookiestr[0]] = cookiestr[1]
        return cookiedict

    def GetVideo(self):
        res = requests.get(self.URL, headers=self.headers, proxies=self.proxies, cookies=self.getcookedict()).text
        soup = BeautifulSoup(res, 'html.parser')
        element = soup.find("link", {"as": "fetch"})["href"]
        return element
if __name__ == '__main__':
    URL = "https://xhamster.com/videos/uncensored-korean-pussy-amateur-kbj-droplet-gives-super-rare-private-vip-show-xhS94yu"
    print(xhamster(URL).GetVideo())