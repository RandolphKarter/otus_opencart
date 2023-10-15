import allure
import pytest
from pages.elements.AdminMenu import AdminMenu
from pages.AdminPage import AdminPage


# @pytest.mark.xdist_group(name="new_product_group")
@allure.tag('Smoke', 'UI')
@allure.feature('Work with products in site admin')
@allure.story('Add product')
@allure.title('Test the addition of a new product')
@pytest.mark.usefixtures('admin_auth')
# @pytest.mark.parametrize('new_product',
#                          [
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product())
#                          ])
@pytest.mark.parametrize('repeat', range(5))
def test_add_product(driver, repeat, get_new_product):
    """Test the addition of a new product"""
    AdminMenu(driver).go_to_products_directory()
    AdminPage(driver).add_new_product(get_new_product)
    assert 'Success: You have modified products!' in AdminPage(driver).get_success_alert_text()


# @pytest.mark.xdist_group(name="new_product_group")
@allure.tag('Smoke', 'UI')
@allure.feature('Work with products in site admin')
@allure.story('Delete product')
@allure.title('Test the deleting of a new product')
@pytest.mark.usefixtures('admin_auth')
# @pytest.mark.parametrize('new_product',
#                          [
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product()),
#                              next(generate_product())
#                          ])
@pytest.mark.parametrize('repeat', range(5))
def test_delete_product(driver, repeat, get_new_product):
    """Test the deleting of a new product"""
    new_product = get_new_product
    AdminMenu(driver).go_to_products_directory()
    AdminPage(driver).add_new_product(new_product)
    AdminPage(driver).filter_the_list(new_product)
    AdminPage(driver).delete_product()
    assert 'Success: You have modified products!' in AdminPage(driver).get_success_alert_text()
