from app.core.models.command_line_model import CommandLineModel
from app.core.models.data_model import DataModel
import app.core.views.command_line_view as cl_view
import app.core.views.data_view as data_view
import json
import os


class MainController:

    def __init__(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            self.cl_model = CommandLineModel(self.config)
            self.data_model = DataModel(self.config)

    def run(self):
        if self.cl_model.get_entered_arg():
            entered_arg = self.cl_model.get_entered_arg()
        else:
            available_args = self.cl_model.get_available_args()
            exit(cl_view.show_available_args(available_args))

        if entered_arg == 'quickstart':
            # Social Network -- Input
            available_sn = self.data_model.get_config_option('available_social_networks')
            self.data_model.data_layout['social_network']['name'] = input(data_view.social_network_input(available_sn))

            # Remote Drive -- Input
            available_drives = self.data_model.get_config_option('available_remote_drives')
            self.data_model.data_layout['remote_drive']['name'] = input(data_view.remote_drive_input(available_drives))

            # Token Path for Social Network -- Input

            # Token Path for Remote Drive -- Input

        elif entered_arg == 'rm-data':
            pass

        elif entered_arg == 'create-backup':
            pass

        elif entered_arg == 'help':
            pass
