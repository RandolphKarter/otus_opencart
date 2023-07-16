from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu
from pages.elements.TopMenu import TopMenu


def test_main_page_logo(driver, url, port):
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_logo_img_attr_title() == 'Your Store'


def test_main_page_search(driver, url, port):
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_search_input_placeholder() == 'Search'


def test_main_page_cart(driver, url, port):
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_cart()


def test_main_page_menu(driver, url, port):
    MainPage(driver).open(url, port)
    assert MainMenu(driver).get_main_menu()


def test_main_page_slider(driver, url, port):
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_slider()


def test_main_page_change_currency(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).choice_currency()
    selected_currency = TopMenu(driver).get_currency_name()
    product_price = MainPage(driver).get_featured_product_price()
    assert selected_currency[:1] in product_price
