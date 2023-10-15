import allure
import pytest
from pages.MainPage import MainPage
from pages.elements.TopMenu import TopMenu
from pages.CartPage import CartPage


@allure.tag('Smoke', 'UI')
@allure.feature('Cart')
@allure.story('Add product to cart')
@allure.title('Test adding product to cart')
@pytest.mark.parametrize('repeat', range(2))
def test_add_product_to_cart(driver, url, repeat):
    """Test add product to cart"""
    MainPage(driver).open(url)
    product_name = MainPage(driver).get_product_name_and_add_product_to_cart()
    TopMenu(driver).go_to_cart_page()
    product_name_from_cart = CartPage(driver).get_product_name_from_cart()
    assert product_name == product_name_from_cart


@allure.tag('Smoke', 'UI')
@allure.feature('Cart')
@allure.story('Remove product from cart')
@allure.title('Test removing product from cart')
@pytest.mark.parametrize('repeat', range(2))
def test_remove_product_from_cart(driver, url, repeat):
    """Test remove product from cart"""
    MainPage(driver).open(url)
    MainPage(driver).add_product_to_cart()
    TopMenu(driver).go_to_cart_page()
    CartPage(driver).remove_product_from_cart()
    assert 'Your shopping cart is empty!' in CartPage(driver).get_empty_cart_text()
