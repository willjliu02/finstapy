from element import LoginButtonElement
from element import PicturePostElement
from element import VideoPostElement
from element import SearchTextElement
from element import UsernameBarElement
from element import PasswordBarElement
from element import RecommendedHashtagElement

from locators import AccountPageLocators, ExplorePageLocators
from locators import ScrollPostLocators
from locators import LoginPageLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import TimeOutException
from abc import ABC

class BasePage(ABC):
    """
    Represents the basic building block of what a page is.
    """

    def __init__(self, driver:webdriver):
        self.driver = driver

    def get_posts(self, locator = ""):
        """
        Retrieves the posts loaded on the page
        """

        try:
            posts = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_all_elements(locator))
        except TimeOutException:
            posts = []

        return posts

    def get_buttons(self):
        """
        Retrieves the buttons on the screen
        """
        pass

    def scroll(self):
        """
        Scrolls through the page to load more posts
        """
        scroller = ActionChains(self.driver)
        scroller.scroll_by_amount(0, 50)

    def click_on(self, element):
        element.click(self.driver)

class LoginPage(BasePage):
    """
    Represents the Login Page
    """

    def log_in(self, username, password):
        """
        Logs into the account
        """
        userElement = self.driver.find_element(LoginPageLocators.USERNAME_BAR)
        username_bar = UsernameBarElement(userElement)  # Enters the username
        username_bar.enter_username(username)

        pwElement = self.driver.find_element(LoginPageLocators.PASSWORD_BAR)
        password_bar = PasswordBarElement(pwElement)  # Enters the username
        password_bar.enter_password(password)

    def click_login(self):
        """
        Clicks on the login button
        """
        button = self.driver.find_element(LoginPageLocators.LOG_IN_BUTTON)
        login_button = LoginButtonElement(button)
        login_button.click(self.driver)

class HomePage(BasePage):
    """
    Represents the home page, where the users' feed typically is.
    """

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def get_posts(self):
        """
        Gets the posts that have loaded on the page.
        """
        return super.get_posts(ScrollPostLocators.POSTS)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Instagram" appears in page title"""

        return "Instagram" in self.driver.title

    

class ExplorePage(BasePage):
    """
    Represents the explore page on Instagram.
    """

    def select_hashtag(self, target_hashtags):
        """
        Chooses one of the recommended hashtags

        Args:
            target_hashtags(list[str]): A list of the desired hashtags as strings

        Output:
            __(bool): True if a hashtag is selected, False if not
        """
        hashtags = self.select_hashtag()

        for hashtag in hashtags:
            if target_hashtags.find(hashtag) != -1:
                return hashtag.click(self.driver)

        return False

    def get_hasthtags(self):
        """
        Gets the recommended hashtags
        """

        list_of_hashtags = self.driver.find_all_elements(ExplorePageLocators.REC_HASHTAGS)
        return list(map(lambda hashtag: RecommendedHashtagElement(hashtag), list_of_hashtags))


class AccountPage(BasePage):
    """
    Represents the AccountPage of some account
    """

    def follow(self):
        """
        Follows the account
        """
        follow_button = self.driver.find_element(AccountPageLocators.FOLLOW_BUTTON)
        
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