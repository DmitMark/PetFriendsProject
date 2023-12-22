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



    btn_my_pets = WebElement(xpath='//*[@id="navbarNav"]/ul[1]/li[1]/a[1]')
    btb_all_pets = WebPage(css_selector='div#navbarNav > ul > li:nth-of-type(2) > a')
    title = WebElement(xpath='//body/div[1]/div[1]/h1[1]')

    images = ManyWebElements(css_selector='.card-deck.card-img-top')
    names = ManyWebElements(css_selector='.card-deck.card-title')
    descriptions = ManyWebElements(css_selector='.card-deck.card-title')




