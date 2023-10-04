# python -m pytest -v --driver chrome --driver-path c:\chromedriver.exe tests/test_all_pets_page.py

from pages.all_pets_page import AllPetsPage
from selenium.webdriver.common.action_chains import ActionChains

def test_get_all_pets_page(web_browser):


    page = AllPetsPage(web_browser)

    images = page.images.get_attribute('src')
    names = page.names.get_text()
    descriptions = page.descriptions.get_text()

    for image in images:
        assert image != ''

    for name in names:
        assert name != ''

    for description in descriptions:
        assert description != ''
        parts = description.split(',')
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0




