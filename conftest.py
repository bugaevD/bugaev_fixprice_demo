import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver

from pages.base_page import BasePage

load_dotenv()


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=2560,1440")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    base_page = BasePage(driver)
    base_page.open_base_page("https://fix-price.com/")
    return base_page

@pytest.fixture
def user_data():
    return {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD"),
        "invalid_email": "invalid_email@mailru",
        "invalid_password": "",
        "expected_name": os.getenv("EXPECTED_NAME"),
    }