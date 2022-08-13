from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FinstaPy:
    """
    Is an Instagram Bot that helsp to make accounts maintain relevancy
    """

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

        PATH = "/Users/williamliu/Desktop/College/Summer 2 2022/EECE 2140/finstapy/chromedriver"
        self.browser = webdriver.Chrome(PATH)

        self.browser.get('https://www.instagram.com')
        assert 'Instagram' in self.browser.title

    def log_in(self):
        username_bar = self.browser.find_element(By.NAME, 'username')  # Enters the username
        username_bar.send_keys(self.username + Keys.TAB)

        password_bar = self.browser.find_element(By.NAME, "password")  # Enters the username
        password_bar.send_keys(self.password + Keys.RETURN)

    def dismiss_notification(self):
        alert = self.browser.switch_to.alert()
        self.browser.close(alert)

    def find_hashtag(self, hashtag):
        search = self.browser.find_element(By.TAG_NAME, "input")
        search.send_keys("#" + hashtag + Keys.RETURN)

    def quit(self):
        print("Logging out.")
        self.browser.quit()
