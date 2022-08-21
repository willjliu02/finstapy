from base_page import BasePage

from follow_button_element import FollowButtonElement

from account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    """
    Represents the AccountPage of some account
    """

    def follow(self):
        """
        Follows the account
        """
        locator = AccountPageLocators.FOLLOW_BUTTON
        button = self.driver.find_element(locator[0], locator[1])
        follow_button = FollowButtonElement(button)
        follow_button.click(self.driver)

    def get_follower_count(self):
        """
        Returns the number of followers that the account has
        """
        locator = AccountPageLocators.POST_FOLLOWER_FOLLOWING
        account_info = self.driver.find_all_elements(locator[0], locator[1])
        follower_count = account_info[AccountPageLocators.FOLLOWERS].getAttribute("title").split(",")
        tens = len(follower_count)
        followers = 0
        for i in range(tens):
            followers += follower_count[i] * 10**(3*(tens - i - 1))
        return followers