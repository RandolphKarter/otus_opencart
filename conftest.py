import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='This is the browser in which the tests will run'
    )
    parser.addoption(
        '--maximize',
        action='store_true',
        help='Maximize browser window width'
    )
    parser.addoption(
        '--headless',
        action='store_true',
        help='Headless browser mode'
    )
    parser.addoption(
        '--url',
        default='http://127.0.0.1',
        help='This is opencart local url'
    )
    parser.addoption(
        '--port',
        default=':8081',
        help='This is opencart local port'
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('--browser')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')

    match browser_name:
        case 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('headless=new')
            driver = webdriver.Chrome(options=options)
        case 'firefox':
            options = FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options)
        case 'opera':
            options = ChromeOptions()
            if headless:
                options.add_argument('headless=new')
            options.add_experimental_option('w3c', True)
            service = Service(executable_path=os.path.expanduser('~/drivers/operadriver'))
            driver = webdriver.Chrome(options=options, service=service)
        case _:
            raise ValueError(f'Browser {browser_name} not support')

    if maximize:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def opencart_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def opencart_port(request):
    return request.config.getoption('--port')
