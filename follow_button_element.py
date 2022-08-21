from base_page_element import BasePageElement

class FollowButtonElement(BasePageElement):
    """
    Represents the follow button on the Account Pages
    """

    def click(self, driver):
        if self.element.text == "Follow":
            super().click(driver)
        return True