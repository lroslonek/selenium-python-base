import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.ResultsPage import ResultsPage
from pages.utils.WebdriverWaits import WebdriverWaits


class MainPage(BasePage):
    query_box_locator = (By.NAME, 'q')
    country_modal_locator = (By.XPATH, '//*[@id="Form"]/div[7]/div/div/div/button')
    ad_modal_locator = (By.XPATH, '//*[@id="advertPopup"]/div/div/div[1]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.sportsdirect.com/')
        logging.info("SportsDirect page opened")

    def search_for_phrase(self, phrase):
        query_box = self.driver.find_element(By.NAME, 'q')
        query_box.send_keys(phrase)
        query_box.submit()
        return ResultsPage(self.driver)

    def dismiss_modals(self):
        WebdriverWaits.wait_for_element_visible(self.driver, 3, self.country_modal_locator).click()
        WebdriverWaits.wait_for_element_visible(self.driver, 3, self.ad_modal_locator).click()

