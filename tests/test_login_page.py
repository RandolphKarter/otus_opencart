from pages.LoginPage import LoginPage


def test_login_page_title(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert 'Please enter your login details.' in LoginPage(driver).get_page_title_text()


def test_login_page_username_input(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_username_input_placeholder() == 'Username'


def test_login_page_password_input(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_password_input_placeholder() == 'Password'


def test_login_page_submit_button(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_submit_button_text() == 'Login'


def test_login_page_forgotten_password_link(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    assert LoginPage(driver).get_forgotten_password_link_text() == 'Forgotten Password'




