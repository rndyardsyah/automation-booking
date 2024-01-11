import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.tiket_page import TiketPage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_transaksi_download_tiket(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    time.sleep(10)
    print("udah")

    tiket_page = TiketPage(driver)
    tiket_page.open_tiket_page()
    tiket_page.click_tiket_detail()
    time.sleep(2)
    # tiket_page.click_tiket()
    