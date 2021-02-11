from app.yandex_drive_api.models.yandex_drive_api_model import YandexDriveApiModel
import app.yandex_drive_api.views.yandex_drive_api_view as ya_drive_views


class YandexDriveApiController:
    def __init__(self, rm_drive_data: dict):
        self.rm_drive_data = rm_drive_data
        self.ya_drive_model = YandexDriveApiModel(rm_drive_data['token'])

        if not self.ya_drive_model.is_token_correct():
            exit(ya_drive_views.incorrect_token())

    def upload_files_by_url(self, dir_name, files: list):
        # Check is base dir for upload exist
        if not self.ya_drive_model.is_resource_exist(self.ya_drive_model.BASE_DIR_FOR_UPLOAD):
            self.ya_drive_model.create_folder(self.ya_drive_model.BASE_DIR_FOR_UPLOAD)

        # Create new folder for current upload
        current_datatime = self.ya_drive_model.get_current_datetime()
        current_upload_dir = f"{self.ya_drive_model.BASE_DIR_FOR_UPLOAD}/{dir_name}__{current_datatime}"

        if not self.ya_drive_model.create_folder(current_upload_dir):
            exit(ya_drive_views.folder_was_not_created())

        for file in files:
            if self.ya_drive_model.upload_file_by_url(current_upload_dir, file.get('name'), file.get('url')):
                print(ya_drive_views.file_was_successfully_uploaded(file.get('name')))
            else:
                print(ya_drive_views.file_was_not_uploaded(file.get('name')))
