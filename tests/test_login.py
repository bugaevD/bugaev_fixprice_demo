import os

import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.login_form import LoginForm, UserData


@allure.epic("Test login form")
@allure.feature("Login form")
class TestLogin:

    @allure.title("Successful login with email")
    def test_login_by_email_success(self, driver, base_page, valid_user):
        login_form = LoginForm(driver)
        login_form.open_login()
        login_form.fill_login_form(valid_user)
        login_form.wait.until(EC.invisibility_of_element_located(LoginForm.LOGIN_FORM))
        assert valid_user.expected_name == login_form.get_profile_name()

    @allure.title("Invalid login with email")
    @pytest.mark.parametrize("email, password, error", [
        ("", "", "email"),
        ("", "test12345", "email"),
        ("testuser@test.ru", "", "password"),
        ("testuser@test.ru", "invalid_password", "login_error"),
        ("afsnklnsdkbdasjhbkjhads@mail.ru", "valid_pass", "login_error"),
    ])
    def test_login_by_email_fail(self, driver, base_page, email, password, error):
        login_form = LoginForm(driver)
        invalid_data = UserData(email=email, password=password)
        login_form.open_login()
        login_form.fill_login_form(invalid_data)
        if error == "email":
            with allure.step("Check email error message"):
                email_error = login_form.get_email_error()
                assert "Требуется указать email" == email_error
        elif error == "password":
            with allure.step("Check password error message"):
                password_error = login_form.get_password_error()
                assert "Требуется указать пароль" == password_error
        elif error == "login_error":
            with allure.step("Check login error message"):
                login_error = login_form.get_login_error()
                assert "Неверный логин или пароль. Проверьте введённые данные и попробуйте снова." in login_error
        else:
            assert False, f"Неизвестный тип ошибки: {error}"
