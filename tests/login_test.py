import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
            driver = webdriver.Chrome()
            driver.maximize_window()
            yield driver

# @pytest.mark.parametrize("username1, password1", [
#     ("qa.tribunbooking@gmail.com", "password1")
# ])


def test_open_tribun(driver):
    login_page = LoginPage(driver)
    login_page.open_booking("https://booking.tribunnews.com/")
    login_page.click_home()
    login_page.send_username("qa.tribunbooking@gmail.com")
    login_page.send_password("password1")
    login_page.click_login()

    time.sleep(3)


# def test_open_tribun(driver, username1, password1):  
        
#             driver.get("https://booking.tribunnews.com/")
#             driver.find_element(By.CLASS_NAME,  "menu-login").click()

#             email_sso = driver.find_element(By.ID,  "email")
#             email_sso.send_keys(username1)

#             driver.find_element(By.ID,  "password").send_keys(password1)
#             driver.find_element(By.XPATH,  "//input[@value='Login']").click()
#             time.sleep(2)
#             print("udah")