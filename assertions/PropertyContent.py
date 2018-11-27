class PropertyContent:

    @staticmethod
    def page_source_has_text(driver, phrase):
        return True if driver.page_source.find(phrase) else False
