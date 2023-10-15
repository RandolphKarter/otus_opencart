import allure
from pages.AdminLoginPage import AdminLoginPage


@allure.tag('Smoke', 'UI')
@allure.feature('Admin login page')
@allure.story('Page title')
@allure.title('Test visibility of a page title')
def test_admin_login_page_title(driver, url):
    """Test title of login page"""
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    assert 'Please enter your login details.' in AdminLoginPage(driver).get_page_title_text()


@allure.tag('Smoke', 'UI')
@allure.feature('Admin login page')
@allure.story('Username input')
@allure.title('Test visibility of username input')
def test_admin_login_page_username_input(driver, url):
    """Test visibility of username input on login page"""
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    assert AdminLoginPage(driver).get_username_input_placeholder() == 'Username'


@allure.tag('Smoke', 'UI')
@allure.feature('Admin login page')
@allure.story('Password input')
@allure.title('Test visibility of password input')
def test_admin_login_page_password_input(driver, url):
    """Test visibility of password input on login page"""
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    assert AdminLoginPage(driver).get_password_input_placeholder() == 'Password'


@allure.tag('Smoke', 'UI')
@allure.feature('Admin login page')
@allure.story('Submit button')
@allure.title('Test visibility of submit button')
def test_admin_login_page_submit_button(driver, url):
    """Test visibility of submit button on login page"""
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    assert AdminLoginPage(driver).get_submit_button_text() == 'Login'


@allure.tag('Smoke', 'UI')
@allure.feature('Admin login page')
@allure.story('Forgotten password link')
@allure.title('Test visibility of forgotten password')
def test_admin_login_page_forgotten_password_link(driver, url):
    """Test visibility of forgotten password link on login page"""
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    assert AdminLoginPage(driver).get_forgotten_password_link_text() == 'Forgotten Password'
