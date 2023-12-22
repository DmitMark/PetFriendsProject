# python -m pytest tests/test_api.py

from api.api_pf import PetFriendsApi
from src.schemas.pets_friends_schema import Auth_key, Pets, Pet
from src.base_response.api_pf_response import Base_pf_response
from test_data.settings import (valid_email, valid_password, invalid_email, invalid_password, user_not_found,
                                invalid_key, inv_key_mess, name_pet, type_pet, age_pet, age_pet_invalid,
                                photo_pet, photo_pet_invalid)


pf = PetFriendsApi()
def test_get_api_key(email=valid_email, password=valid_password):
    """ Запрос api key с использованием валидных данных."""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.validate(Auth_key)
    response.assert_status_code(200)

def test_get_api_key_with_invalid_user(email=invalid_email, password=invalid_password):
    """Запрос api key с использованием невалидных данных(пользователь
    отсутствует в базе)."""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.assert_status_code(403)
    response.assert_message(user_not_found)

def test_get_api_key_with_invalid_password(email=valid_email, password=invalid_password):
    """ Запрос api key с использованием невалидных данных(неверный пароль)."""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.assert_status_code(403)
    response.assert_message(user_not_found)

def test_get_all_pets(get_api_key, filter=''):
    """ Запрос списка всех питомцев с использованием валидных данных."""

    # auth_key = pf.get_api_key(valid_email, valid_password).json()
    auth_key = get_api_key
    response = Base_pf_response(pf.get_list_of_pets(auth_key, filter))
    response.validate(Pets)

def test_get_all_pets_with_invalid_key(filter=''):
    """Запрос списка всех питомцев с использованием неверного ключа."""

    response = Base_pf_response(pf.get_list_of_pets(invalid_key, filter))
    response.assert_status_code(403)
    response.assert_message(inv_key_mess)

def test_get_my_pets(get_api_key,filter='my_pets'):
    """Запрос списка питомцев пользователя с использованием валидных данных."""

    # auth_key = pf.get_api_key(valid_email, valid_password).json()
    auth_key = get_api_key
    response = Base_pf_response(pf.get_list_of_pets(auth_key, filter))
    response.validate(Pets)

def test_add_new_pet(name=name_pet, animal_type=type_pet, age=age_pet, pet_photo = photo_pet):
    """Добавление нового питомца с использованием валидных данных"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.add_new_pet(auth_key, name, animal_type, age, pet_photo))
    response.assert_status_code(200)
    response.validate(Pet)

def test_add_new_pet_with_invalid_key(name=name_pet, animal_type=type_pet, age=age_pet, pet_photo = photo_pet):
    """Добавление нового питомца с использованием невалидного ключа."""

    response = Base_pf_response(pf.add_new_pet(invalid_key, name, animal_type, age, pet_photo))
    response.assert_status_code(403)

def test_add_new_pet_with_invalid_photo(name=name_pet, animal_type=type_pet, age=age_pet, pet_photo = photo_pet_invalid):
    """Добавление нового питомца с использованием невалидного файла фото."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.add_new_pet(auth_key, name, animal_type, age, pet_photo))
    response.assert_status_code(400)

def test_add_new_pet_with_invalid_age(name=name_pet, animal_type=type_pet, age=age_pet_invalid, pet_photo = photo_pet_invalid):
    """Добавление нового питомца с использованием невалидного типа данных в поле "возраст"."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.add_new_pet(auth_key, name, animal_type, age, pet_photo))
    response.assert_status_code(400)

def test_add_pet_photo(pet_photo = photo_pet):
    """Добавление фото питомца."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key,'Jack', 'dog','5','test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.add_photo_pet(auth_key, pet_id, pet_photo))
    response.assert_status_code(200)
    response.validate(Pet)

def test_add_pet_photo_with_invalid_key(pet_photo = photo_pet):
    """Добавление фото питомца с использованием невалидного ключа."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key,'Jack', 'dog','5','test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.add_photo_pet(invalid_key, pet_id, pet_photo))
    response.assert_status_code(403)

def test_add_pet_photo_with_invalid_data(pet_photo = photo_pet_invalid):
    """Добавление фото питомца с использованием невалидного файла фото."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key,'Jack', 'dog','5','test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.add_photo_pet(auth_key, pet_id, pet_photo))
    response.assert_status_code(400)

def test_delet_pet():
    """Удаление питомца"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.delete_pet(auth_key, pet_id))
    response.assert_status_code(200)

def test_delet_pet_with_invalid_key():
    """Удаление питомца с использованием невалидного ключа"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.delete_pet(invalid_key, pet_id))
    response.assert_status_code(403)

def test_delet_pet_with_invalid_pet_id():
    """Удаление питомца из списка всех питомцев"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    pets = pf.get_list_of_pets(auth_key, '').json()

    if len(pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        pets = pf.get_list_of_pets(auth_key, '')

    pet_id = pets['pets'][0]['id']
    response = Base_pf_response(pf.delete_pet(invalid_key, pet_id))
    response.assert_status_code(400)

def test_update_pet_with_valid_key(name = 'Tom', animal_type = 'cat', age = '8'):
    """Изменение информации о питомце"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.update_pet_info(auth_key, pet_id, name, animal_type, age))
    response.assert_status_code(200)
    response.validate(Pet)


def test_update_pet_with_invalid_key(name='Tom', animal_type='cat', age='8'):
    """Изменение информации о питомце с использованием невалидного ключа"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    my_pets = pf.get_list_of_pets(auth_key, 'my_pets').json()

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    response = Base_pf_response(pf.update_pet_info(invalid_key, pet_id, name, animal_type, age))
    response.assert_status_code(200)
    response.validate(Pet)


def test_update_pet_with_invalid_pet_id(name='Tom', animal_type='cat', age='8'):
    """Изменение информации о питомце из списка всех питомцев"""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    pets = pf.get_list_of_pets(auth_key, '').json()

    if len(pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Jack', 'dog', '5', 'test_data/dog1.jpg')
        pets = pf.get_list_of_pets(auth_key, '')

    pet_id = pets['pets'][0]['id']
    response = Base_pf_response(pf.update_pet_info(auth_key, pet_id, name, animal_type, age))
    response.assert_status_code(400)
