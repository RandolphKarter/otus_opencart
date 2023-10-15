import random
import allure
from pages.MainPage import MainPage
from pages.ProductCardPage import ProductCardPage


@allure.tag('Smoke', 'UI')
@allure.feature('Product cart page')
@allure.story('Button cart')
@allure.title('Test visibility of cart button')
def test_product_card_page_button_cart(driver, url):
    """Test visibility of cart button"""
    MainPage(driver).open(url)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    assert ProductCardPage(driver).get_button_cart_text() == 'Add to Cart'


@allure.tag('Smoke', 'UI')
@allure.feature('Product cart page')
@allure.story('Thumbnails')
@allure.title('Test visibility of thumbnails')
def test_product_card_page_thumbnails(driver, url):
    """Test visibility of thumbnails"""
    MainPage(driver).open(url)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    featured_product_name = ProductCardPage(driver).get_product_name()
    thumbnails_list = ProductCardPage(driver).get_thumbnails_list()
    assert featured_product_name in [element.get_attribute('title') for element in thumbnails_list]


@allure.tag('Smoke', 'UI')
@allure.feature('Product cart page')
@allure.story('Breadcrumb')
@allure.title('Test visibility of breadcrumb')
def test_product_card_page_breadcrumb(driver, url):
    """Test visibility of breadcrumb"""
    MainPage(driver).open(url)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    featured_product_name = ProductCardPage(driver).get_product_name()
    current_breadcrumb = ProductCardPage(driver).get_current_breadcrumb_text()
    assert featured_product_name in current_breadcrumb


@allure.tag('Smoke', 'UI')
@allure.feature('Product cart page')
@allure.story('Review button')
@allure.title('Test visibility of review button')
def test_product_card_page_review_button(driver, url):
    """Test visibility of review button"""
    MainPage(driver).open(url)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    ProductCardPage(driver).review_tab_click()
    assert 'Continue' in ProductCardPage(driver).get_review_button_text()


@allure.tag('Smoke', 'UI')
@allure.feature('Product cart page')
@allure.story('Description tab')
@allure.title('Test visibility of description tab')
def test_product_card_page_description_tab(driver, url):
    """Test visibility of description tab"""
    MainPage(driver).open(url)
    MainPage(driver).featured_product_click(random.randint(0, 3))
    assert 'Description' in ProductCardPage(driver).get_description_tab_text()
