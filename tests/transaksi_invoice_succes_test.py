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

# @pytest.mark.parametrize("username1, password1", [
#     ("qa.tribunbooking@gmail.com", "password1"),
# ])
def test_transaksi_invoice_invoice(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    time.sleep(10)
    print("udah")

    transaksi_page = TransaksiPage(driver)
    transaksi_page.click_humberger()
    transaksi_page.click_transaksi()
    transaksi_page.click_invoice()
    # assert verify_invoice.is_displayed(),"muncul"
    time.sleep(3)
    print("Transaksi page opened")
