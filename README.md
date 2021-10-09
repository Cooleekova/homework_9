## Python. Работа с библиотекой requests, http-запросы.

#### Задача №1

Есть [API c информацией о супергероях](https://superheroapi.com/?ref=apilist.fun#appearance). 

Нужно определить кто самый умный (intelligence) из трех супергероев- Hulk, Captain America, Thanos.

Для определения id нужно использовать метод _/search/name_  

Токен, который нужно использовать для доступа к API: 2619421814940190.  

Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.  

#### Задача №2

У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует [Полигон](https://yandex.ru/dev/disk/poligon/).

Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
1. Все ответы приходят в формате json;
2. Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
3. Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".  

HOST: https://cloud-api.yandex.net:443

Шаблон для программы
```python
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')

```
