from http.client import CONTINUE
from element import AccountLinkTagElement, CommentBoxElement, FollowButtonElement
from element import SaveInfoButtonElement
from element import NotNowButtonElement
from element import LikeButtonElement
from element import LoginButtonElement
from element import PostElement
from element import PicturePostElement
from element import VideoPostElement
from element import SearchTextElement
from element import UsernameBarElement
from element import PasswordBarElement
from element import RecommendedHashtagElement
from element import SaveInfoButtonElement

from locators import AccountPageLocators
from locators import ExplorePageLocators
from locators import ScrollPostLocators
from locators import ScrollPostLocators
from locators import LoginPageLocators
from locators import HomePageLocators
from locators import SaveInfoPageLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
from abc import ABC

import time

class BasePage(ABC):
    """
    Represents the basic building block of what a page is.
    """

    def __init__(self, driver:webdriver):
        self.driver = driver

    def get_posts(self, postLocator, button_locator, like_button_locator, comment_box_locator, acc_link_tag_locator):
        """
        Retrieves the posts loaded on the page
        """
        time.sleep(10)
        # while True:
        try:
            posts = WebDriverWait(self.driver, 30).until(
                    lambda driver: driver.find_elements(postLocator[0], postLocator[1]))
            
        except TimeoutException:
            posts = []
            print("the exception did go off")

        buttons = self.get_buttons(button_locator)
        like_buttons = []
        comment_boxes = []
        acc_link_tags = self.get_account_tags(acc_link_tag_locator)
        for i, button in enumerate(buttons):
            buttonType = i % 6
            if buttonType == like_button_locator:
                like_buttons.append(LikeButtonElement(button))
            elif buttonType == comment_box_locator:
                comment_boxes.append(CommentBoxElement(button))

        num_posts = len(posts)
        num_like_buttons = len(like_buttons)
        num_comment_boxes = len(comment_boxes)
        num_acc_link_tag = len(acc_link_tags)

        print(f"{num_posts} posts found")
        print(f"{num_like_buttons} like_buttons found")
        print(f"{num_comment_boxes} comment_boxes found")
        print(f"{num_acc_link_tag} acc_link_tags found")

            # if num_posts == num_like_buttons == num_comment_boxes == num_acc_link_tag:
            #     break

        post_params = zip(posts, like_buttons, comment_boxes, acc_link_tags)
        post_elements = list(map(lambda tup: PostElement(tup[0], tup[1], tup[2], tup[3]), post_params))

        return post_elements


    def get_buttons(self, locator):
        """
        Retrieves the buttons on the screen
        """
        try:
            buttons = WebDriverWait(self.driver, 30).until(
                    lambda driver: driver.find_elements(locator[0], locator[1]))
        except TimeoutException:
            buttons = []

        return buttons

    def get_account_tags(self, locator):
        """
        Retrieves the location for the account name's and the path to their account pages
        """

        try:
            account_link_tags = WebDriverWait(self.driver, 30).until(
                    lambda driver: driver.find_elements(locator[0], locator[1]))
        except TimeoutException:
            account_link_tags = []

        return list(map(lambda tag: AccountLinkTagElement(tag), account_link_tags))


    def get_likes(self, locator):
        """
        Retrieves the number of likes for each post
        """
        try:
            by, value = locator
            like_counts = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_elements(locator[0], locator[1]))
        except TimeoutException:
            like_counts = []

        return like_counts


    def scroll(self, element):
        """
        Scrolls through the page to load more posts
        """
        scroller = ActionChains(self.driver)
        origin = ScrollOrigin(element, 0, 0)
        scroller.scroll_from_origin(origin, 0, 100)
        scroller.perform()

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
        try:
            locator = LoginPageLocators.USERNAME_BAR
            userElement = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element(locator[0], locator[1]))
            username_bar = UsernameBarElement(userElement)  # Enters the username
            username_bar.enter_username(username)

            locator = LoginPageLocators.PASSWORD_BAR
            pwElement = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element(locator[0], locator[1]))
            password_bar = PasswordBarElement(pwElement)  # Enters the password
            password_bar.enter_password(password)
        except TimeoutException:
            self.driver.quit()

    def click_login(self):
        """
        Clicks on the login button
        """
        locator = LoginPageLocators.LOG_IN_BUTTON
        button = self.driver.find_element(locator[0], locator[1])
        login_button = LoginButtonElement(button)
        login_button.click(self.driver)

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
        locator = ExplorePageLocators.REC_HASHTAGS
        list_of_hashtags = self.driver.find_all_elements(locator[0], locator[1])
        return list(map(lambda hashtag: RecommendedHashtagElement(hashtag), list_of_hashtags))


class AccountPage(BasePage):
    """
    Represents the AccountPage of some account
    """

    def follow(self):
        """
        Follows the account
        """
        locator = AccountPageLocators.FOLLOW_BUTTON
        button = self.driver.find_element(locator[0], locator[1])
        follow_button = FollowButtonElement(button)
        follow_button.click(self.driver)

    def get_follower_count(self):
        """
        Returns the number of followers that the account has
        """
        locator = AccountPageLocators.POST_FOLLOWER_FOLLOWING
        account_info = self.driver.find_all_elements(locator[0], locator[1])
        follower_count = account_info[AccountPageLocators.FOLLOWERS].getAttribute("title").split(",")
        tens = len(follower_count)
        followers = 0
        for i in range(tens):
            followers += follower_count[i] * 10**(3*(tens - i - 1))
        return followers
        

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source