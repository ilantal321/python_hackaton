from selenium.webdriver.common.by import By


class PageNotification:
    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.find_element(By.TAG_NAME, "h2")

    def notification_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul[data-test='notifications-list'] li")
