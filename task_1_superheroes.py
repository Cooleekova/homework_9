# импортирую requests
import requests


# создаю список с именами героев, которых буду сравнивать
heroes_names = ['Hulk', 'Captain America', 'Thanos']

# создаю пустые переменные
Cleverest_Hero = 0
Cleverest_Hero_intelligence = 0

# в цикле обращаюсь к API сайта,
# для каждого имени героя в списке heroes_names получаю данные
for name in heroes_names:
    response_hero = requests.get("https://www.superheroapi.com/api.php/2619421814940190//search/" + name)
# проверяю код ответа
    if response_hero.status_code != 200:
        raise Exception('ALARM!!!')
# получаю словарь (json формат) с характеристиками героя
    data = (response_hero.json()['results'][0])
# из списка характеристик выделяю значение "умности" intelligence
    intelligence = int(data['powerstats']['intelligence'])
# сравниваю intelligence всех героев, самое большое значение записываю в переменную
    if intelligence > Cleverest_Hero_intelligence:
        Cleverest_Hero_intelligence = intelligence
        Cleverest_Hero = name
# вывожу результат
print(f'Самый умный супергерой: {Cleverest_Hero}, intelligence = {Cleverest_Hero_intelligence}')

