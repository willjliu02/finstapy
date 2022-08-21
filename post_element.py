from base_page_element import BasePageElement
from like_button_element import LikeButtonElement
from comment_box_element import CommentBoxElement
from account_link_tag_element import AccountLinkTagElement

class PostElement(BasePageElement):
    """
    PostElement gets a specific Post as a WebElement
    """
    def __init__(self, element, like_button: LikeButtonElement, comment_box: CommentBoxElement, acc_link_tag: AccountLinkTagElement, moreButton = None) -> None:
        super().__init__(element)
        self.like_button = like_button
        self.comment_box = comment_box
        self.acc_link_tag = acc_link_tag

    def get_likes(self):
        """
        Gets the number of likes on the post
        """
        text = self.get_post_text()
        divided_text = text.split()
        number_index = self.find_likes(divided_text) #inclusive
        broken_like_count = divided_text[number_index].split(",")
        tens = len(broken_like_count)
        likes = 0
        for i in range(tens):
            likes += broken_like_count[i] * 10**(3*(tens - i - 1))
        return likes

    def find_likes(self, lst_words):
        for i, word in enumerate(lst_words):
            if word == "likes" or word == "views":
                return i-1
            elif word == "Liked":
                return i + 4
        return -1

    def go_to_account_page(self, driver):
        """
        Retrieves the account page
        """
        self.acc_link_tag.click(driver)

    def like_post(self, driver) -> bool:
        """
        Likes the likeButton attribute
        """
        return self.like_button.click(driver)

    def get_post_text(self) -> str:
        """
        Gets all the text from the post
        """
        return self.element.text

    def has_desired_hashtags(self, hashtags = []):
        """
        Returns how many of the desired hashtags are in the caption
        """
        pass

    def comment(self, comment):
        """
        Commments in the comment section
        """