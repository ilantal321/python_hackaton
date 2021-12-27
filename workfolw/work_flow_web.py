import time

import pytest
from smart_assertions import soft_assert

from actions.UI_action import UI_action
from workfolw.login_existing_user import login_extisting_user


class WFW_app:

    def logout(self, sidebar):
        UI_action.click_on_elem(sidebar.btn_logout())

    def check_notification(self, sidebar):
        UI_action.click_on_elem(sidebar.btn_notification())


