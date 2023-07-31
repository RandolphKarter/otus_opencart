import json
import logging
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from pages.LoginPage import LoginPage


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
    parser.addoption(
        '--log_level',
        action='store',
        default='INFO',
        help='This is level of logging'
    )
    parser.addoption(
        '--local',
        action='store_true',
        help='Option for local tests run'
    )
    parser.addoption(
        '--executor',
        action='store',
        default='127.0.0.1',
        help='Selenoid executor'
    )
    parser.addoption(
        '--selenoid_video',
        action='store_true',
        help='Enable video for tests run in selenoid'
    )
    parser.addoption(
        '--selenoid_log',
        action='store_true',
        help='Enable selenoid logging'
    )
    parser.addoption(
        '--selenoid_vnc',
        action='store_true',
        help='Enable selenoid vnc'
    )
    parser.addoption(
        '--browser_version',
        action='store',
        help='Set browser version for selenoid'
    )
    parser.addoption(
        '--mobile',
        action='store',
        help='Launch mobile browser version. Only for chromium'
    )


@pytest.fixture
def driver(request, logger):
    browser = request.config.getoption('--browser')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')
    local = request.config.getoption('--local')
    executor = request.config.getoption("--executor")
    selenoid_video = request.config.getoption('--selenoid_video')
    selenoid_log = request.config.getoption('--selenoid_log')
    selenoid_vnc = request.config.getoption('--selenoid_vnc')
    browser_version = request.config.getoption('--browser_version')
    mobile = request.config.getoption('--mobile')

    executor_url = f"http://{executor}:4444/wd/hub"

    selenoid_caps = {
            "enableVideo": selenoid_video,
            "enableLog": selenoid_log,
            "enableVNC": selenoid_vnc
    }

    mobile_emulation = {
        'deviceName':  mobile
    }

    match browser:
        case 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('headless=new')
            if mobile:
                options.add_experimental_option('mobileEmulation', mobile_emulation)
            if local:
                driver = webdriver.Chrome(options=options)
            else:
                options.set_capability("browserName", browser)
                options.browser_version = browser_version
                options.set_capability('selenoid:options', selenoid_caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case 'firefox':
            options = FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            if mobile:
                raise ValueError('Mobile firefox not support')
            if local:
                driver = webdriver.Firefox(options=options)
            else:
                options.set_capability("browserName", browser)
                options.browser_version = browser_version
                options.set_capability('selenoid:options', selenoid_caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case 'opera':
            options = ChromeOptions()
            options.add_experimental_option('w3c', True)
            if headless:
                options.add_argument('headless=new')
            if mobile:
                options.add_experimental_option('mobileEmulation', mobile_emulation)
            if local:
                service = Service(executable_path=os.path.expanduser('~/drivers/operadriver'))
                driver = webdriver.Chrome(options=options, service=service)
            else:
                options.set_capability("browserName", browser)
                options.browser_version = browser_version
                options.set_capability('selenoid:options', selenoid_caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case 'edge':
            options = EdgeOptions()
            if headless:
                options.add_argument('headless=new')
            if mobile:
                options.add_experimental_option('mobileEmulation', mobile_emulation)
            if local:
                driver = webdriver.Edge(options=options)
            else:
                options.set_capability("browserName", 'MicrosoftEdge')
                options.browser_version = browser_version
                options.set_capability('selenoid:options', selenoid_caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case _:
            raise ValueError(f'Browser {browser} not support')

    if maximize:
        driver.set_window_size(1920, 1080)

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    driver.logger = logger
    driver.logger.info('Browser %s started' % browser)

    yield driver
    driver.quit()


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def port(request):
    return request.config.getoption('--port')


@pytest.fixture
def admin_auth(driver, url, port):
    LoginPage(driver).open(url, port, LoginPage.PATH)
    LoginPage(driver).fill_input(LoginPage.USERNAME_INPUT, 'user')
    LoginPage(driver).fill_input(LoginPage.PASSWORD_INPUT, 'bitnami')
    LoginPage(driver).element_is_visible(LoginPage.SUBMIT_BUTTON).click()


@pytest.fixture
def logger(request):
    log_level = request.config.getoption('--log_level')

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s '
        '[File name: %(filename)s | Function name: %(funcName)s | Line: %(lineno)d]'
    ))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    logger.info("=========> TEST %s START" % request.node.name)
    yield logger
    logger.info("=========> TEST %s FINISH" % request.node.name)
