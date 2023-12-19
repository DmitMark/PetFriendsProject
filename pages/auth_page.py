from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://petfriends.skillfactory.ru/login'
        super().__init__(web_driver, url)

    email = WebElement(id='email')
    password = WebElement(id='pass')
    btn_login = WebElement(class_name='btn.btn-success')
    alert = WebElement(class_name='alert.alert-danger')
    btn_new_user = WebElement(xpath='/html/body/div/div/form/div[3]/a')

    btn_PetFriends = WebElement(class_name='navbar-brand.header2')