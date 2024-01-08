import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.transaksi_page import TransaksiPage
# D:\automation-booking\tests\pages\transaksi_page.py
@pytest.fixture()
def driver():
            driver = webdriver.Chrome()
            driver.maximize_window()
            yield driver

# class open_transaksi():
def test_open_tribun(driver):
        login_page = LoginPage(driver)
        login_page.open_booking("https://booking.tribunnews.com/")
        login_page.click_home()
        login_page.send_username("qa.tribunbooking@gmail.com")
        login_page.send_password("password1")
        login_page.click_login()
        time.sleep(3)

def test_buka_transaksi():
        transaksi_page.clickdropdown()
        transaksi_page.clicktransaksi()

