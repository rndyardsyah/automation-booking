from selenium import webdriver

class ChromeDriver:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.mobile_emulation = {"deviceName": "iPhone 12 Pro"}
        self.chrome_options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        self.driver = None

    def start_driver(self):
        if not self.driver:
            self.driver = webdriver.Chrome(options=self.chrome_options)
            # self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None