from sys import argv


class CommandLineModel:
    MAX_ARGS_QUANTITY = 2

    def __init__(self, config: dict):
        self.config = config
        self.arguments = argv

    def get_entered_arg(self):
        if len(self.arguments) == self.MAX_ARGS_QUANTITY:
            entered_arg = self.arguments[1]

            if entered_arg in self.config['available_args']:
                return entered_arg

        return None

    def get_available_args(self):
        return self.config['available_args']
