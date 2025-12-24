from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        a_title = self.browser.find_element(By.XPATH, "//*[text()='HTC Touch HD']")
        assert a_title.text == title