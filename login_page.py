from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from base_page import BasePage

from login_page_locators import LoginPageLocators

from username_bar_element import UsernameBarElement
from password_bar_element import PasswordBarElement
from login_button_element import LoginButtonElement


class LoginPage(BasePage):
    """
    Represents the Login Page
    """

    def log_in(self, username, password):
        """
        Logs into the account
        """
        try:
            locator = LoginPageLocators.USERNAME_BAR
            userElement = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element(locator[0], locator[1]))
            username_bar = UsernameBarElement(userElement)  # Enters the username
            username_bar.enter_username(username)

            locator = LoginPageLocators.PASSWORD_BAR
            pwElement = WebDriverWait(self.driver, 15).until(
                    lambda driver: driver.find_element(locator[0], locator[1]))
            password_bar = PasswordBarElement(pwElement)  # Enters the password
            password_bar.enter_password(password)
        except TimeoutException:
            self.driver.quit()

    def click_login(self):
        """
        Clicks on the login button
        """
        locator = LoginPageLocators.LOG_IN_BUTTON
        button = self.driver.find_element(locator[0], locator[1])
        login_button = LoginButtonElement(button)
        login_button.click(self.driver)