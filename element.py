from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from abc import ABC

class BasePageElement():
    """Base page class that is initialized on every page object class."""

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

class CommentSectionElement(BasePageElement):
    """
    CommentSectionElement a reference to the comment section as as whole
    """
    
    def get_caption(self):
        """
        Gets the caption of the post
        """
        pass

    def has_desired_hashtags(self, hashtags = []):
        """
        Counts how many of the desired hashtags the post has
        """
        pass

class PostElement(BasePageElement, ABC):
    """
    PostElement gets a specific Post as a WebElement
    """
    def __init__(self, driver, likeButton: LikeButtonElement, commentSection: CommentSectionElement) -> None:
        self.likeButton = likeButton
        self.commentSection = commentSection

    def like_post(self) -> bool:
        """
        Likes the likeButton attribute
        """
        pass

    def get_caption(self) -> str:
        """
        Gets the caption for the post
        """
        pass

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

class VideoElement(PostElement):
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