import time
import allure
import pytest

from workfolw.create_signup import CreateNewUser
from workfolw.login_existing_user import login_extisting_user
from workfolw.work_flow_web import WFW_app


@pytest.mark.usefixtures("init_web")
class TestSignIn:
    @allure.title('add new user to real world')
    @allure.description('this test add new user to real-world web site')
    @pytest.mark.order(1)
    def test_01signup(self):
        login_fun = login_extisting_user()
        login_fun.signup(self.login)
        login_fun.signup(self.login)
        signup = CreateNewUser()
        signup.on_user_create(self.signup)
        time.sleep(1)
        assert self.driver.current_url == 'http://localhost:4000/signin'

    @allure.title('Check balance to extisting user')
    @allure.description('this test Check balance to exsisting user task')
    @pytest.mark.order(2)
    def test_02login(self):
        time.sleep(1)
        login_fun = login_extisting_user()
        login_fun.signin(self.login)
        time.sleep(5)
        login_fun.find_balance(self.side_bar)
        assert self.side_bar.balance().text == "$1,681.37"

    @allure.title('Check notification title')
    @allure.description('this test Check notification title')
    @pytest.mark.order(3)
    def test_03notification_title(self):
        time.sleep(1)
        wfa = WFW_app()
        wfa.check_notification(self.side_bar)
        time.sleep(1)
        assert self.notifiaction.title().text == 'Notifications'

    @allure.title('Check notification list size')
    @allure.description('this test Check notification list size')
    @pytest.mark.order(4)
    def test_04notification_size(self):
        print('sbfeukjkhvesrfvesrukg')
        assert len(self.notifiaction.notification_list()) == 8

    @allure.title('Check logout')
    @allure.description('this test Check button logout')
    @pytest.mark.order(5)
    def test_05logout(self):
        print('plplplplplpl')
        time.sleep(1)
        wfa = WFW_app()
        wfa.logout(self.side_bar)
        time.sleep(1)
        assert self.driver.current_url == 'http://localhost:4000/signin'
