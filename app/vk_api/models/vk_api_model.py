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

    def format_uid(self, uid):
        api_method = 'utils.resolveScreenName'
        params = {
            'screen_name': uid
        }

        response = requests.get(self.url + api_method, params={**self.params, **params}).json()['response']

        if response:
            return int(response['object_id'])
        return int(uid)

    def get_photos(self, uid, album_id='profile'):
        api_method = 'photos.get'
        params = {
            'owner_id': uid,
            'album_id': album_id,
            'photo_sizes': 1,
            'extended': 1
        }

        response = requests.get(self.url + api_method, params={**self.params, **params})

        return response.json()['response']

    def __get_max_photo_size(self, sizes: list):
        max_size = sizes[0].get('width') * sizes[0].get('height')
        max_index = 0

        for i in range(1, len(sizes)):

            if max_size < (sizes[i].get('width') * sizes[i].get('height')):
                max_size = sizes[i].get('width') * sizes[i].get('height')
                max_index = i

        if max_size == 0:
            index_of_max_quality = -1
            max_index = index_of_max_quality

        return sizes[max_index], max_size

    def get_the_biggest_photos(self, photos: dict, quantity=5):
        count = photos.get('count')
        items = photos.get('items')

        for item in items:
            item['max_sizes'], item['max_size'] = self.__get_max_photo_size(item['sizes'])

        items = sorted(items, key= lambda k: k['max_size'], reverse=True)

        if 0 < count <= quantity:
            return items
        return items[0:quantity]



