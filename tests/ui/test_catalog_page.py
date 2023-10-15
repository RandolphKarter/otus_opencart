import allure
from pages.CatalogPage import CatalogPage
from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu


@allure.tag('Smoke', 'UI')
@allure.feature('Catalog page')
@allure.story('Compare link')
@allure.title('Test visibility of a compare link')
def test_catalog_page_product_compare_link(driver, url):
    """Test visibility of a compare link"""
    MainPage(driver).open(url)
    MainMenu(driver).random_link_click()
    assert 'Product Compare' in CatalogPage(driver).get_product_compare_link_text()


@allure.tag('Smoke', 'UI')
@allure.feature('Catalog page')
@allure.story('Page title')
@allure.title('Test visibility of a page title')
def test_catalog_page_title(driver, url):
    """Test visibility of a page title"""
    MainPage(driver).open(url)
    random_link_text = MainMenu(driver).get_random_link_name()
    MainMenu(driver).random_link_click()
    page_title = CatalogPage(driver).get_page_title_text()
    assert random_link_text in page_title


@allure.tag('Smoke', 'UI')
@allure.feature('Catalog page')
@allure.story('Sort input')
@allure.title('Test visibility of sort')
def test_catalog_page_select_sort(driver, url):
    """Test visibility of sort"""
    MainPage(driver).open(url)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_sort_input()


@allure.tag('Smoke', 'UI')
@allure.feature('Catalog page')
@allure.story('Limit input')
@allure.title('Test visibility of select a limit')
def test_catalog_page_select_limit(driver, url):
    """Test visibility of select a limit"""
    MainPage(driver).open(url)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_limit_input()


@allure.tag('Smoke', 'UI')
@allure.feature('Catalog page')
@allure.story('Product card')
@allure.title('Test visibility of product cards')
def test_catalog_page_product_card(driver, url):
    """Test visibility of product cards"""
    MainPage(driver).open(url)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_product_cards()
