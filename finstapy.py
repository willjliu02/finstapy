from http.client import CONTINUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import page
import element
import locators

from random import Random

class FinstaPy:
    """
    Is an Instagram Bot that helps to make accounts maintain relevancy
    """

    def __init__(self, username, password, comments = [], hashtags = []) -> None:
        PATH = "/Users/williamliu/chromedriver"
        self.driver = webdriver.Chrome(PATH)

        self.driver.get('https://www.instagram.com')
        loginPage = page.LoginPage(self.driver)
        loginPage.log_in(username, password)
        loginPage.click_login()
        self.dismiss_notification()

    def scrollHomePage(self):
        homePage = page.HomePage(self.driver)
        for post in homePage.get_posts():
            self.like_post(post)

    def like_post(self, post, freq = 0.7):
        """
        Likes the given element, frequency % of the time

        Args:
            post(WebElement): The element that is to be liked
            freq(float): How often the post is liked
        
        Output:
            __(bool): If the post is liked
        """
        if Random.next() < freq:
            post.like_post(self.driver)
            return True
        return False

    def dismiss_notification(self):
        try:
            alert = self.driver.switch_to.alert()
            self.browser.close(alert)
        except NoSuchElementException:
            CONTINUE

    def search_hashtag(self, hashtag):
        search = self.driver.find_element(By.TAG_NAME, "input")
        search.send_keys("#" + hashtag + Keys.RETURN)

    def search_location(self, location):
        pass


    def watch_real(self, real):
        """
        Watches the entire Instagram real with a delay.

        Args:
            real(WebElement): The web element that interacts with the real

        Output:
            __(bool): A true after the real has been watched
        """
        pass

    def add_comment(self, comment):
        self.comments.append(comment)

    def comment_photo(self, comment = ""):
        pass

    def get_caption(self, post):
        """
        Gets the caption to the specific post

        Args:
            post(WebElement): A reference to the actual post

        Output:
            caption(str): The caption to the post
        """
        pass

    def follow_account(self, post, account, likes_follower_ratio = 0.35):
        """
        Likes the given account if the post's like to account follower ratio is >= likes_follower_ratio

        Args:
            post(WebElement): The refernce to the post
            account(WebElement): The reference to the account
            likes_follower_ratio(float): The ratio between the likes on the post to the account's followers

        Output:
            __(bool): If the account was followed

        Note:
        post likes path: article/div/div/div/div/section/div/div/div/a/div/span link_text
        """
        like_follower_ratio = post.get_likes()/post.get_follower_count()
        pass

    def scroll_page(self):
        """
        Scrolls down the page to load more posts and then pauses to allow it to load

        Args:

        Output:

        """
        pass

    def click(self, element):
        pass

    def quit(self):
        print("Logging out.")
        self.driver.quit()
