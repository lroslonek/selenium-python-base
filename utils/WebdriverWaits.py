from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebdriverWaits:

    @staticmethod
    def wait_for_element_visible(driver, timeout, locator):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_clickable(driver, timeout, locator):
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_element_open(driver, timeout):
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'open')))
