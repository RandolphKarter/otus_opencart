import allure
import pytest
from pages.RegisterPage import RegisterPage
from pages.elements.TopMenu import TopMenu
from pages.MainPage import MainPage
from pages.UserLoginPage import UserLoginPage
from pages.AccountPage import AccountPage


@allure.tag('Smoke', 'UI')
@allure.feature('User login')
@allure.story('New user login')
@allure.title('Test new user login')
@pytest.mark.parametrize('repeat', range(5))
def test_new_user_login(driver, url, get_new_user, repeat):
    """Test new user login"""
    new_user = get_new_user
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    RegisterPage(driver).fill_registration_form(new_user)
    TopMenu(driver).logout_user()
    TopMenu(driver).go_to_login_page()
    UserLoginPage(driver).fill_login_form(new_user)
    assert 'My Account' in AccountPage(driver).get_my_account_tittle()


@allure.tag('Smoke', 'UI')
@allure.feature('User login')
@allure.story('Login not existing user')
@allure.title('Test not existing user login')
@pytest.mark.parametrize('repeat', range(5))
def test_login_not_existing_user(driver, url, get_new_user, repeat):
    """Test not existing user login"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_login_page()
    UserLoginPage(driver).fill_login_form(get_new_user)
    assert ('Warning: No match for E-Mail Address and/or Password'
            in UserLoginPage(driver).get_warning_alert_text())
