from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from abc import ABC

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

class UsernameBarElement(BasePageElement):
    """
    Represents the Username Bar
    """

    def enter_username(self, username):
        self.element.send_keys(username)

class PasswordBarElement(BasePageElement):
    """
    Represents the Password Bar
    """

    def enter_password(self, password):
        self.element.send_keys(password)

class LoginButtonElement(BasePageElement):
    """
    Represents the Login Button
    """

class SaveInfoButtonElement(BasePageElement):
    """
    Represents the Save Info Button after the Login Page
    """

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = (By.XPATH, "//input")

class LikeButtonElement(BasePageElement):
    """
    LikeButtonElement is an object created for the actual like button of an article
    """
    
    def like_post(self):
        """
        Clicks on the like button
        """

class CommentBoxElement(BasePageElement):
    """
    CommentBoxElement a reference to the comment section as as whole
    """
    
    def comment(self, comment):
        """
        Comments on the post
        """
        pass

    def posts_comment(self, driver):
        """
        Clicks on the post button for the comment
        """
        pass

    def has_desired_hashtags(self, hashtags = []):
        """
        Counts how many of the desired hashtags the post has
        """
        pass

class AccountLinkTagElement(BasePageElement):
    """
    Represents the name of the account as well as the link to the account page
    """

class PostElement(BasePageElement):
    """
    PostElement gets a specific Post as a WebElement
    """
    def __init__(self, element, like_button: LikeButtonElement, comment_box: CommentBoxElement, acc_link_tag: AccountLinkTagElement, moreButton = None) -> None:
        super.__init__(element)
        self.like_button = like_button
        self.comment_box = comment_box
        self.acc_link_tag = acc_link_tag

    def get_likes(self):
        """
        Gets the number of likes on the post
        """
        text = self.get_post_text()
        divided_text = text.split()
        number_index = self.find_likes(divided_text) #inclusive
        broken_like_count = divided_text[number_index].split(",")
        tens = len(broken_like_count)
        likes = 0
        for i in range(tens):
            likes += broken_like_count[i] * 10**(3*(tens - i - 1))
        return likes

    def find_likes(self, lst_words):
        for i, word in enumerate(lst_words):
            if word == "likes" or word == "views":
                return i-1
            elif word == "Liked":
                return i + 4
        return -1

    def go_to_account_page(self, driver):
        """
        Retrieves the account page
        """
        self.acc_link_tag.click(driver)

    def like_post(self, driver) -> bool:
        """
        Likes the likeButton attribute
        """
        self.like_button.click(driver)

    def get_post_text(self) -> str:
        """
        Gets all the text from the post
        """
        return self.element.text

    def has_desired_hashtags(self, hashtags = []):
        """
        Returns how many of the desired hashtags are in the caption
        """
        pass

    def comment(self, comment):
        """
        Commments in the comment section
        """

class PicturePostElement(PostElement):
    """
    Represents a PostElement with just pictures
    """

    def has_multiple_pictures(self):
        """
        Returns how many pictures the post has
        """
        pass

class VideoPostElement(PostElement):
    """
    Represents a PostElement with a Real or IGTV
    """
    
    def watch_real(self):
        """
        Gets the duration of the real and sleeps until the video finishes
        """
        pass

    def get_duration(self):
        """
        Gets the length of the video
        """
        pass

class RecommendedHashtagElement(BasePageElement):
    """
    Represents one of the recommended hashtags on the explore page
    """

class FollowButtonElement(BasePageElement):
    """
    Represents the follow button on the Account Pages
    """

    def click(self, driver):
        if self.element.text == "Follow":
            super().click(driver)
        return True