from abc import ABC

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import time

from like_button_element import LikeButtonElement
from comment_box_element import CommentBoxElement
from post_element import PostElement

from account_link_tag_element import AccountLinkTagElement


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