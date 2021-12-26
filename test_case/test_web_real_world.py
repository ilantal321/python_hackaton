import time
import allure
import pytest

from workfolw.create_signup import CreateNewUser
from workfolw.login_existing_user import login_extisting_user


@pytest.mark.usefixtures("init_web")
class TestSignIn:
    @allure.title('Check balance to extisting user')
    @allure.description('this test Check balance to exsisting user task')
    def test_login(self):
        login_fun = login_extisting_user()
        login_fun.signin(self.login)
        time.sleep(5)
        login_fun.find_balance(self.side_bar)
        assert self.side_bar.balance().text == "$1,681.37"

    @allure.title('add new user to real world')
    @allure.description('this test add new user to real-world web site')
    def test_signup(self):
        login_fun = login_extisting_user()
        login_fun.signup(self.login)
        login_fun.signup(self.login)
        signup = CreateNewUser()
        signup.on_user_create(self.signup)






