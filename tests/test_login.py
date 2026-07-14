import allure

from pages.login_form import LoginForm
from pages.base_page import BasePage

class TestLogin:

    @allure.title("Successful login with email")
    def test_login_by_email_success(self, driver, base_page, user_data):
        login_form = LoginForm(driver)
        with allure.step("Open login form"):
            login_form.open_login()
        with allure.step("Login by email"):
            login_form.login_by_email(email=user_data["email"], password=user_data["password"], expected_name=user_data["expected_name"])
