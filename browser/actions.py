from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import MEDIUM_TIMEOUT, USERNAME

class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Navigate to specified URL"""
        self.driver.get(url)

    def login(self):
        """Perform login with predefined username"""
        try:
            username_input = WebDriverWait(self.driver, MEDIUM_TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
            )
            username_input.send_keys(USERNAME)

            continue_button = self.driver.find_element(
                By.XPATH, '//button[contains(text(), "Continue")]'
            )
            continue_button.click()
            return True
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    @staticmethod
    def wait_for_manual_action(message=""):
        """Wait for user to perform manual action"""
        print(message)
        input("Press Enter to continue after completing the manual action...")

    def get_forms(self):
        """Get all video forms on the page"""
        try:
            WebDriverWait(self.driver, MEDIUM_TIMEOUT).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//form[contains(@action, "controller.php")]')
                )
            )
            return self.driver.find_elements(
                By.XPATH, '//form[contains(@action, "controller.php")]'
            )
        except:
            return []