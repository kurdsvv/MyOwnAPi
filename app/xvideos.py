import requests
from bs4 import BeautifulSoup
import re


# url_favorite = "https://www.xvideos.com/favorite/98505705/korean"
class Xvideos():
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-us",
            "Connection": "keep-alive",
            "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
            "device-memory": "8",
            "sec-ch-ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-arch": "x86",
            "viewport-width": "1092",
            "sec-ch-ua-full-version": "114.0.5735.134",
            "sec-ch-ua-platform-version": "8.0.0",
            "Origin": "https://www.xvideos.com",
            "Referer": "https://www.xvideos.com/"

            }
        self.proxies = {'http': 'host.docker.internal:7677', 'https': 'host.docker.internal:7677'}
        self.proxies = {'http': 'host.docker.internal:7677', 'https': 'host.docker.internal:7677'}
        self.PATTERN_hls = re.compile(r'html5player.setVideoHLS\(\S+\)')
        self.PATTERN_360 = re.compile(r'hls-360p\S+m3u8')
        self.PATTERN_480 = re.compile(r'hls-480p\S+m3u8')
        self.PATTERN_720 = re.compile(r'hls-720p\S+m3u8')
        self.PATTERN_1080 = re.compile(r'hls-1080p\S+m3u8')
        self.cookiestr = '''
    session_ath=black; session_blih=c20a943369d6ef29o8j1WvVLtVG7XLv9I2W6Mv6OWCWyPoTOgOKG2zswFbg%3D; html5_pref=%7B%22SQ%22%3Afalse%2C%22MUTE%22%3Atrue%2C%22VOLUME%22%3A0.7407407407407408%2C%22FORCENOPICTURE%22%3Afalse%2C%22FORCENOAUTOBUFFER%22%3Afalse%2C%22FORCENATIVEHLS%22%3Afalse%2C%22PLAUTOPLAY%22%3Atrue%2C%22CHROMECAST%22%3Afalse%2C%22EXPANDED%22%3Afalse%2C%22FORCENOLOOP%22%3Afalse%7D; xv_nbview=5; html5_networkspeed=76214; last_views=%5B%2253996353-1687582877%22%2C%2232981817-1687582895%22%2C%2263136279-1687583064%22%2C%2276779123-1687583069%22%2C%2276779805-1687583072%22%2C%2258516677-1687583138%22%2C%2259923583-1687583168%22%2C%2263064289-1687583251%22%2C%2259736463-1687583333%22%2C%2264440677-1687583366%22%2C%2254300551-1687583367%22%2C%2246538263-1687583413%22%2C%2242017723-1687583433%22%2C%2228429531-1687583494%22%2C%2236198969-1687583529%22%2C%2255747511-1687583544%22%2C%2228796993-1687583581%22%2C%2228735349-1687583601%22%2C%2224781363-1687583676%22%2C%2276779719-1687583712%22%2C%2225066605-1687583735%22%2C%2276779673-1687583776%22%2C%2276777711-1687583779%22%2C%2235230027-1687583813%22%2C%2245441291-1687583832%22%2C%2239832779-1687583848%22%2C%2245351005-1687583856%22%2C%2245440895-1687583861%22%2C%2252857253-1687583873%22%2C%2253740779-1687583915%22%2C%2236159409-1687583944%22%2C%221320872-1687583977%22%2C%2249066019-1687584039%22%2C%2235071653-1687584124%22%2C%2248940103-1687584339%22%2C%2247976951-1687584343%22%2C%2249807333-1687584344%22%2C%2262314715-1687584347%22%2C%2237406603-1687584354%22%2C%2231128713-1687584394%22%2C%2237407879-1687584471%22%2C%2224806733-1687584506%22%2C%2230102115-1687584516%22%2C%2237410965-1687584520%22%2C%2231051601-1687584519%22%2C%2250747721-1687584521%22%2C%2224806793-1687584561%22%2C%2221349341-1687584615%22%2C%2231124883-1687584644%22%2C%2227841653-1687584672%22%2C%2227849797-1687584676%22%2C%2224806811-1687584707%22%2C%2227266579-1687584838%22%2C%2227198479-1687584846%22%2C%2224806747-1687584860%22%2C%2263190041-1687769637%22%2C%2255997427-1687769642%22%2C%2238715909-1687769648%22%2C%2229487323-1687769688%22%2C%2218555575-1687769849%22%2C%2218487285-1687769916%22%2C%2235791367-1687769990%22%2C%2218555471-1687770000%22%2C%2218486125-1687770011%22%2C%2254677689-1687770598%22%2C%2254095203-1687770633%22%2C%2227797373-1687770703%22%2C%2244695569-1687770760%22%2C%2220589365-1687770833%22%2C%2216332301-1687771676%22%2C%2226822961-1687771699%22%5D; pending_thumb=%7B%22t%22%3A%5B%5D%2C%22s%22%3A%5B%5D%2C%22p%22%3A%5B%5D%2C%22r%22%3A%5B%5D%7D; last_subs_check=1; session_token=633bfa305a95687aHK3ZlpGYWzEGk3BnuD8t8ahB-G_t5anxdHhU3S3zXridWxofsrAXt21EbGL8-EiO3omAjXAltab_ovDUTZhRYVw00VRgPKOxlqCP_p2mSIO9nIbygHtl5Y5tWXwLGl5mATTrzeEDdSIDWSqZEWU8ApC3MuAh_1n9E8rqU7XuS3yxEDOdmqRj8RLs8DSlLIfwZ8lRplQMtOzb5oEmXa4odiH69M91dBFDZek7796UtjskQs25XtaOyQUOS9tUjaA7lZ1Hal9_kwliXEUgeL67soAe2I7GnXWFiyk4EzjaX0ctpmsis937JJzb-ouwU3lK9kdhi1NUkPfFlek1YgfVaEmIBQde7YkhU7nOk6tgsfrYk1c4uAKYK1n-pFvFJIGNuKUjR7MHyXCMWA-kQcC-cgZrc-i8xULEsxsbDCwN7XpeqOOu5aU-1LKI9EEdGy3dAgWjcllgiMWAsl13uRRthxEVl_z55kUllSVTS3zzJUKbIqAP78iDuTlrCgSRuWGiwAbYmt0pgm6bOorTmVArtg%3D%3D
    '''

    def getcookedict(self):
        cookiedict = {}
        for cookies in self.cookiestr.strip().split(";"):
            if len(cookies) != 0:
                cookiestr = cookies.split("=")
                cookiedict[cookiestr[0]] = cookiestr[1]
        return cookiedict

    def GetVideo(self):
        res = requests.get(self.url, proxies=self.proxies, headers=self.headers, cookies=self.getcookedict())
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
    print(Xvideos.GetVideo())
