from selenium.webdriver.common.by import By


class PageSignup:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#firstName")

    def last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#firstName")

    def user_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#username")

    def password_user(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#password")

    def confirm_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#confirmPassword")

    def btn_sign_up(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".makeStyles-paper-174 button")

    def link_back_signin(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/signin']")
