from element import RealPostElement
from element import PicturePostElement
from element import VideoPostElement
from element import SearchTextElement
from locators import HomePageLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import TimeOutException

class BasePage:
    """
    Represents the basic building block of what a page is.
    """

    def __init__(self, driver:webdriver):
        self.driver = driver

    def scroll(self):
        """
        Scrolls through the page to load more posts
        """
        scroller = ActionChains(self.driver)
        
        scroller.scroll_by_amount(0, 50)

    def click(self, element):
        element.click()


class HomePage(BasePage):
    """
    Represents the home page, where the users' feed typically is.
    """

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Instagram" appears in page title"""

        return "Instagram" in self.driver.title

    def get_posts(self):
        """
        Gets the posts that have loaded on the page.
        """
        try:
            posts = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_all_elements(HomePageLocators.POSTS))
        except TimeOutException:
            posts = []

        return posts

class ExplorePage(BasePage):
    """
    Represents the explore page on Instagram.
    """
    


class AccountPage(BasePage):
    """
    Represents the AccountPage of some account
    """

    def follow(self):
        """
        Follows the account
        """
        pass
    def check_following(self):
        """
        Returns the number of followers that the account has
        """
        pass

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source