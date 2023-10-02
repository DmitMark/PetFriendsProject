# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests/test_all_pets_page.py

import pytest
import time, pickle
from pages.all_pets_page import AllPetsPage
from selenium.webdriver.common.action_chains import ActionChains

def test_get_all_pets_page(web_browser):


    page = AllPetsPage(web_browser)

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'