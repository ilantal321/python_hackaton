import allure

from actions.UI_action import UI_action


class CWF:
    @allure.step("enters the calculation input")
    def test_combination(self,cp):
        UI_action.click_on_elem(cp.seven())
        UI_action.click_on_elem(cp.multiplyButton())
        UI_action.click_on_elem(cp.nine())
        UI_action.click_on_elem(cp.plusButton())
        UI_action.click_on_elem(cp.one())
        UI_action.click_on_elem(cp.equalButton())
        UI_action.click_on_elem(cp.minusButton())
        UI_action.click_on_elem(cp.eight())
        UI_action.click_on_elem(cp.equalButton())