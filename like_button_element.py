from base_page_element import BasePageElement

class LikeButtonElement(BasePageElement):
    """
    LikeButtonElement is an object created for the actual like button of an article
    """

    def click(self, driver):
        innerHTML = self.element.get_attribute("innerHTML")
        words = set(innerHTML.split())
        if "aria-label=\"Like\"" in words:
            super().click(driver)
            return True
        return False