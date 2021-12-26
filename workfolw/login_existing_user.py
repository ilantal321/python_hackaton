import time


class login_extisting_user:
    def signin(self, login):
        login.username().send_keys("Katharina_Bernier")
        login.password().send_keys("s3cret")
        login.btn_sign_in().click()

    def find_balance(self, side_bar):
        print(side_bar.balance().text)

    def signup(self, login):
        login.link_create_user().click()
