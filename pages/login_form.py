import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.login_form_locators import LoginFormLocators


class LoginForm:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open login form")
    def open_login(self):
        self.driver.find_element(*LoginFormLocators.LOGIN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_EMAIL))

    @allure.step("Login with email")
    def login_by_email(self, email, password, expected_name):
        self.driver.find_element(*LoginFormLocators.LOGIN_EMAIL).click()
        self.wait.until(EC.element_to_be_clickable(LoginFormLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginFormLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginFormLocators.LOGIN_SUBMIT_BUTTON).click()
        self.wait.until(EC.invisibility_of_element_located(LoginFormLocators.LOGIN_FORM))

        profile_name = self.driver.find_element(*BasePageLocators.PROFILE_NAME)
        profile_name = profile_name.text

        assert profile_name == expected_name, f"Ждали: {expected_name}, получили: {profile_name}"