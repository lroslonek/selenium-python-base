import unittest
from time import sleep

from selenium import webdriver

from pages.MainPage import MainPage


class GoogleQueryTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def test_google_query(self):
        page = MainPage(self.driver)
        page.dismiss_modals()
        page = page.search_for_phrase("Garmin forerunner")
        page = page.get_first_product_result()
        page.add_product_to_bag()
        page = page.view_bag()
        page.increase_product_quantity()
        page.update_bag()

        sleep(3)
        assert True

    def tearDown(self):
        self.driver.quit()
