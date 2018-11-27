import unittest

from selenium import webdriver

from pages.MainPage import MainPage


class PricesInBagTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_should_item_and_total_bag_prices_be_correct(self):
        # given
        main_page = MainPage(self.driver)
        main_page.dismiss_modals()
        result_page = main_page.search_for_phrase("Garmin forerunner")
        product_page = result_page.get_first_product_result()

        # when
        product_page.add_product_to_bag()
        bag_page = product_page.view_bag()

        # and
        bag_page.increase_product_quantity()
        bag_page.update_bag()

        # then
        assert bag_page.is_total_price_correct()
