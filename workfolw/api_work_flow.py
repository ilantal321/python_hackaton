import allure
import requests


class ApiWorkFlow:
    @allure.step("gets the list length")
    def size_elem(self,url):
        response = requests.get(url + '/posts')
        json = response.json()
        return len(json)

    @allure.step("gets the first object at the list")
    def object_data(self,url):
        response = requests.get(url + '/posts')
        json = response.json()
        return json[0]



