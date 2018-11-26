import logging

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.ProductPage import ProductPage
from utils.WebdriverWaits import WebdriverWaits


class ResultsPage(BasePage):

    __first_product_result_locator = (By.XPATH, '//*[@id="navlist"]/li[1]')

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("results page opened")

    def get_first_product_result(self):
        WebdriverWaits.wait_for_element_visible(self.driver, 5, self.__first_product_result_locator).click()
        return ProductPage(self.driver)
