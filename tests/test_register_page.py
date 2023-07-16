from pages.RegisterPage import RegisterPage
from pages.elements.TopMenu import TopMenu
from pages.MainPage import MainPage


def test_register_page_submit_button(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_submit_button_attr_value() == 'Continue'


def test_register_page_agree_checkbox(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_agree_checkbox_attr_name() == 'agree'


def test_register_page_firstname_input(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_firstname_input_placeholder() == 'First Name'


def test_register_page_telephone_input(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_telephone_input_placeholder() == 'Telephone'


def test_register_page_password_input(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    assert RegisterPage(driver).get_password_input_placeholder() == 'Password'


def test_new_user_registration(driver, url, port):
    MainPage(driver).open(url, port)
    TopMenu(driver).go_to_registration_page()
    RegisterPage(driver).fill_registration_form()
    assert 'Your Account Has Been Created!' in RegisterPage(driver).get_success_text()


