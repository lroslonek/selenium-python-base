import logging

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.WebdriverWaits import WebdriverWaits


class BagPage(BasePage):

    __increase_quantity_locator = (By.XPATH, '//*[@id="dnn_ctr1628848_ViewBasket_BasketDetails_gvBasketDetails"]/table/tbody/tr/td[4]/div/a[2]')
    __update_bag_locator = (By.CLASS_NAME, 'NewUpdateQuant')

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("bag page opened")

    def increase_product_quantity(self):
        self.driver.find_element(*self.__increase_quantity_locator).click()

    def update_bag(self):
        self.driver.find_element(*self.__update_bag_locator).click()

