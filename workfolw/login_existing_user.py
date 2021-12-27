from actions.UI_action import UI_action
from allure_commons._allure import step
import utilities


class login_extisting_user:

    @step('login')
    def signin(self, login):
        UI_action.send_keys_to_elem(login.username(), "Katharina_Bernier")
        UI_action.send_keys_to_elem(login.password(), "s3cret")
        UI_action.click_on_elem(login.btn_sign_in())


    @step('print balance')
    def find_balance(self, side_bar):
        print(side_bar.balance().text)

    @step('click new user')
    def signup(self, login):
        UI_action.click_on_elem(login.link_create_user())
