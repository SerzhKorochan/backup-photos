import requests
import datetime
import os
import json


class YandexDriveApiModel:
    BASE_DIR_FOR_UPLOAD = 'Backups'
    PATH_TO_SAVE_LOGS = 'logs'

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

    def save_uploaded_files_info(self, files: list, fields_to_save: list):
        uploaded_data = []

        for file in files:
            required_file_info = {}

            for field in fields_to_save:
                required_file_info[field] = file.get(field)

            uploaded_data.append(required_file_info)

        log_name = 'backup__' + self.get_current_datetime() + '.json'
        log_path = os.path.join(self.PATH_TO_SAVE_LOGS, log_name)

        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(uploaded_data, f, indent=2)

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')