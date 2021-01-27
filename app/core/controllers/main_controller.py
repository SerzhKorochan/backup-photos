from app.core.models.command_line_model import CommandLineModel
import app.core.views.command_line_view as cl_view
import json
import os


class MainController:

    def __init__(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            self.cl_model = CommandLineModel(self.config)

    def run(self):
        if self.cl_model.get_entered_arg():
            entered_arg = self.cl_model.get_entered_arg()
        else:
            available_args = self.cl_model.get_available_args()
            exit(cl_view.show_available_args(available_args))

        if entered_arg == 'quickstart':
            pass

        elif entered_arg == 'rm-data':
            pass

        elif entered_arg == 'create-backup':
            pass

        elif entered_arg == 'help':
            pass
