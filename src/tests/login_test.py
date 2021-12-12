from src.main.page.login_page import LoginPage
from src.main.config.conf_test import set_up
from src.main.utils.read_property import ReadProperty
import time


class TestLogin:
    def test_login_page(self, set_up):
        self.driver = set_up
        self.driver.get(ReadProperty.get_application_url())
        login_page: LoginPage = LoginPage(self.driver)
        login_page.login_to_application(ReadProperty.get_user_name(), ReadProperty.get_user_password())

        time.sleep(3)
        self.driver.close()
