from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    '''
    Login page
    '''
    textbox_username_id = 'username'
    textbox_password_id = 'password'
    button_submit_css_selector = '[data-test="signin-submit"]'
    linktext_logout_linktext = ''

    def __init__(self, driver):
        # webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.driver.maximize_window()

    def login_to_application(self, username, password):
        self.driver.find_element(By.ID,
                                 self.textbox_username_id).send_keys(username)
        self.driver.find_element(By.ID,
                                 self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,
                                 self.button_submit_css_selector).click()

