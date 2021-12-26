
from selenium.webdriver.common.by import By


class PageSignin:
    def __init__(self, driver):
        self.driver = driver

    def link_create_user(self):
        return self.driver.find_element(By.LINK_TEXT, "Don't have an account? Sign Up")

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#username")

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#password")

    def remember_me(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input.PrivateSwitchBase-input-157")

    def btn_sign_in(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span[class='MuiButton-label']")

