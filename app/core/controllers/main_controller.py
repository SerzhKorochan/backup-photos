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
            sn_name = input(data_view.social_network_input(available_sn)).lower().title()
            self.data_model.data_layout['social_network']['name'] = sn_name

            # Remote Drive -- Input
            available_drives = self.data_model.get_config_option('available_remote_drives')
            rm_drive_name = input(data_view.remote_drive_input(available_drives)).lower().title()
            self.data_model.data_layout['remote_drive']['name'] = rm_drive_name

            # Check Entered Services
            if not self.data_model.check_entered_services():
                exit(data_view.service_does_not_exist())

            # Token Path for Social Network -- Input
            sn_token_path = input(data_view.token_path_input(sn_name))
            self.data_model.data_layout['social_network']['token_path'] = sn_token_path

            # Token Path for Remote Drive -- Input
            rm_drive_token_path = input(data_view.token_path_input(rm_drive_name))
            self.data_model.data_layout['remote_drive']['token_path'] = rm_drive_token_path

            # Check Entered Paths
            if not self.data_model.check_tokens_paths():
                exit(data_view.path_does_not_exist())

            # Read Tokens
            self.data_model.read_tokens()

            # Save Entered Data to json file
            self.data_model.save_selected_options()

            exit(data_view.successfully_saved())

        elif entered_arg == 'rm-data':
            # Remove all data

            self.data_model.remove_data()
            exit(data_view.successfully_removed())

        elif entered_arg == 'create-backup':
            # Check Did user use command 'quickstart'

            if self.data_model.is_data_empty():
                exit(data_view.data_is_empty())

        elif entered_arg == 'help':
            pass
