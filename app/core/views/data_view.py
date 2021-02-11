def social_network_input(available_sn: list):
    return f"Please enter name of the social network for backup [{', '.join(available_sn)}]: "


def remote_drive_input(available_drives: list):
    return f"Please enter name of the remote drive for backup [{', '.join(available_drives)}]: "


def token_path_input(selected_system: str):
    return f"Enter or paste path to '{selected_system}' token file: "


def service_does_not_exist():
    return "Entered service does not exist!"


def path_does_not_exist():
    return "Entered path does not exist!"


def successfully_saved():
    return "Data was saved successfully!"


def successfully_removed():
    return "Data was removed successfully!"


def data_is_empty():
    return "You didn't enter the data. Use 'python main.py quickstart' and follow the instructions."


def data_is_not_empty():
    return "Data is not empty. Use 'python main.py rm-data' and try again."

