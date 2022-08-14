from element import BasePageElement
from element import SearchTextElement
from locators import HomePageLocators


class BasePage:
    """
    Represents the basic building block of what a page is.
    """

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    """
    Represents the home page, where the users' feed typically is.
    """

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Instagram" appears in page title"""

        return "Instagram" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*HomePageLocators.GO_BUTTON)
        element.click()

class DiscoverPage(BasePage):
    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

class AccountPage(BasePage):
    pass

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source