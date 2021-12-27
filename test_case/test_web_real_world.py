import time
import allure
import pytest
import smart_assertions
from smart_assertions import soft_assert, verify_expectations

from workfolw.create_signup import CreateNewUser
from workfolw.login_existing_user import login_extisting_user
from workfolw.work_flow_web import WFW_app


@pytest.mark.usefixtures("init_web")
class TestSignIn:
    @pytest.mark.parametrize(
        "f_name,l_name,u_name, password,c_password",
        [
            ("dolev", "sigon", "dolev123",'123456','123456'),
            ("hanan", "dorfman", "hanan123",'1234456','1234456'),
            ("ilan", "tal", "ilantal",'6486468','6486468')
        ]
    )
    @allure.title('add new user to real world')
    @allure.description('this test add new user to real-world web site')
    @pytest.mark.order(1)
    def test_01signup(self,f_name,l_name,u_name,password,c_password):
        login_fun = login_extisting_user()
        login_fun.signup(self.login)
        login_fun.signup(self.login)
        signup = CreateNewUser()
        signup.on_user_create(self.signup,f_name,l_name,u_name,password,c_password)
        time.sleep(1)
        assert self.driver.current_url == 'http://localhost:4000/signin'


    @allure.title('Check balance to extisting user')
    @allure.description('this test Check balance to exsisting user task')
    @pytest.mark.order(2)
    def test_02login(self):
        time.sleep(1)
        login_fun = login_extisting_user()
        login_fun.signin(self.login, 'Katharina_Bernier', 's3cret')
        time.sleep(5)
        login_fun.find_balance(self.side_bar)
        assert self.side_bar.balance().text == '$1,681.37'


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
        assert len(self.notifiaction.notification_list()) == 8

    @allure.title('Check logout')
    @allure.description('this test Check button logout')
    @pytest.mark.order(5)
    def test_05logout(self):
        time.sleep(1)
        wfa = WFW_app()
        wfa.logout(self.side_bar)
        time.sleep(1)
        assert self.driver.current_url == 'http://localhost:4000/signin'
