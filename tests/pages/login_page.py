from selenium.webdriver.common.by import By

class LoginPage():
    def __init__ (self, driver):
        self.driver = driver
        self.login_home = (By.CLASS_NAME,  "menu-login")
        self.username_textfield = (By.ID,  "email")
        self.password_textfield = (By.ID,  "password")
        self.login_button = (By.XPATH,  "//input[@value='Login']")

    def open_booking(self, url):
        self.driver.get(url)
    def click_home(self):
        self.driver.find_element(*self.login_home).click()
    def send_username(self, username):
        self.driver.find_element(*self.username_textfield).send_keys(username)
    def send_password(self, password):
        self.driver.find_element(*self.password_textfield).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()