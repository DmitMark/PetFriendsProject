import os,pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements



class AllPetsPage(WebPage):

    def __init__(self, web_driver, url = ''):
        url = 'https://petfriends.skillfactory.ru/'
        super().__init__(web_driver, url)
        with open('my_cookies.txt', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)
            web_driver.refresh();



    btn_my_pets = WebElement(XPATH='//*[@id="navbarNav"]/ul[1]/li[1]/a[1]')
    #
    # password = WebElement(id='pass')
    #
    # btn = WebElement(class_name='btn.btn-success')




