from pages.api_class import ApiClass
import allure

api = ApiClass("https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?phrase=")

@allure.step("Поиск по полному названию книги")
def test_search_full_description():
    auth_headers = api.get_token()
    response = api.get('Люби', auth_headers)
    assert response.status_code == 200

@allure.step("Поиск по названию книги с опечаткой")
def test_search_description_mistake():
    auth_headers = api.get_token()
    response = api.get('Не най', auth_headers)
    assert response.status_code == 200

@allure.step("Поиск по фамилии автора с ошибкой")
def test_search_author_mistake():
    auth_headers = api.get_token()
    response = api.get('Лабковскиий', auth_headers)
    assert response.status_code == 200

@allure.step("Поиск с использованием спецсимволов")
def test_search_symbols():
    auth_headers = api.get_token()
    response = api.get('1966', auth_headers)
    assert response.status_code == 200

@allure.step("Негативный тест: отправка POST вместо GET")
def test_search_post_NEG():
    auth_headers = api.get_token()
    response = api.post('1977', auth_headers)
    assert response.status_code == 405

@allure.step("Негативный тест: поиск по пустому полю")
def test_search_blank_NEG():
    auth_headers = api.get_token()
    response = api.post('', auth_headers)
    assert response.status_code == 405