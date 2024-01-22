from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DetailPage:
    def __init__ (self, driver):
        self.driver = driver
        self.clickeventsearch = (By.XPATH, "//a/div[2]")
        self.clickbuydetail = (By.CLASS_NAME, "btnBlue")
        self.clicktambah = (By.CLASS_NAME, "btnIncrease")
        self.clickbeli = (By.ID, "btnBeliTiket")
        self.stok_element = (By.XPATH, "//div[@class='stok-tiket']")
        self.clickmetode = (By.XPATH, "//span[@id='select2-StateMetode-container']")
        self.findsearch = (By.XPATH, "//input[@type='search']")
        self.clickbank = (By.XPATH, "//span[@id='select2-StateJenisMetode-container']/div/p")
    
    def get_stok_value(self):
        self.driver.find_element(*self.stok_element)
        return stok_element.get_attribute("data-stok")

    def click_detail_search(self):
        self.driver.find_element(*self.clickeventsearch).click()
    def click_beli_tiket_detail(self):
        self.driver.find_element(*self.clickbuydetail).click()
    def click_tambah_detail(self):
        self.driver.find_element(*self.clicktambah).click()
    def click_beli_detail(self):
        self.driver.find_element(*self.clickbeli).click()        
    def data_diri(self):
        self.driver.find_element(By.ID, "name").send_keys("Automation")
    def metode(self):
        self.driver.find_element(*self.clickmetode).click()
    def type_in_metode(self, search_text):
        search_input = self.driver.find_element(*self.findsearch)
        search_input.send_keys(search_text)
        search_input.send_keys(Keys.RETURN)

    def pilih_bank(self):
        self.driver.find_element(*self.clickbank).click()
        # self.driver.find_element(By.XPATH, "//span[@id='select2-StateJenisMetode-container']").click()
        