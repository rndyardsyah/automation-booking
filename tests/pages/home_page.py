from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage:
    def __init__ (self, driver):
        self.driver = driver
        self.clicksearch = (By.ID, "menu__toggle__search")
        self.findsearch = (By.ID, "keywordCariMobile")
        self.clickbelitiket = (By.XPATH, "//div[@id='main-home']/div/section[3]/div[2]/div[2]/div/div/a")

    
    def click_search(self):
        self.driver.find_element(*self.clicksearch).click()

    def type_in_search(self, search_text):
        search_input = self.driver.find_element(*self.findsearch)
        search_input.send_keys(search_text)
        search_input.send_keys(Keys.RETURN)

    def click_beli_tiket(self):
        self.driver.find_element(*self.clickbelitiket).click()