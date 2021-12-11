from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    textbox_username_id = 'username'
    textbox_password_id = 'password'
    button_submit_css_selector = '[data-test="signin-submit"]'
    linktext_logout_linktext = ''

    def __init__(self, driver):
        # webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.driver.maximize_window()

    def login_to_application(self, username, password):
        self.driver.find_element_by_id(
            self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(
            self.textbox_password_id).send_keys(password)
        self.driver.find_element_by_css_selector(
            self.button_submit_css_selector)
