from selenium.webdriver.common.by import By
from pages.base_page import Page

class Shop(Page):
    CURRENT_PAGE = (By.CSS_SELECTOR, "li span.current")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "a.next.page-number")
    PREVIOUS_PAGE_BUTTON = (By.CSS_SELECTOR, "a.prev.page-number")
    PAGE_NUMBER_BUTTONS = (By.CSS_SELECTOR, "a[class='page-number']")
    PRODUCT = (By.CSS_SELECTOR, "div.product-small .box-image")
    QUICK_VIEW = (By.CSS_SELECTOR, "a.quick-view")
    SHOP_URL = 'https://gettop.us/shop/'

    def open_shop_page(self):
        self.open_url('https://gettop.us/shop/')

    def open_quick_view(self):
        self.hover_over_element(*self.PRODUCT)
        self.click(*self.QUICK_VIEW)

    def close_quick_view_by_x(self):
        self.find_element(By.CSS_SELECTOR, "button.mfp-close").click()

    def verify_user_can_add_product_to_cart(self):
        self.click(By.NAME, "add-to-cart")
        count = self.find_element(By.CSS_SELECTOR, "a span.cart-icon.image-icon").text
        assert int(count) > 0, f'Cart got less than 1 product'

    def verify_user_can_click_through_multiple_page_numbers(self):
        page_number_buttons = self.find_elements(*self.PAGE_NUMBER_BUTTONS)

        for i in range(len(page_number_buttons)):
            page_number_button = self.find_elements(*self.PAGE_NUMBER_BUTTONS)[i]
            page_number_button.click()
            actual_text = self.find_element(By.CSS_SELECTOR, "ul a.page-number").text
            self.verify_url_contains_query(actual_text)
        first_page = self.find_elements(*self.PAGE_NUMBER_BUTTONS)[0]
        first_page.click()
        expected_url = 'https://gettop.us/shop/'
        assert self.driver.current_url == expected_url, f'Expected {expected_url}, but got {self.driver.current_url}'

    def verify_user_can_click_through_multiple_pages_by_clicking_next(self):
        page_number_buttons = self.find_elements(*self.PAGE_NUMBER_BUTTONS)

        for i in range(len(page_number_buttons)):
            self.find_element(*self.NEXT_PAGE_BUTTON).click()
            actual_text = self.find_element(*self.CURRENT_PAGE).text
            self.verify_url_contains_query(actual_text)

    def verify_user_can_click_through_multiple_pages_by_clicking_back(self):
        page_number_buttons = self.find_elements(*self.PAGE_NUMBER_BUTTONS)

        for i in range(len(page_number_buttons)):
            self.find_element(*self.PREVIOUS_PAGE_BUTTON).click()
            actual_text = self.find_element(*self.CURRENT_PAGE).text
            if actual_text not in self.driver.current_url:
                break
            self.verify_url_contains_query(actual_text)
        assert self.driver.current_url == self.SHOP_URL, f'Expected {self.SHOP_URL}, but got self.driver.current_url'