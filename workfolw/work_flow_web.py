import time

import allure
import pytest
from smart_assertions import soft_assert

from actions.UI_action import UI_action
from workfolw.login_existing_user import login_extisting_user


class WFW_app:

    @allure.step("logs out")
    def logout(self, sidebar):
        UI_action.click_on_elem(sidebar.btn_logout())

    @allure.step("clicks on the notification tag")
    def check_notification(self, sidebar):
        UI_action.click_on_elem(sidebar.btn_notification())

    @allure.step("graphics elements")
    def sign_eyes(self,driver,eyes):
        try:
            eyes.open(driver,"hackhton1", "check login")
            eyes.check_window('Initial Screen Shot')
            eyes.close()
        except:
            print()
