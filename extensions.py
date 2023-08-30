import requests
import json
from config import keys


class APIException(Exception):
    pass


class ValueConverter():
    @staticmethod
    def get_price(quote: str, base: str, amount: int):

        if quote == base:
            raise APIException("Невозможно перевести одинаковые валюты")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Воспользуйтесь /values для помощи. \nВалюты <{quote}> нет в списке, повторите попытку: ')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Воспользуйтесь /values для помощи. \nВалюты <{base}> нет в списке, повторите попытку: ')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Это -> <{amount}> неверный ввод. Введите необходимое количество в цифрах: ')

        r = requests.get(
            f'https://api.currencyapi.com/v3/latest?apikey=cur_live_H8thNNLYB4HvUKqfEv8YCe3t3Jauxrl7mEpi8GSh&currencies={keys[quote]}&base_currency={keys[base]}')
        response_data = json.loads(r.content)
        value = response_data['data'][keys[quote]]['value']
        converted_amount = value * float(amount)
        return converted_amount