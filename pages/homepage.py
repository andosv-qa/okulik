from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
       self. browser.get('https://ecommerce-playground.lambdatest.io/index.php?route=common/home')

    def click_htc(self):
        htc = self.browser.find_element(By.LINK_TEXT, 'HTC Touch HD')
        htc.click()

    def click_monitor(self):
        windows_link = self.browser.find_element(By.LINK_TEXT, 'Windows')
        windows_link.click()

    def check_product_count(self, count):
        winds = self.browser.find_elements(By.CSS_SELECTOR, '.product-thumb')
        assert len(winds) == count
