from app.vk_api.models.vk_api_model import VkApiModel
import app.vk_api.views.vk_api_view as api_view


class VkApiController:
    def __init__(self, sn_data: dict):
        self.sn_data = sn_data
        self.uid = ''
        self.api_model = VkApiModel(sn_data)

        if not self.api_model.is_correct_token():
            exit(api_view.incorrect_token())

    def get_the_biggest_photos(self):
        QUANTITY_BY_DEFAULT = 5

        uid = input(api_view.user_id_input())
        quantity = input(api_view.quantity_input(QUANTITY_BY_DEFAULT))

        if not quantity:
            quantity = QUANTITY_BY_DEFAULT

        if not self.api_model.is_user_exist(uid):
            exit(api_view.user_does_not_exist(uid))

        uid = self.api_model.format_uid(uid)
        self.uid = uid

        photos = self.api_model.get_photos(uid)
        the_biggest_photos = self.api_model.get_the_biggest_photos(photos, int(quantity))

        return the_biggest_photos
