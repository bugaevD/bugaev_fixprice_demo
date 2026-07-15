import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    MAIN_PAGE_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-input input")
    PROFILE_NAME = (By.CSS_SELECTOR, ".login-btn .profile")
    PROFILE_MENU = (By.CSS_SELECTOR, ".subcategories-container.new-profile")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open main page")
    def open_base_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.MAIN_PAGE_LOGO))

    def get_profile_name(self):
        return self.driver.find_element(*self.PROFILE_NAME).text

    def select_city(self, city):
        pass

    def fill_search_input(self, text="булдак"):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.click()
        search_input.clear()
        search_input.send_keys(text)
