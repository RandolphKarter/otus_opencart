import allure
from pages.MainPage import MainPage
from pages.elements.MainMenu import MainMenu
from pages.elements.TopMenu import TopMenu


@allure.title('Test visibility of logo')
def test_main_page_logo(driver, url, port):
    """Test visibility of logo on main page"""
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_logo_img_attr_title() == 'Your Store'


@allure.title('Test visibility of search')
def test_main_page_search(driver, url, port):
    """Test visibility of search on main page"""
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_search_input_placeholder() == 'Search'


@allure.title('Test visibility of cart')
def test_main_page_cart(driver, url, port):
    """Test visibility of cart on main page"""
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_cart()


@allure.title('Test visibility of main menu')
def test_main_page_menu(driver, url, port):
    """Test visibility of main menu on main page"""
    MainPage(driver).open(url, port)
    assert MainMenu(driver).get_main_menu()


@allure.title('Test visibility of slider')
def test_main_page_slider(driver, url, port):
    """Test visibility of slider on main page"""
    MainPage(driver).open(url, port)
    assert MainPage(driver).get_slider()


@allure.title('Test change currency')
def test_main_page_change_currency(driver, url, port):
    """Test change currency on main page"""
    MainPage(driver).open(url, port)
    TopMenu(driver).choice_currency()
    selected_currency = TopMenu(driver).get_currency_name()
    product_price = MainPage(driver).get_featured_product_price()
    assert selected_currency[:1] in product_price
