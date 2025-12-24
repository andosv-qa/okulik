
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_htc(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_htc()
    product_page = ProductPage(browser)
    product_page.check_title_is('HTC Touch HD')

def test_windows(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    homepage.check_product_count(15)
