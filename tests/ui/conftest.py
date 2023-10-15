import json
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from pages.AdminLoginPage import AdminLoginPage
from dotenv import load_dotenv


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
        'deviceName': mobile
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
def admin_auth(driver, url):
    load_dotenv()
    AdminLoginPage(driver).open(url, AdminLoginPage.PATH)
    AdminLoginPage(driver).fill_input(AdminLoginPage.USERNAME_INPUT, os.getenv('OC_ADMIN_NAME'))
    AdminLoginPage(driver).fill_input(AdminLoginPage.PASSWORD_INPUT, os.getenv('OC_ADMIN_PW'))
    AdminLoginPage(driver).element_is_visible(AdminLoginPage.SUBMIT_BUTTON).click()
