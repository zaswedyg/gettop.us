from pages.main_page import MainPage
from pages.shop import Shop


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.shop = Shop(self.driver)
