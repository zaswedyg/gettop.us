from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    BROWSE_CATEGORIES = (By.CSS_SELECTOR, "div.box-text-inner h5.header-title")

    def open_main_page(self):
        self.open_url('https://gettop.us/')

    def verify_browse_categories(self):
        expected_browse_categories = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
        actual_browse_categories = self.find_elements(*self.BROWSE_CATEGORIES)

        for i in range(len(actual_browse_categories)):
            actual_category_text = actual_browse_categories[i].text
            assert actual_category_text == expected_browse_categories[i], f'Expected {expected_browse_categories[i]}, but got {actual_category_text}'

    def verify_browse_categories_open_correct_page(self):
        browse_categories = self.find_elements(*self.BROWSE_CATEGORIES)

        for i in range(len(browse_categories)):
            category = self.find_elements(*self.BROWSE_CATEGORIES)[i]
            category.click()
            actual_text = self.find_element(By.CSS_SELECTOR,"nav span.divider").text
            self.verify_url_contains_query(actual_text)
            self.driver.back()

