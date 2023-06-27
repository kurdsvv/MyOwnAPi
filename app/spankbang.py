from bs4 import BeautifulSoup
import re
import requests
import json
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Spankbang:
    def __init__(self, url):
        self.url = url
        self.PATTERN_480p = re.compile(r'\'480p\': \[\'(.*?)\'\]')
        self.PATTERN_720p = re.compile(r'\'720p\': \[\'(.*?)\'\]')
        self.PATTERN_1080p = re.compile(r'\'1080p\': \[\'(.*?)\'\]')
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
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "8.0.0",
            "Host": "spankbang.com",
            "Origin": "https://spankbang.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document"
        }
        self.proxies = {'http': 'http://host.docker.internal:7677', 'https': 'http://host.docker.internal:7677'}
        self.cookiestr = '''
            coe=ww; age_pass=1; age_pass=1; ana_vid=ec4c59a2b79ef7afc4bd56b3f93154eaaaed6b21f5eadb5eebf2a4eea7f9f38b; cor=Unknown; backend_version=main; __cfruid=568f88b8b0813092ea989168a6b677d01c36b4c5-1687861941; preroll_skip=1; __cf_bm=8gWn2k1LGOAI4HBoAAvvpdoAq02RtVljJEK7SnRcma0-1687861943-0-AWrQDlZJHZa6SptzHilooSnyWEbOVAEpW8pErFm0P8/WEbkFWNWwxLEir5mqqYbOgiug+kk+qX+Dkqv+CU6XF8h6I32Rp+xmS775re+Ki/mh; ana_sid=48b3a107453e97d45661b12307cc7abb0ae508dc77927dc6ba17f0217eb6c21f; auth=IjI1MTA0MjAzOjo6c3BhbmtiYW5nX3N3cWUi.TSHAR1Iqbs7hlupqoxKhzU2nsz8; cfc_ok=00|2|ww|www|master|25104203; cf_chl_2=4480e963c861d94; cf_clearance=RA2lIFufW.AINI.ShtCbdQPWWoNvXdXTIt9_j5ICrXA-1687862054-0-250; sb_session=eyJfcGVybWFuZW50Ijp0cnVlLCJjc3JmX3Rva2VuIjoiNjgyYmFmY2ZhMGVhZDU5MDliYWJiMGNiMGQyNGU1MTZmYmU3M2M1ZCJ9.ZJq7Ng.3K8FUg7ybHdq025kTohGKKPat8A        
        '''
        self.PostStr = '''md=jY5CHxFFmeO8Nr50qMsHapObPNk2cHj6zCQeRAVUPJA-1687862054-0-AWKsAHbxUSqs9j96jJFWSXI21ha1xyWdv36eb5OeEJIrogl9wwx0FfCIrPEjB2-6VDjYUA4nhLeFpTk5cUzF_XLM7tuQM7lEd-t2kUQqgMnM54GIawvZltGq7TxwwSOyHvT2yhJfuiwaoJGbqYMzgcqxCHazo1FPPCjEALmw7-0WaQPcIv_EZ57D5hpIDFO0TPCeRMcu_b9Sr3UOIU4ehpGi1OWy1EbxG85ZhrAPAAC4h7ZQIOPYVgTjlvTZKNsR18_Tkjwe13ADI7tACe2HWsvbpisCYfLd3hVZxyqof8nEmARqO2LMxtx3oqV6XH2Ae-6xuT-xLFRUcoPdTAFbVhkZQDY-MSLz3SY7VW5-_czesiif-1sGSXtQuP3aGOOJWMnMzKFC2XrEEaH8cxp0Khe0U7uQjHncuZf0jH62IR7H3HM9YrWe_CYvk_wHRv98DR94SwIRqJaM2JaR1ouiLISEAtyDykMYwpdhmUa0nJvJXvFFNJEMK4IN4UtsPqcJAcyOZ6fc-w2KTyuoiRdX_Li9zUjMav4-o_xS8x_3rwrlT4Qa_hSfYXvoKN0GNY214NOFJ8Sg5iSJJxabG66Iz49ZLk_avEu_S_ncBt_CBJzgflIZHozqsfH8wwqHs-ePa8MQEtswFvAPNjPn_qfEbVPMCkZY6c9alRgb8fOCFlkiBUGbHqOeuRU9Xkeg0PxL1LRHPUqS-aR4WQlVReuba6WWx32ItDPURNuxkmE0-B7yugfc94iozeS5D2MD8a7NIauJr7ZmdR5YAHyJqf3gNQQ5KwQAxonzTrR-1Hdo9wfubosr_CF3O3y367V2LwvnJm5nZymTXz5oTa97aYWvIDwNbCrG1Jfn8J-GLbfO9ULzJU7iu7-k72R8e6firV7VAqwVVu2SJatAjGt8qxgyTm5uNVi15PZ__fW3HVkh_semzGXBe4cQdvmu8nd5V9-pTBs1eejwhY2OSIs1oUSlLXGzAW50MfHUZt4Uf2XiVELbZ8inmFhBES1EhE_uauWhRKBtNQjv8sLHZVR_L8xNYyIayZy7a2skPSr3s02Bqh8XUgm2QTw0jn7ePd3PWYF7tppA9wCXimN11SNafjEIauZ52Wae2u9UqUAVTqXCHTfriT-wCWW5DTunJHXmgZARLtwEWI0ZgKFOmSGS5-Hh_GnKCxQnp6DlTKtWsxpMxw8rfu5pTmyii_wRwR_-C-LQ31jnQKzl6Okfjn9U-qwC6IaGO0QK0rEWjG_hAeR9M6-bOaNp4CASu56vZFqVDzM9W-NzZBgdOf8_ycylCe2WGblDW3IieH6mDX2iK-2_y2VxW8pvDmYh1bRZ1AcrHI31FTE-rqCA6OvAK0R0psNNmxzaC9Hbmz5ZOFh8Gu9ZdmHvfFHKyFAvum8DU1blr84eRr3nw4sch0hVx9u6xt_sBjr3DQ66iLZ20BWM9IqignuKsgEVpXV4KV9sN6WesFS9cK-Vinfouveu7ZoROZyIja4tY6E9n_wODTjxe-0EYr3FGch00dYUqNtI_zSqICunzH4iGRh3UIF5UcySTHsJAgiTx9Bc-Kz9bWr5e1YBjz7Tgt9yMGefcRUKFxBrYhAuyOaXfXUaQtY7rPH6-pi6FIpjbzSUCZxNYHcX4Xk-EtL22NzClVfjwnhgB1cuv4lXYiHWVqbgm70FvAGB_xzN0tqg71bXS7ZUJFgk0CaYs6mnxuDOUrI7bvJgRae6-FGbE4zZrrcW6TlXUREMtscTOwiSgg09q6yZ0YqU2XPEcNMXZEoT941sS_5wjlDzzbtbmjXWe54hzIgZa2ZqkQ2reXhv9coMsGVoenouRvbV4cgAY_ZRXdhHs7gyYy6b9c6kCWSuRZ5m962GdKGGnOPjqVUJ-E9B6plmMzfBgaWuYtS1-OxOup0QH1rxV9_4aHWMFeoyctDkMGEtAiClbhohBIkyaaWtHpiRqAWHJzP3wgPDZsmGPKgUNLo5akfQNV3qrr95moR3LC_M-35FDTAngYc422ck-3TQ5wBIcSHrEe7bcFoIJZj3UfuLaxR4MrST9oY12j_K6BKs7P7kZQNndEy7iqqLyTw53chnGBswXUChtVWWL_mQtKyGMhlU2BZC_ozhx1OvyWDSq4R6tr2PS0R4fXbpFM1S8zxlA5ibyhJNr_-_0U6JEF02YUQN3YGnn1A23DNgWvYMhgaVNMMf3Q7kR2ABFGvet9gmxGu1PmNC7cq_Zjl8rmQuLAAAt_8wUURjHO28dfIBhR2gj9KCRc11aXnwywYh9EneSYOoigsXmbBjYzK3Yy1IIvFi05wA1m-GC31fLrTjASaGHOf1aMor6Nf7VkFupS8cKns0HFvELlCOuQWpSaUgjHEBfHJ7Hn595XErhSb0J96E-qOt-yrVmyzczCWwXQ_cxUkG39lc3LHlIFg37CSfp3aCXN7aX6C3vhwtf1mt_WSThR_7ksjfPcLCgef-VuqaMPL6ISR3hH8cLjJlEZw2Br7eUoTwltM0dbgoYcGaxtzvx9j90ZguNH0qN6Wmh0rQgUVNkxdkE8vk6wJVfNM7NnftF2tSM3SzjxPUwhuTrk8Esex21oRJqOJzCKLeEesldoW86PslR0ZikAyqaxvhN9guFNiKBft1J9-EytW_xsLHOrzizkGab-4NDJKxVc9Wi2UnDsnGOrYVSxm4q_9R8L7l9lJDsK3wteli1n21DvJsMwqMeu5CwToS3kyYsMnQzNMYZjqW8S67Akq1xydoPp8afbG2NPb739p27GASfNTUsDIq-Pe_wmxC9IykAo43aCiuisf_tVso-J_KM93ZdCuunf-Mt_GS_NVlS2L-bgEjR3qSiA8wOp6-dAEGH5F0HzYUz5Vrg-xwBM37oAMCm4HeoZHppHDj8SEuLepENbzBMJfxiTQGEXwIc5Um-fYA0zpULd09P5WtA9doLH4Adm9GnEwVrXuQ5lsWGiOYZ_YrbI3CIL7fYvKe69o-BU00qTavhjvslpEaK-E6axqgiU-SBV6nhgISucglSoyLia3G7sLQW23jUn7iwZRI2hMIwwLSw2s7xAX-OQE1Cy_Hme3PdCH4s7JdCtNSzP9U7Cu84Yf6kz5ac6hZDU2epBibsr-6qLE5OJEmZ-h7l9s3yQCAS02I8MTn_HDL-WyUxhncxducCm_4MImY5pF4LYFlTx62pEyqfpkmGz2wiiKPhu7yImkvwkNTDOcO6MKpisULI_w-9P31VYON6b1rqmUzN1UgggQ3eQpE8q7riZpuqN4Kqp2h48QngH63pLKyg7WBidvHj8pfsoEbDZn-J5MrYBVRp5TWz3Td1kqz1kaMXlAL9bpEJq9kNJzhs_NAzRURfBmBncOZjCPs56r8xh6buawS7cqm-aE11vq-zR1jRi0uQEUnHiHWP1dN6lKf9YDSF80rUyg-k_KziKlgiuNi2CM9_F-KCAi1buakvcbECTpV5OSbMsJ_d4T770Pl31iTjNtlewnmMSh31bU7EmhLEtT3Mk23-Zh_3GqaGWPL199D00KYeHBa6nHz7L8VKEzbHPj6eSGAPArZyo-iQtNR5B6WTmn7IFJjU_FeUV2NuGRBZTfzwmLWkriM12n3-XWyIulImp4lbfaVlithfB3ENYqT4SMWN2wPVD2OZ8FxxlWaSsAe0EvmbP19DWti3EAoXCUXkKFHdx8DpOh9woPEBjxR2nbP&sh=5ee45e926d2caa904c7b1486b195f114&aw=CBaARYmXUmFq-1-7ddd094dcfb02ae0&cf_ch_cp_return=24236186f12797eeb070eb9708463cd1%7C%7B%22managed_clearance%22%3A%22i%22%7D
        '''
    def GetPostStr(self):
        PostStriDict = {}
        PostStrList = self.PostStr.strip().split("&")
        for PostStr in PostStrList:
            PostStriDict[PostStr.strip().split("=")[0]] = PostStr.strip().split("=")[1]
        return PostStriDict

    def getcookedict(self):
        cookiedict = {}
        for cookies in self.cookiestr.strip().split(";"):
            if len(cookies) != 0:
                cookiestr = cookies.split("=")
                cookiedict[cookiestr[0]] = cookiestr[1]
        return cookiedict


    def GetVideo(self):
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        # chrome_options.add_argument("disable-javascript")
        # chrome_options.add_argument("–incognito")
        # chrome_options.add_argument('--ignore-certificate-errors')  # 主要是该条
        # chrome_options.add_argument('--ignore-ssl-errors')
        # chrome_options.add_experimental_option("prefs", prefs)
        # driver = webdriver.Chrome(options=chrome_options)
        # driver.minimize_window()
        # driver.get(self.url)

        PostStrDict=self.GetPostStr()
        res = requests.post(self.url, proxies=self.proxies, headers=self.headers, cookies=self.getcookedict(),json=PostStrDict)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            # WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'container')))
            urls = soup.find(id="container").find_all('script', {'type': "text/javascript"})[0].get_text()
            m3u8_1080p = self.PATTERN_1080p.findall(urls)
            m3u8_720p = self.PATTERN_720p.findall(urls)
            m3u8_480p = self.PATTERN_480p.findall(urls)
        except TypeError:
            pass
        if len(m3u8_1080p) != 0:
            # driver.close()
            return m3u8_1080p[0]
        elif ((len(m3u8_1080p) == 0) & (len(m3u8_720p) != 0)):
            # driver.close()
            return m3u8_720p[0]
        else:
            # driver.close()
            return m3u8_480p[0]


if __name__ == '__main__':
    Spankbang = Spankbang("https://spankbang.com/642qi/video/hot+korean+girl+play+squirt+game+with+friends")
    print(Spankbang.GetVideo())
