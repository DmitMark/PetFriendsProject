# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests\test_ui_2_new_user_page.py
# python -m pytest -v --driver Firefox --driver-path C:\geckodriver.exe tests\test_ui_2_new_user_page.py

from pages.new_user_page import NewUserPage
from test_data.settings import valid_email, valid_password

def test_new_user_reg(web_browser):
    """Регистрация нового пользователя"""

    page = NewUserPage(web_browser)
    page.name.send_keys('Bob')
    page.email.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.btn_reg.click()

    page.wait_page_loaded(timeout=5)

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

def test_new_user_reg_with_ivalid_email(web_browser):
    """Регистрация нового пользователя c невалидным email"""

    page = NewUserPage(web_browser)
    page.name.send_keys('Bob')
    page.email.send_keys('nukdy@mailto')
    page.password.send_keys(valid_password)
    page.btn_reg.click()

    page.wait_page_loaded(timeout=5)

    assert page.alert.find() is not None

def test_go_to_login_btn(web_browser):
    """Переход на страницу авторизации"""

    page = NewUserPage(web_browser)
    page.btn_go_login.click()

    page.wait_page_loaded(timeout=5)

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/login'

def test_button_pet_friends(web_browser):
    """Кнопка 'PetFriend' """

    page = NewUserPage(web_browser)
    page.btn_PetFriends.click()
    page.wait_page_loaded(timeout=5)

    assert 'Социальная сеть для любителей животных' in page.get_page_source()