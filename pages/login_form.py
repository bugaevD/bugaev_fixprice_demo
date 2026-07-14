import allure
from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.login_form_locators import LoginFormLocators


@dataclass
class ValidUser:
    email: str
    password: str
    expected_name: str


class LoginForm:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open login form")
    def open_login(self):
        self.driver.find_element(*LoginFormLocators.LOGIN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_EMAIL))

    @allure.step("Login with email")
    def login_by_email(self, user:ValidUser):
        with allure.step("Open login form"):
            self.driver.find_element(*LoginFormLocators.LOGIN_EMAIL).click()
        with allure.step(f"Fill user email with: {user.email}"):
            self.wait.until(EC.element_to_be_clickable(LoginFormLocators.EMAIL_INPUT)).send_keys(user.email)
        with allure.step(f"Fill user password with: {user.password}"):
            self.driver.find_element(*LoginFormLocators.PASSWORD_INPUT).send_keys(user.password)
        with allure.step("Click login button"):
            self.driver.find_element(*LoginFormLocators.LOGIN_SUBMIT_BUTTON).click()
        with allure.step(f"Verify user {user.expected_name} is logged in"):
            self.wait.until(EC.invisibility_of_element_located(LoginFormLocators.LOGIN_FORM))

            profile_name = self.driver.find_element(*BasePageLocators.PROFILE_NAME)
            profile_name = profile_name.text

            assert profile_name == user.expected_name, f"Ждали: {user.expected_name}, получили: {profile_name}"