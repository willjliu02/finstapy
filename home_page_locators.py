from selenium.webdriver.common.by import By

class HomePageLocators:
    """
    A class for main page locators. All main page locators should come here
    """

    NOT_NOW_BUTTON = (By.CSS_SELECTOR, "button._a9--._a9_1")

    POSTS = (By.CSS_SELECTOR, "article._ab6k._ab6l._ab6m._aatb._aatc._aate._aatf._aath._aati")