# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests/test_auth_page.py
# python -m pytest -v --driver Firefox --driver-path C:\geckodriver.exe tests/test_auth_page.py

import pytest
import pickle
import os
from pages.auth_page import AuthPage


def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('nukdy@mailto.plus')

    page.password.send_keys('123')

    page.btn.click()

    page.wait_page_loaded(timeout=10)

    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(page.get_cookies(), cookies)


    # assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'
    assert 'domain' in page.get_cookies()
