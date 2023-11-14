from selenium.webdriver.common.by import By


class Video:
    def __init__(self, form_element, index):
        self.form_element = form_element
        self.index = index
        self.views = self._extract_views()

    def _extract_views(self):
        """Extract views count from form parent element"""
        try:
            parent = self.form_element.find_element(By.XPATH, './../..')
            views_text = parent.find_element(By.CLASS_NAME, 'text-warning').text.strip()
            return views_text
        except:
            return "N/A"

    def select_option(self, option_text="200"):
        """Select an option in the form's select element"""
        select = self.form_element.find_element(By.TAG_NAME, 'select')
        for option in select.find_elements(By.TAG_NAME, 'option'):
            if option_text in option.text:
                option.click()
                return True
        return False

    def submit(self):
        """Submit the form"""
        try:
            submit_btn = self.form_element.find_element(
                By.XPATH, './/button[contains(text(), "Send Views")]'
            )
            submit_btn.click()
            return True
        except:
            return False