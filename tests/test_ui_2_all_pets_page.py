# python -m pytest -v --driver chrome --driver-path c:\chromedriver.exe --alluredir=allureress tests/test_ui_2_all_pets_page.py

from pages.all_pets_page import AllPetsPage

def test_get_all_pets_page(web_browser):
    # тест наличия у всех карточек фото,имени и описания


    page = AllPetsPage(web_browser)
    page.implicitly_wait()

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




