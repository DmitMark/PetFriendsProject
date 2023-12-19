# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests\test_ui_1_auth_page.py
# python -m pytest -v --driver Firefox --driver-path C:\geckodriver.exe tests\test_ui_1_auth_page.py

import pickle
from pages.auth_page import AuthPage
from test_data.settings import valid_email, valid_password


def test_valid_auth(web_browser):
    """Авторизация с валидными данными"""

    page = AuthPage(web_browser)
    page.email.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.btn_login.click()

    page.wait_page_loaded(timeout=5)

    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(page.get_cookies(), cookies)


    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

def test_invalid_mail_auth(web_browser):
    """Авторизация с данными незарегистрированного пользователя"""

    page = AuthPage(web_browser)

    page.email.send_keys('nukdyt@mailto.plus')
    page.password.send_keys(valid_password)
    page.btn_login.click()
    page.wait_page_loaded(timeout=5)

    assert page.alert.find() is not None

def test_invalid_pass_auth(web_browser):
    """ Авторизация с невалидным паролем"""

    page = AuthPage(web_browser)

    page.email.send_keys('nukdy@mailto.plus')
    page.password.send_keys('1234')
    page.btn_login()
    page.wait_page_loaded(timeout=5)

    assert page.alert.find() is not None

def test_button_new_user(web_browser):
    """Переход на страницу регистрации"""

    page = AuthPage(web_browser)
    page.btn_new_user.click()
    page.wait_page_loaded(timeout=5)

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/new_user'


def test_button_pet_friends(web_browser):
    """Кнопка 'PetFriend' """

    page = AuthPage(web_browser)
    page.btn_PetFriends.click()
    page.wait_page_loaded(timeout=5)

    assert 'Социальная сеть для любителей животных' in page.get_page_source()
