from selenium.webdriver.common.by import By


class APIDemoElectron:

    def __init__(self, driver):
        self.driver = driver

    def category(self):
        return self.driver.find_elements(By.CLASS_NAME, "nav-category")
