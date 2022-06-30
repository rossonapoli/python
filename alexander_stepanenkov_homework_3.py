import  random

# Задача 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(num):
    numbers = {
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль'
    }
    if num in numbers:
        return numbers[num]
    else:
        return None

num = input()
print(num_translate(num))

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    new_dict = {}
    new_list = list(names)
    print(new_list)

    for i in new_list:
        new_dict[i[0]] = new_dict.get(i[0], []) + [i]

    print(new_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

def get_jokes(num):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = 0
    jokes = []
    while i < num:

        a_nouns = random.randint(0, len(nouns) - 1)
        jokes.append(nouns[a_nouns])

        a_adverbs = random.randint(0, len(adverbs) - 1)
        jokes.append(adverbs[a_adverbs])

        a_adjectives = random.randint(0, len(adjectives) - 1)
        jokes.append(adjectives[a_adjectives])

        i += 1

    k = [' '.join(x) for x in zip(jokes[0::3], jokes[1::3], jokes[2::3])]

    return(k)

print(get_jokes(10))