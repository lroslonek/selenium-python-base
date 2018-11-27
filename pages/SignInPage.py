import logging

from selenium.webdriver.common.by import By

from assertions.PropertyContent import PropertyContent
from pages.BasePage import BasePage


class SignInPage(BasePage):

    __email_box_locator = (By.ID, 'dnn_ctr28678722_LoginScreen_registerLogin_txtExistingCustomerEmailAddress')
    __password_box_locator = (By.ID, 'dnn_ctr28678722_LoginScreen_registerLogin_txtPassword')
    __sign_in_locator = (By.ID, 'dnn_ctr28678722_LoginScreen_registerLogin_btnRegisteredCustomer')

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("sign-in page opened")

    def sign_in(self, email, password):
        email_box = self.driver.find_element(*self.__email_box_locator)
        password_box = self.driver.find_element(*self.__password_box_locator)
        sign_in_btn = self.driver.find_element(*self.__sign_in_locator)
        email_box.send_keys(email)
        password_box.send_keys(password)
        sign_in_btn.click()

    def is_not_signed_in(self, sign_in_phrase):
        if PropertyContent.page_source_has_text(self.driver, sign_in_phrase):
            logging.info("PASS: unregistered user is not signed-in")
            return True
        else:
            logging.error("FAIL: unregistered user has signed-in!")
            return False
