from allure_commons._allure import step
class UI_action:
    @step('click element')
    def click_on_elem(elem):
        elem.click()

    @step('send keys to element')
    def send_keys_to_elem(elem, text):
        elem.send_keys(text)
