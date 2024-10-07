import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    webDriver = webdriver.Chrome()
    webDriver.maximize_window()
    yield webDriver
    webDriver.quit()


authorization = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjE2NzQ5NTMyLCJpYXQiOjE3MjgyMzQzMDIsImV4cCI6MTcyODIzNzkwMiwidHlwZSI6MjB9.vL7C0G31w9OxVJQnbJuTfMEBXdDGv6zmnkbTTUu6XOE'
