import requests


class VkApiModel:

    def __init__(self, sn_data: dict):
        self.sn_data = sn_data
        self.url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': sn_data['token'],
            'v': '5.126'
        }

    def is_correct_token(self):
        api_method = 'account.getInfo'
        response = requests.get(self.url + api_method, params=self.params).json()

        if not response.get('error'):
            return True
        return False

    def is_user_exist(self, uid):
        api_method = 'users.get'
        params = {
           'user_ids': uid
        }

        response = requests.get(self.url + api_method, params={**self.params, **params}).json()

        if not response.get('error'):
            return True
        return False

    def get_photos(self, uid, album_id='profile'):
        pass
    #TODO this method
