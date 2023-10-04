# python -m pytest -v --driver chrome --driver-path c:\chromedriver.exe tests\test_my_pets.py

from pages.my_pets_page import MyPetsPage

def test_get_my_pets_page(web_browser):

    page = MyPetsPage(web_browser)
    page.btn_my_pets.click()
    # переходим на страницу мои питомцы

    page.wait_page_loaded()
    # добавляем явное ожидание элементов на странице(метод прописан в pages.base в классе WebPage

    data_pets = page.data_user.get_text()
    for data in data_pets:
        if 'Питомцев' in data:
            info = data.split(':')
            pets_count = int(info[1])
    # получаем количество моих питомцев

    my_pets_images = page.images_my_pet.get_attribute('src')
    my_pets_names = page.name_my_pet.get_text()
    my_pets_breeds = page.breed_my_pet.get_text()
    my_pets_years = page.year_my_pet.get_text()



    assert len(page.pet.find()) == 12
    # проверяем все ли питомцы отображаются на странице
    assert len(my_pets_images) >5
    # проверяем что больше половины питомцев имеют фото
    assert len(my_pets_names) == 12
    for my_pets_name in my_pets_names:
        assert len(my_pets_name) > 0
    # проверяем что у всех питомцев есть имя

    unique_names = set(my_pets_names)
    assert len(unique_names) == my_pets_names
    # проверяем что все имена питомцев уникальны

    for my_pets_year in my_pets_years:
        assert len(my_pets_year) > 0
    # проверяем что у всех питомцев есть значени возраста

    for my_pets_breed in my_pets_breeds:
        assert len(my_pets_breed) > 0
    # проверяем что у всех питомцев есть значени парода





