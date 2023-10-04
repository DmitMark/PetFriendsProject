from pages.all_pets_page import AllPetsPage
from pages.elements import WebElement, ManyWebElements
class MyPetsPage(AllPetsPage):

    data_user = WebElement(xpath='/html/body/div[1]/div/div[1]/text()[1]')
    pet = ManyWebElements(xpath='//*[@id="all_my_pets"]/table/tbody/tr')
    images_my_pet = ManyWebElements(xpath='//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/th[1]/img')
    name_my_pet= ManyWebElements(xpath='//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td[1]')
    breed_my_pet = ManyWebElements(xpath='//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td[2]')
    year_my_pet = ManyWebElements(xpath='//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td[3]')

