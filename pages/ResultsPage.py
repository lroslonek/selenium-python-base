import logging
import time
from pages.BasePage import BasePage
from pages.assertions.PropertyContent import PropertyContent


class ResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("results page opened")

    @staticmethod
    def results_contain_phrase(driver, phrase):
        time.sleep(3)
        return PropertyContent.page_source_has_text(driver, phrase)
