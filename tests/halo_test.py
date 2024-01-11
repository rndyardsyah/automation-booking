import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()
    yield driver
    # Teardown: close the browser window after the test
    driver.quit()

def test_google_search_input_presence(setup):
    # Navigate to Google homepage
    setup.get("https://www.google.com")

    # Check if the Google search input field is present
    search_input = setup.find_element(By.NAME, "q")
    assert search_input.is_displayed(), "Google search input field not found on the page."
