from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    textbox_username_id = '#username'
    textbox_password_id = '#password'
    button_submit_id = ''
    linktext_logout_linktext = ''

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(
            self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(
            self.textbox_username_id).send_keys(password)
