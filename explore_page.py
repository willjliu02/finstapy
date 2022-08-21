from base_page import BasePage

from explore_page_locators import ExplorePageLocators
from recommended_hashtag_element import RecommendedHashtagElement

class ExplorePage(BasePage):
    """
    Represents the explore page on Instagram.
    """

    def select_hashtag(self, target_hashtags):
        """
        Chooses one of the recommended hashtags

        Args:
            target_hashtags(list[str]): A list of the desired hashtags as strings

        Output:
            __(bool): True if a hashtag is selected, False if not
        """
        hashtags = self.select_hashtag()

        for hashtag in hashtags:
            if target_hashtags.find(hashtag) != -1:
                return hashtag.click(self.driver)

        return False

    def get_hasthtags(self):
        """
        Gets the recommended hashtags
        """
        locator = ExplorePageLocators.REC_HASHTAGS
        list_of_hashtags = self.driver.find_all_elements(locator[0], locator[1])
        return list(map(lambda hashtag: RecommendedHashtagElement(hashtag), list_of_hashtags))