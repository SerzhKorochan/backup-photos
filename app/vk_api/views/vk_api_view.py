def user_id_input():
    return "Please enter user ID whose photos will be saved: "


def quantity_input(by_default):
    return f"Please enter quantity of user's photos for backup [{by_default}]: "


def incorrect_token():
    return "Entered 'Vk' token is incorrect, please enter right one."


def user_does_not_exist(uid):
    return f"User with ID -- '{uid}' does not exist."
