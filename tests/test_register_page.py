import allure
from pages.RegisterPage import RegisterPage
from pages.elements.TopMenu import TopMenu
from pages.MainPage import MainPage


@allure.title('Test visibility of submit button')
def test_register_page_submit_button(driver, url, port):
    """Test visibility of submit button"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_submit_button_attr_value() == 'Continue'


@allure.title('Test visibility of agree checkbox')
def test_register_page_agree_checkbox(driver, url, port):
    """Test visibility of agree checkbox"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_agree_checkbox_attr_name() == 'agree'


@allure.title('Test visibility of firstname input')
def test_register_page_firstname_input(driver, url, port):
    """Test visibility of firstname input"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_firstname_input_placeholder() == 'First Name'


@allure.title('Test visibility of telephone input')
def test_register_page_telephone_input(driver, url, port):
    """Test visibility of telephone input"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_telephone_input_placeholder() == 'Telephone'


@allure.title('Test visibility of password input')
def test_register_page_password_input(driver, url, port):
    """Test visibility of password input"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_password_input_placeholder() == 'Password'


@allure.title('Test new user registration')
def test_new_user_registration(driver, url, port):
    """Test new user registration"""
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    RegisterPage(driver).fill_registration_form()
    assert 'Your Account Has Been Created!' in RegisterPage(driver).get_success_text()


