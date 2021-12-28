from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def clearBtn(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='clearButton']")

    def zero(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num0Button']")

    def one(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num1Button']")

    def two(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num2Button']")

    def three(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num3Button']")

    def four(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num4Button']")

    def five(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num5Button']")

    def six(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num6Button']")

    def seven(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num7Button']")

    def eight(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num8Button']")

    def nine(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num9Button']")

    def plusButton(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='plusButton']")

    def minusButton(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='minusButton']")

    def multiplyButton(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='multiplyButton']")

    def equalButton(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='equalButton']")

    def CalculatorResults(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")
