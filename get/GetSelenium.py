from selenium import webdriver

class GetSelenium:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.chrome_options.add_argument('--proxy-server=http://127.0.0.1:7677')
        self.chrome_options.add_argument("disable-javascript")

        self.chrome_options.add_argument("–incognito")
        self.chrome_options.add_experimental_option("prefs", self.prefs)

    def GetDriver(self):
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.set_window_size(1,1)
        return driver

