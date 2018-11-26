from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebdriverWaits:

    @staticmethod
    def wait_for_element_visible(driver, timeout, locator):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
