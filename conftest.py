import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver

from pages.base_page import BasePage
load_dotenv("test.env")
# load_dotenv()


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    options = webdriver.ChromeOptions()

    selenoid_url = os.getenv("SELENOID_URL")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    command_executor = f"https://{login}:{password}@{selenoid_url}"

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