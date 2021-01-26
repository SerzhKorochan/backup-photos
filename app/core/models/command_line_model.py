from sys import argv


class CommandLineModel:
    def __init__(self, config: dict):
        self.config = config
        self.arguments = argv
