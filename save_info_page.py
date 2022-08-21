from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from base_page import BasePage

from save_info_page_locators import SaveInfoPageLocators

from save_info_button_element import SaveInfoButtonElement

class SaveInfoPage(BasePage):
    """
    Has the brief question to save the info.
    """

    def click_button(self):
        try:
            locator = SaveInfoPageLocators.SAVE_INFO_BUTTON
            button = WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element(locator[0], locator[1])
            )
            saveInfoButton = SaveInfoButtonElement(button)
            saveInfoButton.click(self.driver)
            return True
        except TimeoutError:
            self.driver.get('https://www.instagram.com')