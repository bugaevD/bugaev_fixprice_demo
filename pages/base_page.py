import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = BasePageLocators()

    @allure.step("Open main page")
    def open_base_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(BasePageLocators.MAIN_PAGE_LOGO))
    @allure.step("Open login form")
    def open_login(self):
        self.driver.find_element(*BasePageLocators.LOGIN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(BasePageLocators.LOGIN_EMAIL))
    @allure.step("Login with email")
    def login_by_email(self, email, password, expected_name):
        self.driver.find_element(*BasePageLocators.LOGIN_EMAIL).click()
        self.wait.until(EC.element_to_be_clickable(BasePageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*BasePageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*BasePageLocators.LOGIN_SUBMIT_BUTTON).click()
        self.wait.until(EC.invisibility_of_element_located(BasePageLocators.LOGIN_FORM))

        profile_name = self.driver.find_element(*BasePageLocators.PROFILE_NAME)
        profile_name = profile_name.text

        assert profile_name == expected_name, f"Ждали: {expected_name}, получили: {profile_name}"

    def get_profile_name(self):
        return self.driver.find_element(*BasePageLocators.PROFILE_NAME).text

    def select_city(self, city):
        pass

    def fill_search_input(self, text="булдак"):
        search_input = self.driver.find_element(*BasePageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.clear()
        search_input.send_keys(text)
