import allure
from pages.LoginPage import LoginPage


@allure.title('Test visibility of a page title')
def test_login_page_title(driver, url, port):
    """Test title of login page"""
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert 'Please enter your login details.' in LoginPage(driver).get_page_title_text()


@allure.title('Test visibility of username input')
def test_login_page_username_input(driver, url, port):
    """Test visibility of username input on login page"""
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_username_input_placeholder() == 'Username'


@allure.title('Test visibility of password input')
def test_login_page_password_input(driver, url, port):
    """Test visibility of password input on login page"""
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_password_input_placeholder() == 'Password'


@allure.title('Test visibility of submit button')
def test_login_page_submit_button(driver, url, port):
    """Test visibility of submit button on login page"""
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_submit_button_text() == 'Login'


@allure.title('Test visibility of forgotten password')
def test_login_page_forgotten_password_link(driver, url, port):
    """Test visibility of forgotten password link on login page"""
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_forgotten_password_link_text() == 'Forgotten Password'




