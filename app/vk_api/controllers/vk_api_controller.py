from app.vk_api.models.vk_api_model import VkApiModel
import app.vk_api.views.vk_api_view as api_view


class VkApiController:
    def __init__(self, sn_data: dict):
        self.sn_data = sn_data
        self.api_model = VkApiModel(sn_data)

        if not self.api_model.is_correct_token():
            exit(api_view.incorrect_token())

    def get_photos(self, name_of_album=None):
        uid = self.sn_data['user_id']

        if not self.api_model.is_user_exist(uid):
            exit(api_view.user_does_not_exist(uid))

        uid = self.api_model.format_uid(uid)

        photos = self.api_model.get_photos(uid)
        the_biggest_photos = self.api_model.get_the_biggest_photos(photos, 5)