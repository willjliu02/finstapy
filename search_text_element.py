from base_page_element import BasePageElement

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = (By.XPATH, "//input")