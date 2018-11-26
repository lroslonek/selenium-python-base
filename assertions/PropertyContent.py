class PropertyContent:

    @staticmethod
    def page_source_has_text(driver, phrase):
        return driver.page_source.find(phrase)
