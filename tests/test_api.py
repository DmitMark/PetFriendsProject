# python -m pytest tests/test_api.py

from api.api_pf import PetFriendsApi
from src.schemas.pets_friends_schema import Auth_key, Pets, Pet
from src.base_response.api_pf_response import Base_pf_response
from test_data.settings import (valid_email, valid_password, invalid_email, invalid_password, user_not_found,
                                invalid_key, inv_key_mess, name_pet, type_pet, age_pet, photo_pet)


pf = PetFriendsApi()
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200
    и в результате содержится слово key при использовании валидных данных"""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.validate(Auth_key)
    response.assert_status_code(200)

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при использовании данных
    незарегистрированного пользователя(отсутствует в базе)"""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.assert_status_code(403)
    response.assert_message(user_not_found)

def test_get_api_key_for_valid_user_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при использовании неверного пароля
     пользователя"""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.assert_status_code(403)
    response.assert_message(user_not_found)

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.get_list_of_pets(auth_key, filter))
    response.validate(Pets)

def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что использовании неверного ключа
    получаем ошибку 403 и соответствующее сообщение"""

    response = Base_pf_response(pf.get_list_of_pets(invalid_key, filter))
    response.assert_status_code(403)
    response.assert_message(inv_key_mess)

def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.get_list_of_pets(auth_key, filter))
    response.validate(Pets)

def test_add_new_pet_with_valid_key(name=name_pet, animal_type=type_pet, age=age_pet, pet_photo = photo_pet):

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    response = Base_pf_response(pf.add_new_pet(auth_key, name, animal_type, age, pet_photo))
    response.assert_status_code(200)
    response.validate(Pet)
