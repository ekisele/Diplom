import requests
from conftest import authorization

class apiClass:

    def __init__(self, url):
        self.url = url

# получить токен авторизации

    def get_token(self):
        auth_headers = {
            authorization
        }
        return auth_headers
    
    def get(self, request_url, auth_headers):
        response = requests.get(self.url + request_url, headers=auth_headers)
        return response
    
    def post(self, request_url, auth_headers):
        response = requests.post(self.url + request_url, headers=auth_headers)
        return response






