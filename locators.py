from lib2to3.pgen2.token import COMMENT
from pickle import NONE
from selenium.webdriver.common.by import By

class LoginPageLocators:
    """
    Holds all the locators for the login page
    """

    USERNAME_BAR = (By.NAME, 'username')
    PASSWORD_BAR = (By.NAME, "password")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button.sqdOP.L3NKy.y3zKF")

class SaveInfoPageLocators:
    """
    Holds the locator for the pop up window after login
    """
    SAVE_INFO_BUTTON = (By.CSS_SELECTOR, "button.sqdOP.L3NKy.y3zKF")

class HomePageLocators:
    """
    A class for main page locators. All main page locators should come here
    """

    NOT_NOW_BUTTON = (By.CSS_SELECTOR, "button._a9--._a9_1")

    POSTS = (By.CSS_SELECTOR, "article._ab6k._ab6l._ab6m._aatb._aatc._aate._aatf._aath._aati")

class ScrollPostLocators:
    """
    A class that contains all the locators for a specific HomePage's PostElement
    """

    """
    "more settings", (more info), (link arrow to get more info), like button, comment button, share, save, emoji
    CSS_SELECTOR = "button._abl-"
    """
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._acan._acao._acat._acaw._a6hd")
    BUTTONS = (By.CSS_SELECTOR, "button._abl-")
    OPTIONS = 0 #indices
    LIKE_BUTTON = 1
    COMMENT_BUTTON = 2
    SHARE_BUTTON = 3
    SAVE_BUTTON = 4
    EMOJI_BUTTON = 5
    # LIKE_COUNT = (By.CSS_SELECTOR, "div._aacl._aaco._aacw._adda._aacx._aada._aade")
    CAPTION_MORE_BUTTON = (By.CSS_SELECTOR, "div._aacl._aaco._aacu._aacx._aad7._aade")


class OtherPostLocators:
    """
    A class that contains all the locators for a specific HomePage's PostElement
    """
    pass

class ExplorePageLocators:
    """
    A class for the locators on the explore page
    """

    REC_HASHTAGS = ()

class SearchResultsPageLocators:
    """A class for search results locators. All search results locators should
    come here
    """

    POSTS = ()

class AccountPageLocators:
    """
    A class for all the account page locators.
    """
    FOLLOW_BUTTON = (By.CSS_SELECTOR, "button._acan _acap _acas")
    POST_FOLLOWER_FOLLOWING = (By.CSS_SELECTOR, "span._ac2a")
    FOLLOWERS = 1 #index 1, title info
    POSTS = ()
