import logging
from decimal import Decimal

from selenium.webdriver.common.by import By

from exceptions.L10nException import L10nException
from pages.BasePage import BasePage


class BagPage(BasePage):

    __increase_quantity_locator = (By.XPATH, '//*[@id="dnn_ctr1628848_ViewBasket_BasketDetails_gvBasketDetails"]/table/tbody/tr/td[4]/div/a[2]')
    __item_price_locator = (By.XPATH, '//*[@id="dnn_ctr1628848_ViewBasket_BasketDetails_gvBasketDetails"]/table/tbody/tr/td[5]/span[2]')
    __total_price_locator = (By.XPATH, '//*[@id="dnn_ctr1628848_ViewBasket_BasketDetails_gvBasketDetails"]/table/tbody/tr/td[6]/span[2]')
    __update_bag_locator = (By.CLASS_NAME, 'NewUpdateQuant')


    def __init__(self, driver):
        super().__init__(driver)
        logging.info("bag page opened")

    def increase_product_quantity(self):
        self.driver.find_element(*self.__increase_quantity_locator).click()

    def update_bag(self):
        self.driver.find_element(*self.__update_bag_locator).click()

    def is_total_price_correct(self):
        item_price = self.__get_decimal_value(self.__item_price_locator)
        total_price = self.__get_decimal_value(self.__total_price_locator)
        logging.info("item price is: {}".format(str(item_price)))
        logging.info("price for two items is: {}".format(str(total_price)))

        if 2 * item_price == total_price:
            logging.info("PASS: prices are correct!")
            return True
        else:
            logging.error("FAIL: prices are NOT correct! :(")
            return False

    def __get_decimal_value(self, locator):
        priceText = self.driver.find_element(*locator).text
        if "£" in priceText:
            return Decimal(priceText.strip("£"))
        else:
            raise L10nException("wrong currency given!")
