from http.client import CONTINUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from page import *
from locators import *

import random

import time

class FinstaPy:
    """
    Is an Instagram Bot that helps to make accounts maintain relevancy
    """

    def __init__(self, username, password, comments = [], hashtags = []) -> None:
        PATH = "/Users/williamliu/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.hashtags = hashtags
        self.comments = comments

        self.driver.get('https://www.instagram.com')
        loginPage = LoginPage(self.driver)
        loginPage.log_in(username, password)
        loginPage.click_login()

        saveInfoPage = SaveInfoPage(self.driver)
        saveInfoPage.click_button()

        time.sleep(3)

    def dismiss_notification(self):
        try:
            alert = self.driver.switch_to.alert()
            self.browser.close(alert)
        except NoSuchElementException:
            CONTINUE
        # try:
        #     locator = locators.PopUpLocators.SAVE_INFO_BUTTON
        #     button = WebDriverWait(self.driver, 15).until(
        #             lambda driver: driver.find_element(locator[0], locator[1]))
        #     saveInfoButton = SaveInfoButtonElement(button)
        #     saveInfoButton.click(self.driver)
        # except TimeoutException:
        #     print("Did not see the pop-up")
        #     self.driver.quit()

    def go_to_home_page(self):
        """
        Goes to the Home Page
        """
        
        self.driver.get("https://www.instagram.com")
        self.homePage = HomePage(self.driver)
        self.homePage.close_notification_alert()
        return self.homePage
    
    def view_page(self, page_to_view, like_freq = 0.7, desired_like_follower_ratio = 0.35):
        time.sleep(3)
        liked = 0
        commented = 0
        followed = 0
        posts = page_to_view.get_posts()
        for post in posts:
            has_desired_hashtag = self.has_hashtag(post)
            if self.like_post(post, like_freq, has_desired_hashtag):
                liked += 1
            if self.comment_on_post(post, has_desired_hashtag):
                commented += 1
            if self.follow_account(post, desired_like_follower_ratio, has_desired_hashtag):
                followed += 1
        self.scroll_page(page_to_view, posts[-1]._get_element()) #element becomes the 4th loaded article
        print(f"\nLiked: {liked}\nCommented on: {commented}\nFollowed: {followed}\nOut of {len(posts)} posts")

    def viewExplorePage(self, like_freq = 0.7, desired_like_follower_ratio = 0.35):
        explorePage = ExplorePage(self.driver)
        posts = explorePage.get_posts()
        for post in posts:
            has_desired_hashtag = self.has_hashtag(post)
            self.like_post(post, like_freq, has_desired_hashtag)
            self.comment_on_post(post, has_desired_hashtag)
            self.follow_account(post, desired_like_follower_ratio, has_desired_hashtag)
        # self.scroll_page(explorePage, posts[-1]._get_element()) #element becomes the 4th loaded article
            
    def has_hashtag(self, post):
        """
        Checks if the post has a hashtag the account would look for
        """
        post_text = post.get_post_text()
        post_hashtags = set([word for word in post_text.split() if "#" in word])
        for hashtag in post_hashtags:
            if hashtag in self.hashtags:
                return True
        return False

    def like_post(self, post, freq, has_hashtag = False, has_hashtag_like_bonus = 0.1):
        """
        Likes the given element, frequency % of the time

        Args:
            post(WebElement): The element that is to be liked
            freq(float): How often the post is liked
        
        Output:
            __(bool): If the post is liked
        """
        probability = random.random()
        if has_hashtag and probability < (freq + has_hashtag_like_bonus) or probability < freq:
            post.like_post(self.driver)
            return True
        return False

    def comment_on_post(self, post, has_hashtag = False):
        """
        Comments on the post
        """
        if has_hashtag:
            comment = random.choice(self.comments)
            post.comment(comment)
            return True
        return False
        
    def follow_account(self, post, desired_like_follower_ratio, has_hashtag = False):
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

        if not has_hashtag:
            return False

        post.go_to_account_page(self.driver)
        accountPage = AccountPage(self.driver)
        follower_count = accountPage.get_follower_count()

        like_follower_ratio = post.get_likes()/follower_count
        
        if like_follower_ratio > desired_like_follower_ratio:
            accountPage.follow()
            return True
        return False

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

    def get_caption(self, post):
        """
        Gets the caption to the specific post

        Args:
            post(WebElement): A reference to the actual post

        Output:
            caption(str): The caption to the post
        """
        pass

    def scroll_page(self, page, element):
        """
        Scrolls down the page to load more posts and then pauses to allow it to load

        Args:

        Output:

        """
        page.scroll(element)

    def click(self, element):
        pass

    def quit(self):
        print("Logging out.")
        self.driver.quit()
