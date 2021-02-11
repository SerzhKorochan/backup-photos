import requests
import datetime


class YandexDriveApiModel:
    BASE_DIR_FOR_UPLOAD = 'Backups'

    def __init__(self, TOKEN):
        self.TOKEN = TOKEN
        self.HEADERS = {
            'Authorization': f'OAuth {self.TOKEN}'
        }

    def is_token_correct(self):
        url = 'https://cloud-api.yandex.net/v1/disk'

        response = requests.get(url, headers=self.HEADERS)

        if response.status_code == 200:
            return True
        return False

    def is_resource_exist(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': path
        }

        response = requests.get(url, params=params, headers=self.HEADERS)

        if response.status_code == 200:
            return True
        return False

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': folder_name
        }

        response = requests.put(url, params=params, headers=self.HEADERS)

        if response.status_code == 201:
            return True
        return False

    def upload_file_by_url(self, path_to_file, file_name, file_url):
        api_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': f"{path_to_file}/{file_name}",
            'url': file_url
        }

        response = requests.post(api_url, params=params, headers=self.HEADERS)

        if response.status_code == 202:
            return True
        return False

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')