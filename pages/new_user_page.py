from pages.base import WebPage
from pages.elements import WebElement

class NewUserPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://petfriends.skillfactory.ru/new_user'
        super().__init__(web_driver, url)

    name = WebElement(id='name')
    email = WebElement(id='email')
    password = WebElement(id='pass')
    btn_reg = WebElement(class_name='btn.btn-success')
    btn_go_login = WebElement(xpath='/html/body/div/div/form/div[4]/a')
    alert = WebElement(class_name='alert.alert-danger')

    btn_PetFriends = WebElement(class_name='navbar-brand.header2')

