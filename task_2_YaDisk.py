import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        file_name = os.path.basename(file_path)
        get_url = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': file_name, 'overwrite': 'true'},
            headers={"Authorization": self.token},
        )
        get_url.raise_for_status()
        result = get_url.json()
        href = result['href']
        with open(file_path, 'rb') as f:
            uploading = requests.put(href, files={'file': f})
        uploading.raise_for_status()
        return f'Файл {file_name} успешно загружен на Яндекс Диск'


my_loader = YaUploader('OAuth *****здесь должен быть ваш токен*****')

print(my_loader.upload(str(input('Введите путь к файлу:'))))