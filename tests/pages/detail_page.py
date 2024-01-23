from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class DetailPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clickeventsearch = (By.XPATH, "//a/div[2]")
        self.clickbuydetail = (By.CLASS_NAME, "btnBlue")
        self.clicktambah = (By.CLASS_NAME, "btnIncrease")
        self.clickbeli = (By.ID, "btnBeliTiket")
        self.stok_element = (By.XPATH, "//div[@class='stok-tiket']")
        self.clickmetode = (By.XPATH, "//span[@id='select2-StateMetode-container']")
        self.clickbank = (By.XPATH, "//span[@id='select2-StateJenisMetode-container']")
        self.checkbox = (By.ID, "cek")
        self.button_beli = (By.ID, "btnch")

    def get_stock_before_purchase(self):
        stok_sebelum_element = self.driver.find_element(By.XPATH, "//div[@class='stok-tiket']")
        return int(stok_sebelum_element.get_attribute("data-stok"))
    def get_stock_after_purchase(self):
        stok_sesudah_element = self.driver.find_element(By.XPATH, "//div[@class='stok-tiket']")
        return int(stok_sesudah_element.get_attribute("data-stok"))

    def click_detail_search(self):
        self.driver.find_element(*self.clickeventsearch).click()
    def click_beli_tiket_detail(self):
        self.driver.find_element(*self.clickbuydetail).click()
    def click_tambah_detail(self):
        self.driver.find_element(*self.clicktambah).click()
    def click_beli_detail(self):
        self.driver.find_element(*self.clickbeli).click()        
    def clear(self):
        self.driver.find_element(By.ID, "name").clear()
    def data_diri(self):
        self.driver.find_element(By.ID, "name").send_keys("Automation")
    def metode(self):
        self.driver.find_element(*self.clickmetode).click()
    def click_checkbox(self):
        self.driver.find_element(*self.checkbox).click()
    def click_beli(self):
        self.driver.find_element(*self.button_beli).click()

    def select_payment_method(self, method_text):
        # Locate the dropdown element
        dropdown_element = self.driver.find_element(By.ID, "StateMetode")
        # Create a Select object
        dropdown = Select(dropdown_element)
        # Select the option by visible text
        dropdown.select_by_visible_text(method_text)

    def wait_for_bank_transfer_option(self):
        # Wait for the Bank Transfer option to be clickable
        bank_transfer_option_locator = (By.XPATH, "//option[text()='Bank Transfer']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(bank_transfer_option_locator)
        )
    
    def pilih_bank(self, method_text):
        # Locate the dropdown element
        dropdown_element = self.driver.find_element(By.ID, "StateJenisMetode")
        # Create a Select object
        dropdown = Select(dropdown_element)
        # Select the option by visible text
        dropdown.select_by_visible_text(method_text)

    def wait_bank_appear(self):
        # Wait for the Bank Transfer option to be clickable
        bank_transfer_option_locator = (By.XPATH, "//option[text()='Bank Central Asia (BCA)']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(bank_transfer_option_locator)
        )