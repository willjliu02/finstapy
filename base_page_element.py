from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class BasePageElement(ABC):
    """Base page class that is initialized on every page object class."""

    def __init__(self, element) -> None:
        self.element = element

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

    def _get_element(self):
        """
        Gets the element
        """
        return self.element

    def click(self, driver):
        action = ActionChains(driver)
        action.click(self.element)
        action.perform()
        return True