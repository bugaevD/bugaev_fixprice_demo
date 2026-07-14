import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from utils import attach
from pages.base_page import BasePage

load_dotenv("test.env")


# load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to use",
        choices=("chrome", "firefox", "msedge")
    )
    parser.addoption(
        "--browser_version",
        default="148.0",
        help="Browser version to use. Versions 148.0 and 149.0 for Chrome, 144.0 and 145.0 for msedge, 150.0 and 151.0 for Firefox",
        choices=("144.0", "145.0", "148.0", "149.0", "150.0", "151.0")
    )
    parser.addoption(
        "--headless",
        type=str,
        default="false",
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--window-size",
        default="1920x1080",
        help="Size of window to use",
        choices=("1920x1080", "2560x1440", "1280x720")
    )
    parser.addoption(
        "--base_url",
        default=os.getenv("BASE_URL"),
        help="website url"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    headless = request.config.getoption("--headless").lower() == "true"
    window_size = request.config.getoption("--window-size")

    selenoid_url = os.getenv("SELENOID_URL")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    command_executor = f"https://{login}:{password}@{selenoid_url}"

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless")

    options.add_argument(f"--window-size={window_size.replace('x', ',')}")

    selenoid_capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )

    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(driver)
    driver.quit()


@pytest.fixture
def base_page(driver, base_url):
    base_page = BasePage(driver)
    base_page.open_base_page(base_url)
    return base_page


@pytest.fixture
def user_data():
    return {
        "email": os.getenv("USER_EMAIL"),
        "password": os.getenv("USER_PASSWORD"),
        "invalid_email": "invalid_email@mailru",
        "invalid_password": "",
        "expected_name": os.getenv("EXPECTED_NAME"),
    }


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
