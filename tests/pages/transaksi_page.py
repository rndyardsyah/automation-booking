from selenium.webdriver.common.by import By

class TransaksiPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clickhumberger = (By.CLASS_NAME, "hamburger-menu")
        self.clicktransaksi = (By.XPATH, "//a[4]/div")
        self.clicktiket = (By.XPATH, "//div[@onclick='window.location.href=`https://booking.tribunnews.com/ticket/myticket/31399` ']")
        self.clickdownload = (By.ID, "btn-download-image")

# xpath=//div[@onclick='window.location.href=`https://booking.tribunnews.com/ticket/myticket/31399` ']
    def click_humberger(self):
        self.driver.find_element(*self.clickhumberger).click()
    def click_transaksi(self):
        self.driver.find_element(*self.clicktransaksi).click()
    def click_tiket(self):
        self.driver.find_element(*self.clicktiket).click()
    def click_download(self):
        self.driver.find_element(*self.clickdownload).click()