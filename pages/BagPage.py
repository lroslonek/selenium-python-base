import logging

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.WebdriverWaits import WebdriverWaits


class BagPage(BasePage):

    __add_to_bag_locator = (By.CLASS_NAME, 'addToBag')

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("bag page opened")

    # def add_product_to_bag(self):
    #     WebdriverWaits.wait_for_element_visible(self.driver, 5, self.__add_to_bag_locator).click()
    #
    # def view_bag(self):
    #     WebdriverWaits.wait_for_element_open(self.driver, 4)
    #     self.driver.find_element(*self.__view_bag_locator).click()
    #     return BagPage(self.driver)
