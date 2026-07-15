import allure
from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.login_form_locators import LoginFormLocators
from pages.base_page import BasePage


@dataclass
class ValidUser:
    email: str
    password: str
    expected_name: str


class LoginForm:
    LOGIN_FORM = (By.CSS_SELECTOR, ".wrapper.modal-child")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")
    LOGIN_EMAIL = (By.XPATH, "//button[contains(@class, 'outline-tetriary') and span[text()='По email']]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and span[text()='Войти']]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open login form")
    def open_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL))

    @allure.step("Login with email")
    def login_by_email(self, user: ValidUser):
        with allure.step("Open login form"):
            self.driver.find_element(*self.LOGIN_EMAIL).click()
        with allure.step(f"Fill user email with: {user.email}"):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(user.email)
        with allure.step(f"Fill user password with: {user.password}"):
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(user.password)
        with allure.step("Click login button"):
            self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()
        with allure.step(f"Verify user {user.expected_name} is logged in"):
            self.wait.until(EC.invisibility_of_element_located(self.LOGIN_FORM))

            profile_name = self.driver.find_element(*BasePage.PROFILE_NAME)
            profile_name = profile_name.text

            assert profile_name == user.expected_name, f"Ждали: {user.expected_name}, получили: {profile_name}"
