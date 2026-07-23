from typing import Optional

import allure
from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


@dataclass
class UserData:
    email: str
    password: str
    expected_name: Optional[str] = None


class LoginForm:
    LOGIN_FORM = (By.CSS_SELECTOR, ".wrapper.modal-child")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")
    LOGIN_EMAIL = (By.XPATH, "//button[contains(@class, 'outline-tetriary') and span[text()='По email']]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and span[text()='Войти']]")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".login .error")
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".password .error")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".informer.error .content")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Open login form")
    def open(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL))

    @allure.step("Login by email")
    def fill_in(self, user: UserData):
        with allure.step("Open login by email"):
            self.driver.find_element(*self.LOGIN_EMAIL).click()
        with allure.step(f"Fill user email with: {user.email}"):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(user.email)
        with allure.step(f"Fill user password with: {user.password}"):
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(user.password)
        with allure.step("Click login button"):
            self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()

    @allure.step("Get error message after login with invalid email")
    def get_email_warning(self):
        with allure.step("Check email error message"):
            email_error = self.wait.until(EC.visibility_of_element_located(self.EMAIL_ERROR))
            email_error = email_error.text
            return email_error

    @allure.step("Get error message after login with invalid password")
    def get_password_warning(self):
        with allure.step("Check password error message"):
            password_error = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_ERROR))
            password_error = password_error.text
            return password_error

    @allure.step("Get error message after login with invalid data")
    def get_login_warning(self):
        with allure.step("Check login error message"):
            login_error = self.wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR))
            login_error = login_error.text
            return login_error

    @allure.step("Get user profile name after success login")
    def get_profile_name(self):
        return self.driver.find_element(*BasePage.PROFILE_NAME).text
