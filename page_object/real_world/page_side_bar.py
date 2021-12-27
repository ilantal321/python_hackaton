from selenium.webdriver.common.by import By


class PageSideBar:
    def __init__(self, driver):
        self.driver = driver

    def balance(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h6[data-test='sidenav-user-balance']")

    def btn_logout(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[data-test='sidenav-signout']")

    def btn_notification(self):
        return self.driver.find_element(By.CSS_SELECTOR,"a[data-test='sidenav-notifications']")

