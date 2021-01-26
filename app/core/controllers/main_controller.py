from app.core.models.command_line_model import CommandLineModel
import json
import os


class MainController:

    def __init__(self, config_path):

        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            model = CommandLineModel(self.config)
