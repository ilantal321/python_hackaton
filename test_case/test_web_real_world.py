import time

import pytest

from workfolw.create_signup import CreateNewUser
from workfolw.login_existing_user import login_extisting_user


@pytest.mark.usefixtures("init_web")
class TestSignIn:
    def test_login(self):
        login_fun = login_extisting_user()
        login_fun.signin(self.login)
        time.sleep(5)
        login_fun.find_balance(self.side_bar)
        assert self.side_bar.balance().text == "$1,681.37"

    def test_signup(self):
        login_fun = login_extisting_user()
        login_fun.signup(self.login)
        time.sleep(5)
        signup = CreateNewUser()
        signup.on_user_create(self.signup)






