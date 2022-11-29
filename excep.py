import requests
import json
from config import allval


class ConvertionException(Exception):
    pass
class Converter:
    @staticmethod
    def convert(val1, val2, cash):

        if val1 == val2:
            raise ConvertionException('Введите валюту перевода')

        try:
            tiker1 = allval[val1.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {val1}')

        try:
            tiker2 = allval[val2.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {val2}')

        try:
            cash = float(cash)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество {cash}')

        r = f'https://api.apilayer.com/exchangerates_data/convert?to={tiker1}&from={tiker2}&amount={cash}'
        payload = {}
        headers = {
            "apikey": "SDj1gjFCwsUAbStqkm2BsRAxkuAZg6lg"
        }
        response = requests.request("GET", r, headers=headers, data=payload)

        response = json.loads(response.content)
        print(response)
        pr = response.get('result', 'Конвертация недоступна')
        pr = round(pr, 3)
        message = f'Цена {cash} {val2} в {val1}: {pr}'
        return message


