from pages.ui_class import UiPage

def test_search(driver):

    uipage = UiPage(driver)
    uipage.set_cookie_policy()

    # ввод разных значений в строку "Поиск"
    isFound = uipage.search('Анна Каренина')
    assert isFound == True

    isFound = uipage.search('Beautifull girl')
    assert isFound == True

    isFound = uipage.search('ГОГОЛЬ')
    assert isFound == True

    isFound = uipage.search('михаил лабковский')
    assert isFound == True

    isFound = uipage.search('2021')
    assert isFound == True

    isFound = uipage.search('ответ }{*?,/')
    assert isFound == True

    # добавление в корзину
    uipage.search('Магия утра')
    count_in_cart = uipage.AddToCart()
    assert count_in_cart == 1