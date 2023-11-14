from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class BrowserDriver:
    def __init__(self, headless=False):
        self.headless = headless
        self.driver = None

    def initialize_driver(self):
        """Initialize and configure the WebDriver"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")

        try:
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            return self.driver
        except Exception as e:
            raise Exception(f"Failed to initialize WebDriver: {str(e)}")

    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()