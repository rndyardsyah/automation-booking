import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.transaksi_page import TransaksiPage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_open_tribun(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    time.sleep(10)
    login_page.logout()
    # assert driver.find_element_by_id("main-home").is_displayed(), "muncul"
