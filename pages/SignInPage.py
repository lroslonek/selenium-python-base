import logging

from pages.BasePage import BasePage


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("sign-in page opened")
