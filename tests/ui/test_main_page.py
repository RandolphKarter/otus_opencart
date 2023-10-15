import allure
import pytest
from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu
from pages.elements.TopMenu import TopMenu
from pages.SearchPage import SearchPage


@allure.tag('Smoke', 'UI')
@allure.feature('Main page')
@allure.story('Page logo')
@allure.title('Test visibility of logo')
def test_main_page_logo(driver, url):
    """Test visibility of logo on main page"""
    MainPage(driver).open(url)
    assert MainPage(driver).get_logo_img_attr_title() == 'Your Store'


@allure.tag('Smoke', 'UI')
@allure.feature('Main page')
@allure.story('Page search')
@allure.title('Test visibility of search')
def test_main_page_search(driver, url):
    """Test visibility of search on main page"""
    MainPage(driver).open(url)
    assert MainPage(driver).get_search_input_placeholder() == 'Search'


@allure.tag('Smoke', 'UI')
@allure.feature('Main page')
@allure.story('Cart')
@allure.title('Test visibility of cart')
def test_main_page_cart(driver, url):
    """Test visibility of cart on main page"""
    MainPage(driver).open(url)
    assert MainPage(driver).get_cart()


@allure.tag('Smoke', 'UI')
@allure.feature('Main page')
@allure.story('Menu')
@allure.title('Test visibility of main menu')
def test_main_page_menu(driver, url):
    """Test visibility of main menu on main page"""
    MainPage(driver).open(url)
    assert MainMenu(driver).get_main_menu()


@allure.tag('Smoke', 'UI')
@allure.feature('Main page')
@allure.story('Slider')
@allure.title('Test visibility of slider')
def test_main_page_slider(driver, url):
    """Test visibility of slider on main page"""
    MainPage(driver).open(url)
    assert MainPage(driver).get_slider()


@allure.tag('Smoke', 'UI')
@allure.feature('Currency')
@allure.story('Change currency on a main page')
@allure.title('Test change currency')
@pytest.mark.parametrize('currency',
                         [
                             'Euro',
                             'Pound Sterling',
                             'US Dollar',
                         ])
def test_main_page_change_currency(driver, url, currency):
    """Test change currency on main page"""
    MainPage(driver).open(url)
    TopMenu(driver).choice_currency(currency)
    assert TopMenu(driver).get_currency_name()[:1] in MainPage(driver).get_featured_product_price()


@allure.tag('Smoke', 'UI')
@allure.feature('Search')
@allure.story('Search product')
@allure.title('Test search existing product')
@pytest.mark.parametrize('product',
                         [
                             'iPhone',
                             'HTC Touch HD',
                             'Samsung SyncMaster 941BW',
                             'iMac',
                             'MacBook'
                         ])
def test_search_existing_product(driver, url, product):
    """Test search existing product"""
    MainPage(driver).open(url)
    MainPage(driver).searching_the_product(product)
    assert product in SearchPage(driver).get_found_product_name()


@allure.tag('Smoke', 'UI')
@allure.feature('Search')
@allure.story('Search product')
@allure.title('Test search not existing product')
@pytest.mark.parametrize('product',
                         [
                             'Xiaomi',
                             'Lenovo',
                             'Samsung A12',
                             'Guinness',
                             'AOC'
                         ])
def test_search_not_existing_product(driver, url, product):
    """Test search not existing product"""
    MainPage(driver).open(url)
    MainPage(driver).searching_the_product(product)
    assert 'There is no product that matches the search criteria.' in SearchPage(driver).get_empty_search_page_text()
