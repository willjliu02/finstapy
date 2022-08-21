from selenium.webdriver.common.by import By

class AccountPageLocators:
    """
    A class for all the account page locators.
    """
    FOLLOW_BUTTON = (By.CSS_SELECTOR, "button._acan _acap _acas")
    POST_FOLLOWER_FOLLOWING = (By.CSS_SELECTOR, "span._ac2a")
    FOLLOWERS = 1 #index 1, title info
    POSTS = ()