import logging
from unittest import TestCase
from selenium import webdriver
from pages.MainPage import MainPage


class PricesInBagTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_should_item_and_total_bag_prices_be_correct(self):
        logging.info("")
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

    def test_should_not_sign_in_unregistered_user(self):
        # given
        main_page = MainPage(self.driver)
        main_page.dismiss_modals()

        # when
        login_page = main_page.go_to_sign_in_page()
        login_page.sign_in("unregistered@foo.com", "unregistered")

        # then
        assert login_page.is_not_signed_in("This email address or password is incorrect")
