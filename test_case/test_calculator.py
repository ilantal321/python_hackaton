import allure
import pytest

import utilities.commonOps
from workfolw.calculator_wf import CWF


@pytest.mark.usefixtures("init_desktop")
class TestCalculator:

    @allure.title("calculator operations result")
    @allure.description("assures that the calculator arithmetic calculation value is the correct one")
    def test01_combo(self):
        cwf = CWF()
        cwf.test_combination(self.cp)
        assert utilities.commonOps.get_data('calculatorResult') == self.cp.CalculatorResults().text
