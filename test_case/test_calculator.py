import pytest

import utilities.commonOps
from workfolw.calculator_wf import CWF


@pytest.mark.usefixtures("init_desktop")
class TestCalculator:

    def test01_combo(self):
        cwf = CWF()
        cwf.test_combination(self.cp)
        assert utilities.commonOps.get_data('calculatorResult') == self.cp.CalculatorResults().text
