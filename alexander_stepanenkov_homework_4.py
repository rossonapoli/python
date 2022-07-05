# Задача 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с
# денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(cur):
    session = requests.Session()

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'}
    params = {
        'country' : 'us',
        'apiKey' : 'f23fc1bb0977426692953d5c2003028d'
    }

    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = session.get(url, headers = headers)
    response = response.json()
    response = response['Valute']

    if cur in response:
        print(response[cur]['Value'])
    else:
        return None

# Задача 4*. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import utils, sys

utils.currency_rates(sys.argv[1])
