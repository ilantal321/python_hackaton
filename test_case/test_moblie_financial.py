import allure
import pytest

import utilities.commonOps
from workfolw.work_flow_mobile import WFM


@pytest.mark.usefixtures("init_mobile")
class TestMobile:
    @allure.title('icons count')
    @allure.description('this test counts the amount of icons in home page')
    def test01(self):
        assert utilities.commonOps.get_data('icon_count') == str(len(self.home_page.icons_list()))

    @allure.title('Check persentage calculator')
    @allure.description('this test Check 69% of 420')
    def test02(self):
        mwf=WFM()
        mwf.find_d(self.home_page)
        mwf.percentage_calc(self.pc)
        assert float(utilities.commonOps.get_data('result'))==float(self.pc.result().text)
