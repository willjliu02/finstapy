from http.client import CONTINUE

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

from base_page import BasePage

from home_page_locators import HomePageLocators
from scroll_post_locators import ScrollPostLocators

from not_now_button_element import NotNowButtonElement





class HomePage(BasePage):
    """
    Represents the home page, where the users' feed typically is.
    """

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.posts = []

    def close_notification_alert(self):
        """
        Closes the notification alert that pops up as you switch to the page
        """
        try:
            locator = HomePageLocators.NOT_NOW_BUTTON
            button = WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(locator[0], locator[1]))
            not_now_button = NotNowButtonElement(button)
            not_now_button.click(self.driver)
            # print("done!")
        except TimeoutError:
            # print("didn't close.")
            CONTINUE

    def get_posts(self):
        """
        Gets the important information for the posts
        """
        self.posts = super().get_posts(HomePageLocators.POSTS, ScrollPostLocators.BUTTONS, ScrollPostLocators.LIKE_BUTTON, ScrollPostLocators.COMMENT_BUTTON, ScrollPostLocators.ACCOUNT_LINK)
        return self.posts

    def get_like_buttons(self):
        """
        Returns the like buttons on the page
        """
        return [button for i, button in enumerate(self.get_buttons()) if i % 6 == ScrollPostLocators.LIKE_BUTTON]

    def is_title_matches(self):
        """Verifies that the hardcoded text "Instagram" appears in page title"""

        return "Instagram" in self.driver.title

    def load_more_posts(self):
        self.scroll()
        self.posts = self.get_posts()