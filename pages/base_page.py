import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open main page")
    def open_base_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(BasePageLocators.MAIN_PAGE_LOGO))

    def get_profile_name(self):
        return self.driver.find_element(*BasePageLocators.PROFILE_NAME).text

    def select_city(self, city):
        pass

    def fill_search_input(self, text="булдак"):
        search_input = self.driver.find_element(*BasePageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.clear()
        search_input.send_keys(text)
