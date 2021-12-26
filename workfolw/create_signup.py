import time


class CreateNewUser:
    def on_user_create(self, signup):
        signup.first_name().send_keys("Dolev")
        signup.last_name().send_keys("Hanan")
        signup.user_name().send_keys("Ilan")
        signup.password_user().send_keys("123456")
        signup.confirm_password().send_keys("123456")
        signup.btn_sign_up().click()


