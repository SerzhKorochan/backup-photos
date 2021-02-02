def social_network_input(available_sn: list):
    return f"Please enter name of the social network for backup [{', '.join(available_sn)}]: "


def remote_drive_input(available_drives: list):
    return f"Please enter name of the remote drive for backup [{', '.join(available_drives)}]: "


def token_path_input(selected_system: str):
    return f"Enter or paste path to token file of {selected_system}: "