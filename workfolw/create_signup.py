from actions.UI_action import UI_action
from allure_commons._allure import step

class CreateNewUser:
    @step('add new user to web site')
    def on_user_create(self, signup,f_name,l_name,u_name,password,c_password):
        UI_action.send_keys_to_elem(signup.first_name(), f_name)
        UI_action.send_keys_to_elem(signup.last_name(), l_name)
        UI_action.send_keys_to_elem(signup.user_name(), u_name)
        UI_action.send_keys_to_elem(signup.password_user(), password)
        UI_action.send_keys_to_elem(signup.confirm_password(), c_password)
        UI_action.click_on_elem(signup.btn_sign_up())
