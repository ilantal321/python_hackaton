from actions.UI_action import UI_action
from allure_commons._allure import step
import utilities


class login_extisting_user:

    @step('login')
    def signin(self, login, mydb):
        result = self.patch_user(mydb)
        UI_action.send_keys_to_elem(login.username(), result[0][0])
        UI_action.send_keys_to_elem(login.password(), result[0][1])
        UI_action.click_on_elem(login.btn_sign_in())

    @step
    def patch_user(self, mydb):
        query = "SELECT username, password FROM Usernames limit 1"
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result



    # @step('print balance')
    # def find_balance(self, side_bar):
    #     print(side_bar.balance().text)

    @step('click new user')
    def signup(self, login):
        UI_action.click_on_elem(login.link_create_user())
