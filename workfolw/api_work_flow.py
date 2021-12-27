import requests


class ApiWorkFlow:
    def size_elem(self,url):
        response = requests.get(url + '/posts')
        json = response.json()
        return len(json)

    def object_data(self,url):
        response = requests.get(url + '/posts')
        json = response.json()
        return json[0]



