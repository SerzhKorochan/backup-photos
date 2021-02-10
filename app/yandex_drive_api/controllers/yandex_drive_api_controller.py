from app.yandex_drive_api.models.yandex_drive_api_model import YandexDriveApiModel
import app.yandex_drive_api.views.yandex_drive_api_view as ya_drive_views


class YandexDriveApiController:
    def __init__(self, rm_drive_data: dict):
        self.rm_drive_data = rm_drive_data
        self.ya_drive_model = YandexDriveApiModel(rm_drive_data['token'])

    def upload_files_by_url(self, dir_name, files: list):
        # Check is base dir for backups exist
        if not self.ya_drive_model.is_resource_exist(self.ya_drive_model.BASE_DIR_FOR_BACKUP):
            self.ya_drive_model.create_folder(self.ya_drive_model.BASE_DIR_FOR_BACKUP)

        # Create new folder for current backup
        current_datatime = self.ya_drive_model.get_current_datetime()
        current_backup_dir = f"{self.ya_drive_model.BASE_DIR_FOR_BACKUP}/id{dir_name}__{current_datatime}"

        if not self.ya_drive_model.create_folder(current_backup_dir):
            exit(ya_drive_views.folder_was_not_created())

        for file in files:
            self.ya_drive_model.upload_file_by_url(current_backup_dir, file.get('likes_count'), file.get('url'))