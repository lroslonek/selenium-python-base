import logging


class BasePage:

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    def __init__(self, driver):
        self.driver = driver
        logging.info("driver initialized")
