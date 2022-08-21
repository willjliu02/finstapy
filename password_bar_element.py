from base_page_element import BasePageElement

class PasswordBarElement(BasePageElement):
    """
    Represents the Password Bar
    """

    def enter_password(self, password):
        self.element.send_keys(password)