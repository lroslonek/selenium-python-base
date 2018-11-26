import logging
from selenium.webdriver.common.by import By


class BasePage:

    _sign_in_locator = (By.ID, 'dnn_dnnLOGIN_loginLink')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    def __init__(self, driver):
        self.driver = driver