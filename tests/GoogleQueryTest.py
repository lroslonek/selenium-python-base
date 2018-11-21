import unittest
from selenium import webdriver

from pages.MainPage import MainPage


class GoogleQueryTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def test_google_query(self):
        page = MainPage(self.driver)
        page = page.search_for_phrase("Fender Stratocaster")
        assert page.results_contain_phrase(self.driver, "Fender Stratocaster")

    def tearDown(self):
        self.driver.quit()
