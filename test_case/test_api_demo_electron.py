import pytest

import utilities.commonOps


@pytest.mark.usefixtures("init_electron")
class TestApiJson:

    def test01(self):
        assert len(self.epo.category()) == int(utilities.commonOps.get_data('ElectronCategoryResult'))
