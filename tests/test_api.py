# python -m pytest tests/test_api.py
import json.decoder

from api.api import PetFriendsApi
from src.schemas.pets_friends_schema import Auth_key, Pets, Pet
from src.base_response.api_pf_response import Base_pf_response
from settings import valid_email, valid_password, invalid_email, invalid_password

pf = PetFriendsApi()
def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.validate(Auth_key)
    response.assert_status_code(200)


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при использовании данных
    незарегистрированного пользователя(отсутствует в базе)"""

    response = Base_pf_response(pf.get_api_key(email, password))
    response.assert_status_code(403)

#
#
# def test_get_api_key_for_valid_user_invalid_password(email=valid_email, password=invalid_password):
#     """ Проверяем что запрос api ключа возвращает статус 403 при использовании неверного пароля
#      пользователя(отсутствует в базе)"""
#
#     assert pf.get_api_key(email,password).status_code == 403
#     try:
#         assert 'This user wasn&#x27;t found in database' in pf.get_api_key(email, password).json()
#     except json.decoder.JSONDecodeError:
#         assert 'This user wasn&#x27;t found in database' in pf.get_api_key(email, password).text
#
#
def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    result = pf.get_list_of_pets(auth_key, filter)
    response = Base_pf_response(result)
    response.validate(Pets)


def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой."""

    auth_key = pf.get_api_key(valid_email, valid_password).json()
    result = pf.get_list_of_pets(auth_key, filter)
    response = Base_pf_response(result)
    response.validate(Pets)