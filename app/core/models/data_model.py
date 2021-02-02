import json


class DataModel:
    PATH_TO_SELECTED_DATA = 'conf/selected_data.json'

    def __init__(self, config: dict):
        self.config = config
        self.data_layout = {
            'social_network': {
                'name': '',
                'token': ''
            },
            'remote_drive': {
                'name': '',
                'token': ''
            }
        }

    def get_config_option(self, option):
        return self.config.get(option)

    def get_selected_option(self, type_of_service, option):
        with open(self.PATH_TO_SELECTED_DATA, 'r', encoding='utf-8') as f:
            selected_data = json.load(f)
            return selected_data.get(type_of_service).get(option)

    def check_token(self, name_of_service, token):
        pass

    def save_selected_options(self):
        with open(self.PATH_TO_SELECTED_DATA, 'w', encoding='utf-8') as f:
            data = self.data_layout
            json.dump(data, f)
