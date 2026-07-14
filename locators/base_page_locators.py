from selenium.webdriver.common.by import By

class BasePageLocators:

    MAIN_PAGE_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-input input")
    PROFILE_NAME = (By.CSS_SELECTOR, ".login-btn .profile")
    PROFILE_MENU = (By.CSS_SELECTOR, ".subcategories-container.new-profile")