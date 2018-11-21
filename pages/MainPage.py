import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.ResultsPage import ResultsPage


class MainPage(BasePage):

    query_box_locator = (By.NAME, 'q')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://www.google.com/xhtml')
        logging.info("main page opened")

    def search_for_phrase(self, phrase):
        query_box = self.driver.find_element(By.NAME, 'q')
        query_box.send_keys(phrase)
        query_box.submit()
        return ResultsPage(self.driver)






