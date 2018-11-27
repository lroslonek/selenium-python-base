import unittest
from selenium import webdriver
from pages.MainPage import MainPage


class UnauthorizedLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_should_not_sign_in_unregistered_user(self):
        # given
        main_page = MainPage(self.driver)
        main_page.dismiss_modals()

        # when
        login_page = main_page.go_to_sign_in_page()
        login_page.sign_in("unregistered@foo.com", "unregistered")

        # then
        assert login_page.is_not_signed_in("This email address or password is incorrect")
