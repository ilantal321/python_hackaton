import allure
import pytest
import requests
import smart_assertions
from smart_assertions import soft_assert, verify_expectations

import utilities.commonOps
from workfolw.api_work_flow import ApiWorkFlow


@pytest.mark.usefixtures("init_api")
class TestApiJson:

    @allure.title("list size")
    @allure.description("checks that the list size is 1")
    def test01(self):
        apiwe = ApiWorkFlow()
        size = apiwe.size_elem(self.url)
        assert 1 == size

    @allure.title("object values")
    @allure.description("compares the returned object values to a given set")
    def test02(self):
        apiwe = ApiWorkFlow()
        object_data = apiwe.object_data(self.url)
        for i in object_data.keys():
            soft_assert(str(object_data[i]) == str(utilities.commonOps.get_data(i)))
        verify_expectations()
