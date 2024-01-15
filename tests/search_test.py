import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_search(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    time.sleep(2)

    home_page = HomePage(driver)
    home_page.click_search()
    home_page.type_in_search("13angga")
    # time.sleep(10)