import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.main.page.login_page import LoginPage
from src.main.config.conf_test import setUp
import time


class Test_Login:
    baseURL = 'http://localhost:3000/signin'
    username = 'Katharina_Bernier'
    password = 's3cret'

    def test_login_page(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        loginpage = LoginPage(self.driver)
        loginpage.login_to_application(self.username, self.password)

        time.sleep(3)
        self.driver.close()
