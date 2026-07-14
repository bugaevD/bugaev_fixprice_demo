from selenium.webdriver.common.by import By

class BasePageLocators:

    MAIN_PAGE_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-input input")
    LOGIN_FORM = (By.CSS_SELECTOR, ".wrapper.modal-child")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")
    LOGIN_EMAIL = (By.XPATH, "//button[contains(@class, 'outline-tetriary') and span[text()='По email']]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='input'][type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and span[text()='Войти']]")
    PROFILE_NAME = (By.CSS_SELECTOR, ".login-btn .profile")
    PROFILE_MENU = (By.CSS_SELECTOR, ".subcategories-container.new-profile")