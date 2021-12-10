import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.main.page.login_page import LoginPage
import time


class Test_Login:
    baseURL = 'http://localhost:3000/signin'
    username = ''
    password = ''

    def test_login_page(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseURL)
        loginpage = LoginPage(driver)
        loginpage.setUserName(username)
        loginpage.setPassword(password)

        time.sleep(3)
        self.driver.close()


# def test_login():
#     Login_Test().test_login_page()
