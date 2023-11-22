# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests\test_ui_1_auth_page.py
# python -m pytest -v --driver Firefox --driver-path C:\geckodriver.exe tests\test_ui_1_auth_page.py

import pytest
import pickle
import os
from pages.auth_page import AuthPage


def test_valid_auth(web_browser):
    ### тест авторизации с валидными данными ###

    page = AuthPage(web_browser)

    page.email.send_keys('nukdy@mailto.plus')

    page.password.send_keys('123')

    page.btn.click()

    page.wait_page_loaded(timeout=5)

    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(page.get_cookies(), cookies)


    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

def test_invalid_mail_auth(web_browser):
    ### тест авторизации с невалидным email ###

    page = AuthPage(web_browser)

    page.email.send_keys('nukdy@mailto.com')
    page.password.send_keys('123')
    page.btn.click()
    page.wait_page_loaded(timeout=5)

    assert page.alert.find() is not None

def test_invalid_mail_auth(web_browser):
    ### тест авторизации с невалидным паролем ###

    page = AuthPage(web_browser)

    page.email.send_keys('nukdy@mailto.plus')
    page.password.send_keys('1234')
    page.btn.click()
    page.wait_page_loaded(timeout=5)

    assert page.alert.find() is not None
