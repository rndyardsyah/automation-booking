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

# start pilih bank
    def select_payment_method(self, method_text):
        dropdown_element = self.driver.find_element(By.ID, "StateMetode")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(method_text)

    def wait_for_bank_transfer_option(self):
        bank_transfer_option_locator = (By.XPATH, "//option[text()='Bank Transfer']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(bank_transfer_option_locator)
        )
    
    def pilih_bank(self, method_text):
        dropdown_element = self.driver.find_element(By.ID, "StateJenisMetode")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(method_text)

    def wait_bank_appear(self):
        bank_transfer_option_locator = (By.XPATH, "//option[text()='Bank Central Asia (BCA)']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(bank_transfer_option_locator)
        )
# end pilih bank

# start pilih E-wallet
    def pilih_ewallet(self, method_text):
        dropdown_ewallet = self.driver.find_element(By.ID, "StateMetode")
        dropdown = Select(dropdown_ewallet)
        dropdown.select_by_visible_text(method_text)

    def wait_ewallet(self):
        ewallet_option_locator = (By.XPATH, "//option[text()='E-wallet']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ewallet_option_locator)
        )
    #gopay
    def pilih_gopay(self, method_text):
        dropdown_gopay = self.driver.find_element(By.ID, "StateJenisMetode")
        dropdown = Select(dropdown_gopay)
        dropdown.select_by_visible_text(method_text)
    def wait_gopay_appear(self):
        gopay_option_locator = (By.XPATH, "//option[text()='Gopay [QRIS]']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(gopay_option_locator)
        )
    #Shopeepay
    def pilih_shopeepay(self, method_text):
        dropdown_shopeepay = self.driver.find_element(By.ID, "StateJenisMetode")
        dropdown = Select(dropdown_shopeepay)
        dropdown.select_by_visible_text(method_text)
    def wait_shopeepay_appear(self):
        shopeepay_option_locator = (By.XPATH, "//option[text()='Shopee Pay']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(shopeepay_option_locator)
        )
# end pilih E-wallet

# start pilih Gerai
    def pilih_gerai(self, method_text):
        dropdown_element = self.driver.find_element(By.ID, "StateMetode")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(method_text)

    def wait_gerai_option(self):
        gerai_option_locator = (By.XPATH, "//option[text()='Gerai']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(gerai_option_locator)
        )
    
    #alfamart
    def pilih_alfamart(self, method_text):
        dropdown_element = self.driver.find_element(By.ID, "StateJenisMetode")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(method_text)

    def wait_alfamart_appear(self):
        alfamart_option_locator = (By.XPATH, "//option[text()='Alfamart']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(alfamart_option_locator)
        )
# end pilih bank