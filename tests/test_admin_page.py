import pytest
from data.generator.product_generator import generate_product
from pages.elements.AdminMenu import AdminMenu
from pages.AdminPage import AdminPage


@pytest.mark.usefixtures('admin_auth')
class TestProductsDirectory:
    new_product = next(generate_product())

    def test_add_product(self, driver):
        AdminMenu(driver).go_to_products_directory()
        AdminPage(driver).add_new_product(self.new_product)
        assert 'Success: You have modified products!' in AdminPage(driver).get_success_alert_text()

    def test_delete_product(self, driver):
        AdminMenu(driver).go_to_products_directory()
        AdminPage(driver).filter_the_list(self.new_product)
        AdminPage(driver).delete_product()
        assert 'Success: You have modified products!' in AdminPage(driver).get_success_alert_text()
