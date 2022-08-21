from selenium.webdriver.common.by import By

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