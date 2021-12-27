from selenium.webdriver.common.by import By


class PercentagePage:

    def __init__(self, driver):
        self.driver = driver

    def input_percent(self):
        return self.driver.find_element(By.ID,'yPercentInput')

    def input_amount(self):
        return self.driver.find_element(By.ID,'xAmountInput')

    def result(self):
        return self.driver.find_element(By.ID,'percentValueResult')