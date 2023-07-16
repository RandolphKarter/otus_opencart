import random
from pages.MainPage import MainPage
from pages.ProductCardPage import ProductCardPage


def test_product_card_page_button_cart(driver, url, port):
    MainPage(driver).open(url, port)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    assert ProductCardPage(driver).get_button_cart_text() == 'Add to Cart'


def test_product_card_page_thumbnails(driver, url, port):
    MainPage(driver).open(url, port)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    featured_product_name = ProductCardPage(driver).get_product_name()
    thumbnails_list = ProductCardPage(driver).get_thumbnails_list()
    assert featured_product_name in [element.get_attribute('title') for element in thumbnails_list]


def test_product_card_page_breadcrumb(driver, url, port):
    MainPage(driver).open(url, port)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    featured_product_name = ProductCardPage(driver).get_product_name()
    current_breadcrumb = ProductCardPage(driver).get_current_breadcrumb_text()
    assert featured_product_name in current_breadcrumb


def test_product_card_page_review_button(driver, url, port):
    MainPage(driver).open(url, port)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    ProductCardPage(driver).review_tab_click()
    assert 'Continue' in ProductCardPage(driver).get_review_button_text()


def test_product_card_page_description_tab(driver, url, port):
    MainPage(driver).open(url, port)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    assert 'Description' in ProductCardPage(driver).get_description_tab_text()
