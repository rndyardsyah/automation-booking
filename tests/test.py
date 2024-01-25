from pages.window_page import ChromeDriver  # Replace 'your_module_name' with the actual module name

def test_chrome_driver():
    # Create an instance of the ChromeDriver class
    chrome_driver = ChromeDriver()

    # Start the driver and get the driver instance
    driver_instance = chrome_driver.start_driver()

    try:
        # Perform actions using the driver instance
        driver_instance.get("https://booking.tribunnews.com/")

        # Add more test steps as needed

    finally:
        # Close the driver when done
        chrome_driver.close_driver()

if __name__ == "__main__":
    test_chrome_driver()
