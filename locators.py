from lib2to3.pgen2.token import COMMENT
from pickle import NONE
from selenium.webdriver.common.by import By

class HomePageLocators:
    """
    A class for main page locators. All main page locators should come here
    """

    GO_BUTTON = (By.ID, 'submit')
    POSTS = (By.XPATH, "//article")

class HomePostLocators:
    """
    A class that contains all the locators for a specific HomePage's PostElement
    """

    """
    "more settings", (more info), (link arrow to get more info), like button, comment button, share, save, emoji
    CSS_SELECTOR = "button._abl-"
    """
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a.oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _acan _acao _acat _acaw _a6hd")
    BUTTONS = (By.CSS_SELECTOR, "button._abl-")
    MORE_SETTINGS = 0
    LIKE_BUTTON = 1
    COMMENT_BUTTON = 2
    SHARE_BUTTON = 3
    SAVE_BUTTON = 4
    EMOJI_BUTTON = 5


class OtherPostLocators:
    """
    A class that contains all the locators for a specific HomePage's PostElement
    """
    pass

class SearchResultsPageLocators:
    """A class for search results locators. All search results locators should
    come here
    """

    POSTS = ()

class AccountPageLocators:
    """
    A class for all the account page locators.
    """
    FOLLOW_BUTTON = ()
    FOLLOWERS_COUNT = ()
    POSTS = ()
