import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.login_form import LoginForm, UserData


@allure.epic("Test login form")
@allure.feature("Login form")
class TestLogin:

    @allure.title("Successful login with email")
    def test_login_by_email_success(self, login_form, base_page, valid_user):
        login_form.open()
        login_form.fill_in(valid_user)
        login_form.wait.until(EC.invisibility_of_element_located(LoginForm.LOGIN_FORM))
        assert valid_user.expected_name == login_form.get_profile_name()

    @allure.title("Invalid login with email")
    @pytest.mark.parametrize("email, password, warning", [
        ("", "", "email"),
        ("", "test12345", "email"),
        ("testuser@test.ru", "", "password"),
        ("testuser@test.ru", "invalid_password", "login_error"),
        ("afsnklnsdkbdasjhbkjhads@mail.ru", "valid_pass", "login_error"),
    ])
    def test_login_by_email_fail(self, login_form, base_page, email, password, warning):
        invalid_data = UserData(email=email, password=password)
        login_form.open()
        login_form.fill_in(invalid_data)
        match warning:
            case "email":
                with allure.step("Check email warning message"):
                    warning_email = login_form.get_email_warning()
                    assert "Требуется указать email" == warning_email, "Сообщение с предупреждением не высветилось"
            case "password":
                with allure.step("Check password warning message"):
                    warning_password = login_form.get_password_warning()
                    assert "Требуется указать пароль" == warning_password, "Сообщение с предупреждением не высветилось"
            case "login_error":
                with allure.step("Check login error message"):
                    login_error = login_form.get_login_error()
                    assert "Неверный логин или пароль. Проверьте введённые данные и попробуйте снова." in login_error, "Сообщение об ошибке не высветилось"

            case _:
                assert False, "Неизвестное сообщение об ошибке"
