from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def icons_list(self):
        return self.driver.find_elements(By.ID,'icon')

    def btn_percent_calc(self):
        return self.driver.find_element(By.XPATH,"//*[@text='Percentage Calculator']")