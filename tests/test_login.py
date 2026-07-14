import os

import allure

from pages.login_form import LoginForm, ValidUser
from pages.base_page import BasePage

class TestLogin:

    @allure.title("Successful login with email")
    def test_login_by_email_success(self, driver, base_page):
        login_form = LoginForm(driver)
        valid_data = ValidUser(email=os.getenv("USER_EMAIL"), password=os.getenv("USER_PASSWORD"), expected_name=os.getenv("EXPECTED_NAME"))
        with allure.step("Open login form"):
            login_form.open_login()
        with allure.step("Login by email"):
            login_form.login_by_email(valid_data)
