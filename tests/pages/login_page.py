# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://booking.tribunnews.com/")
        self.driver.find_element(By.ID, "menu-burger").click()
        self.driver.find_element(By.CLASS_NAME, "button-login").click()
        # self.driver.find_element(By.CLASS_NAME, "button-logout").click()
    
    def logout(self):
        self.driver.find_element(By.ID, "menu-burger").click()
        self.driver.find_element(By.CLASS_NAME, "button-logout").click()

    def login(self):
        email_sso = self.driver.find_element(By.ID, "email")
        email_sso.send_keys("qa.tribunbooking@gmail.com")

        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
