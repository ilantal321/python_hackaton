from selenium.webdriver.common.by import By

import utilities.commonOps
from actions.UI_action import UI_action

class WFM:
    def find_d(self,hp):
        UI_action.click_on_elem(hp.btn_percent_calc())

    def percentage_calc(self,pc):
        UI_action.send_keys_to_elem(pc.input_percent(),utilities.commonOps.get_data('input_percent'))
        UI_action.send_keys_to_elem(pc.input_amount(),utilities.commonOps.get_data('input_amount'))




