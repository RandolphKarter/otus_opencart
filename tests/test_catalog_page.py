import allure
from pages.CatalogPage import CatalogPage
from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu


@allure.title('Test visibility of a compare link')
def test_catalog_page_product_compare_link(driver, url, port):
    """Test visibility of a compare link"""
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert 'Product Compare' in CatalogPage(driver).get_product_compare_link_text()


@allure.title('Test visibility of a page title')
def test_catalog_page_title(driver, url, port):
    """Test visibility of a page title"""
    MainPage(driver).open(url, port)
    random_link_text = MainMenu(driver).get_random_link_name()
    MainMenu(driver).random_link_click()
    page_title = CatalogPage(driver).get_page_title_text()
    assert random_link_text in page_title


@allure.title('Test visibility of sort')
def test_catalog_page_select_sort(driver, url, port):
    """Test visibility of sort"""
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_sort_input()


@allure.title('Test visibility of select a limit')
def test_catalog_page_select_limit(driver, url, port):
    """Test visibility of select a limit"""
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_limit_input()


@allure.title('Test visibility of product cards')
def test_catalog_page_product_card(driver, url, port):
    """Test visibility of product cards"""
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_product_cards()
