import time
import unittest

from selenium import webdriver

from pages.MainPage import MainPage


class UnauthorizedLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_item_and_total_prices_in_bag(self):
        # given
        main_page = MainPage(self.driver)
        main_page.dismiss_modals()
        login_page = main_page.go_to_sign_in_page()
        time.sleep(3)
        # when

        # then
        assert True
