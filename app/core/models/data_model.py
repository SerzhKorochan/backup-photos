import json
from os import path


class DataModel:
    PATH_TO_SELECTED_DATA = 'conf/selected_data.json'

    def __init__(self, config: dict):
        self.config = config
        self.data_layout = {
            'social_network': {
                'name': '',
                'token_path': '',
                'token': '',
                'user_id': ''
            },
            'remote_drive': {
                'name': '',
                'token_path': '',
                'token': ''
            }
        }

    def get_config_option(self, option):
        return self.config.get(option)

    def get_selected_service(self, type_of_service, option=None):
        with open(self.PATH_TO_SELECTED_DATA, 'r', encoding='utf-8') as f:
            selected_data = json.load(f)
            if option:
                return selected_data.get(type_of_service).get(option)
            else:
                return selected_data.get(type_of_service)

    def check_entered_services(self):
        if self.data_layout.get('social_network').get('name') in \
                self.get_config_option('available_social_networks') \
                and self.data_layout.get('remote_drive').get('name') in \
                self.get_config_option('available_remote_drives'):
            return True
        return False

    def check_tokens_paths(self):
        if path.exists(self.data_layout.get('social_network').get('token_path')) and \
                path.exists(self.data_layout.get('remote_drive').get('token_path')):
            return True
        return False

    def read_tokens(self):
        with open(self.data_layout.get('social_network').get('token_path'), 'r', encoding='utf-8') as f:
            self.data_layout['social_network']['token'] = f.readline()

        with open(self.data_layout.get('remote_drive').get('token_path'), 'r', encoding='utf-8') as f:
            self.data_layout['remote_drive']['token'] = f.readline()

    def save_selected_options(self):
        with open(self.PATH_TO_SELECTED_DATA, 'w', encoding='utf-8') as f:
            data = self.data_layout
            json.dump(data, f)

    def remove_data(self):
        with open(self.PATH_TO_SELECTED_DATA, 'w', encoding='utf-8') as f:
            json.dump('', f)

    def is_data_empty(self):
        with open(self.PATH_TO_SELECTED_DATA, 'r', encoding='utf-8') as f:
            if json.load(f):
                return False
        return True

