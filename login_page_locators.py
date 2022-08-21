from selenium.webdriver.common.by import By

class LoginPageLocators:
    """
    Holds all the locators for the login page
    """

    USERNAME_BAR = (By.NAME, 'username')
    PASSWORD_BAR = (By.NAME, "password")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button.sqdOP.L3NKy.y3zKF")