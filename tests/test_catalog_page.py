from pages.CatalogPage import CatalogPage
from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu


def test_catalog_page_product_compare_link(driver, url, port):
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert 'Product Compare' in CatalogPage(driver).get_product_compare_link_text()


def test_catalog_page_title(driver, url, port):
    MainPage(driver).open(url, port)
    random_link_text = MainMenu(driver).get_random_link_name()
    MainMenu(driver).random_link_click()
    page_title = CatalogPage(driver).get_page_title_text()
    assert random_link_text in page_title


def test_catalog_page_select_sort(driver, url, port):
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_sort_input()


def test_catalog_page_select_limit(driver, url, port):
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_select_limit_input()


def test_catalog_page_product_card(driver, url, port):
    MainPage(driver).open(url, port)
    MainMenu(driver).random_link_click()
    assert CatalogPage(driver).get_product_cards()
