from selenium.webdriver.common.by import By

class TiketPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clicktiket = (By.CLASS_NAME, "tribun-primary-color")
        self.clickpast = (By.XPATH, "//div[@id='main-detail']/div/div[2]/div/div[2]")
        self.clickinvoice = (By.CLASS_NAME, "tribun-font-primary-color")
        self.clickpastinvoice = (By.CSS_SELECTOR, ".card-event-berjalan:nth-child(1) .tribun-font-primary-color")
        self.clicktransaksi = (By.CLASS_NAME, "text-transaksi")

    def open_tiket_page(self):
        self.driver.find_element(By.ID, "menu-burger").click()
        self.driver.find_element(By.XPATH, "//a[5]/div").click()

    def click_tiket_detail(self):
        self.driver.find_element(*self.clicktiket).click()
    
    def click_invoice(self):
        self.driver.find_element(*self.clickinvoice).click()

    def click_past_event(self):
        self.driver.find_element(*self.clickpast).click()
    
    def click_past_invoice(self):
        self.driver.find_element(*self.clickpastinvoice).click()
    
    def click_transaksi(self):
        self.driver.find_element(*self.clicktransaksi).click()
    
