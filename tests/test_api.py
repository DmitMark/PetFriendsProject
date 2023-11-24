from api.api import PetFriendsApi
from settings import valid_email, valid_password, invalid_email, invalid_password

pf = PetFriendsApi()
def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_user(email = invalid_email, password = invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при использовании данных
    незарегистрированного пользователя(отсутствует в базе) и в ответе нет слова key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_valid_user_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при использовании неверного пароля
     пользователя(отсутствует в базе) и в ответе нет слова key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0