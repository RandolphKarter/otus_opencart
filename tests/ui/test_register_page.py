import allure
import pytest
from pages.RegisterPage import RegisterPage
from pages.elements.TopMenu import TopMenu
from pages.MainPage import MainPage


@allure.tag('Smoke', 'UI')
@allure.feature('Register page')
@allure.story('Submit button')
@allure.title('Test visibility of submit button')
def test_register_page_submit_button(driver, url):
    """Test visibility of submit button"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_submit_button_attr_value() == 'Continue'


@allure.tag('Smoke', 'UI')
@allure.feature('Register page')
@allure.story('Agree checkbox')
@allure.title('Test visibility of agree checkbox')
def test_register_page_agree_checkbox(driver, url):
    """Test visibility of agree checkbox"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_agree_checkbox_attr_name() == 'agree'


@allure.tag('Smoke', 'UI')
@allure.feature('Register page')
@allure.story('Firstname input')
@allure.title('Test visibility of firstname input')
def test_register_page_firstname_input(driver, url):
    """Test visibility of firstname input"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_firstname_input_placeholder() == 'First Name'


@allure.tag('Smoke', 'UI')
@allure.feature('Register page')
@allure.story('Telephone input')
@allure.title('Test visibility of telephone input')
def test_register_page_telephone_input(driver, url):
    """Test visibility of telephone input"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_telephone_input_placeholder() == 'Telephone'


@allure.tag('Smoke', 'UI')
@allure.feature('Register page')
@allure.story('Password input')
@allure.title('Test visibility of password input')
def test_register_page_password_input(driver, url):
    """Test visibility of password input"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_password_input_placeholder() == 'Password'


@allure.tag('Smoke', 'UI')
@allure.feature('User registration')
@allure.story('New user registration')
@allure.title('Test new user registration')
@pytest.mark.parametrize('repeat', range(2))
def test_new_user_registration(driver, url, repeat, get_new_user):
    """Test new user registration"""
    MainPage(driver).open(url)
    TopMenu(driver).go_to_registration_page()
    RegisterPage(driver).fill_registration_form(get_new_user)
    assert 'Your Account Has Been Created!' in RegisterPage(driver).get_success_text()
