from base_page_element import BasePageElement

class UsernameBarElement(BasePageElement):
    """
    Represents the Username Bar
    """

    def enter_username(self, username):
        self.element.send_keys(username)