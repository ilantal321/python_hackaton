from actions.UI_action import UI_action
from allure_commons._allure import step

class CreateNewUser:
    @step('add new user to web site')
    def on_user_create(self, signup):
        UI_action.send_keys_to_elem(signup.first_name(), "Dolev")
        UI_action.send_keys_to_elem(signup.last_name(), "Hanan")
        UI_action.send_keys_to_elem(signup.user_name(), "Ilan")
        UI_action.send_keys_to_elem(signup.password_user(), "123456")
        UI_action.send_keys_to_elem(signup.confirm_password(), "123456")
        UI_action.click_on_elem(signup.btn_sign_up())
