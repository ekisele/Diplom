from pages.ui_class import UiPage
import allure

@allure.step("Проверка поиска книг и добавления в корзину")
def test_search(driver):
    uipage = UiPage(driver)
    uipage.set_cookie_policy()

    # Ввод различных значений в строку "Поиск" и проверка результата
    search_terms = [
        ('Анна Каренина', True),
        ('Beautifull girl', True),
        ('ГОГОЛЬ', True),
        ('михаил лабковский', True),
        ('2021', True),
        ('ответ  }{*?,/', True)
    ]
    
    for term, expected in search_terms:
        with allure.step(f"Поиск по термину: {term}"):
            isFound = uipage.search(term)
            assert isFound == expected

    # Добавление товара в корзину
    with allure.step("Добавление книги 'Магия утра' в корзину"):
        uipage.search('Магия утра')
        count_in_cart = uipage.AddToCart()
        assert count_in_cart == 1