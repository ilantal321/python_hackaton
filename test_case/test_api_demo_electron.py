import allure
import pytest

import utilities.commonOps


@pytest.mark.usefixtures("init_electron")
class TestApiJson:

    @allure.title("electron test")
    @allure.description("compares sidebar elements count to a known value")
    def test01(self):
        assert len(self.epo.category()) == int(utilities.commonOps.get_data('ElectronCategoryResult'))
