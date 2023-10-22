import allure
import pytest
from pages.RegisterPage import RegisterPage
from pages.elements.TopMenu import TopMenu
from pages.MainPage import MainPage
from pages.AccountPage import AccountPage


@allure.tag('Smoke', 'UI')
@allure.feature('User login')
@allure.story('User logout')
@allure.title('Test user logout')
@pytest.mark.parametrize('repeat', range(2))
def test_new_user_logout(driver, url, get_new_user, repeat):
    """Test new user logout"""
    new_user = get_new_user
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    RegisterPage(driver).fill_registration_form(new_user)
    TopMenu(driver).logout_user()
    assert 'Account Logout' in AccountPage(driver).get_logout_title()
