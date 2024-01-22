import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.detail_page import DetailPage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_search(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    time.sleep(2)

    home_page = HomePage(driver)
    home_page.click_search()
    home_page.type_in_search("konsep bisnis")
    # time.sleep(10)

    detail_page = DetailPage(driver)
    detail_page.click_detail_search()
    detail_page.click_beli_tiket_detail()
    # detail_page.get_stok_value()
    # print("Value of data-stok attribute:", data-stok)
    detail_page.click_tambah_detail()
    detail_page.click_beli_detail()
    detail_page.data_diri()
    detail_page.select_payment_method("Bank Transfer")
    detail_page.wait_for_bank_transfer_option()
    detail_page.pilih_bank("Bank Central Asia (BCA)")
    detail_page.wait_bank_appear()
    detail_page.click_checkbox()

    time.sleep(10)
    

