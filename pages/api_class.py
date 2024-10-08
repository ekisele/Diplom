import requests
# from conftest import authorization

class apiClass:

    def __init__(self, url):
        self.url = url

# получить токен авторизации

    def get_token(self):
        auth_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjE2NzQ5NTMyLCJpYXQiOjE3MjgyMzQzMDIsImV4cCI6MTcyODIzNzkwMiwidHlwZSI6MjB9.vL7C0G31w9OxVJQnbJuTfMEBXdDGv6zmnkbTTUu6XOE'
        }
        return auth_headers
    
    def get(self, request_url, auth_headers):
        response = requests.get(self.url + request_url, headers=auth_headers)
        return response
    
    def post(self, request_url, auth_headers):
        response = requests.post(self.url + request_url, headers=auth_headers)
        return response






