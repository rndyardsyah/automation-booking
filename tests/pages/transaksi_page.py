from selenium.webdriver.common.by import By

class TransaksiPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clickhumberger = (By.ID, "menu-burger")
        self.clicktransaksi = (By.XPATH, "//a[4]/div")
        self.clicktiket = (By.CLASS_NAME, "button-size-history")
        self.clickdownload = (By.ID, "btn-download-image")
        self.clicktidakberhasil = (By.CSS_SELECTOR, ".tablinks:nth-child(2)")
        self.clickinvoicesucces = (By.CLASS_NAME, "btn-ticket-invoice")
        self.clickinvoicefailed = (By.CLASS_NAME, "button-invoice-ex")
        self.verifyinvoice = (By.CLASS_NAME, "contents-invoices")


# xpath=//div[@onclick='window.location.href=`https://booking.tribunnews.com/ticket/myticket/31399` ']
    def click_humberger(self):
        self.driver.find_element(*self.clickhumberger).click()
    def click_transaksi(self):
        self.driver.find_element(*self.clicktransaksi).click()
    def click_tiket(self):
        self.driver.find_element(*self.clicktiket).click()
    def click_download(self):
        self.driver.find_element(*self.clickdownload).click()
    def click_tidakberhasil(self):
        self.driver.find_element(*self.clicktidakberhasil).click() 
    def click_invoice(self):
        self.driver.find_element(*self.clickinvoicesucces).click()
    def click_invoice_failed(self):
        self.driver.find_element(*self.clickinvoicefailed).click()
    def verify_invoice(self):
        self.driver.find_element(*self.verifyinvoice)