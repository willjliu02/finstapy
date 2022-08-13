from http.client import CONTINUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class FinstaPy:
    """
    Is an Instagram Bot that helsp to make accounts maintain relevancy
    """

    def __init__(self, username, password, comments = []) -> None:
        self.username = username
        self.password = password
        self.comments = comments

        PATH = "/Users/williamliu/Desktop/College/Summer 2 2022/EECE 2140/finstapy/chromedriver"
        self.browser = webdriver.Chrome(PATH)

        self.browser.get('https://www.instagram.com')
        assert 'Instagram' in self.browser.title

    def log_in(self):
        username_bar = self.browser.find_element(By.NAME, 'username')  # Enters the username
        username_bar.send_keys(self.username + Keys.TAB)

        password_bar = self.browser.find_element(By.NAME, "password")  # Enters the username
        password_bar.send_keys(self.password + Keys.RETURN)

    def dismiss_notification(self):
        try:
            alert = self.browser.switch_to.alert()
            self.browser.close(alert)
        except NoSuchElementException:
            CONTINUE

    def search_hashtag(self, hashtag):
        search = self.browser.find_element(By.TAG_NAME, "input")
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

    def like_photo(self, element, freq = 0.7):
        """
        Likes the given element, frequency % of the time

        Args:
            element(WebElement): The element that is to be liked
            freq(float): How often the post is liked
        
        Output:
            __(bool): If the post is liked
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
        self.browser.quit()
