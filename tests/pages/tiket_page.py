from selenium.webdriver.common.by import By

class TiketPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clicktiket = (By.CSS_SELECTOR, ".card-event-berjalan:nth-child(2) .button-size:nth-child(1)")

    def open_tiket_page(self):
        self.driver.find_element(By.ID, "menu-burger").click()
        self.driver.find_element(By.XPATH, "//a[5]/div").click()

    def clicktiket_detail(self):
        self.driver.find_element(*self.clicktiket).click()
