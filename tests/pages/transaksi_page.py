from selenium.webdriver.common.by import By

class TransaksiPage():
    def __init__ (self):
        self.click_dropdown = (By.CLASS_NAME,  "login-username")
        self.click_transaksi = (By.XPATH, "//a[@title='Transaksi']")

    def clickdropdown (self):
        self.driver.find_element(*self.click_dropdown).click()
    def clicktransaksi (self):
        self.driver.find_element(*self.click_transaksi).click()
