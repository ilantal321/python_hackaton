import pytest

import utilities.commonOps
from workfolw.work_flow_mobile import WFM


@pytest.mark.usefixtures("init_mobile")
class TestMobile:

    def test01(self):
        assert utilities.commonOps.get_data('icon_count') == str(len(self.home_page.icons_list()))
    def test02(self):
        mwf=WFM()
        mwf.find_d(self.home_page)
        mwf.percentage_calc(self.pc)
        assert float(utilities.commonOps.get_data('result'))==float(self.pc.result().text)
