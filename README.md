# Backup of photos 
**Backup photos** - it's project which helps you to create backup of photos from social networks to remote drive. I've written it in Python programming language.

**Available social networks:**
* [vk.com](https://vk.com)

**Available remote drives:**
* [yandex-disk](https://disk.yandex.ru)

![](https://i.imgur.com/B58jQPA.png)


# Requirements:
* Python3. [Click here to download it for your OS.](https://www.python.org/downloads/)
* Profiles in social networks and remote drives.
* If you have not access to these services from your country (like from Ukraine), [click here](https://windscribe.com) and download VPN.
* [Requests](https://pypi.org/project/requests/) - HTTP Library for Python.

# How to get access tokens:
* For [vk.com](https://vk.com/dev/access_token).
* For [yandex-disk](https://yandex.ru/dev/disk/api/concepts/quickstart.html).

# How to use:
1. Clone the repository and enter to root dir of this project. Open terminal or cmd from this folder.
2. Enter `python main.py quickstart` and write next data:
* name of social network
* name of remote drive
* full(absolute) path to file with token for social network
* full(absolute) path to file with token for remote drive
3. Enter `python main.py create-backup` and write next data:
*  user id
*  quantity of photos

### Other commands:
* You can remove all the data has written(services and tokens): `python main.py rm-data` 
* Get help and info about program - `python main.py help`

# It's important!
* **Don't give access tokens to nobody.**
* **When you enter paths for tokens files, don't use any gaps.**
* **If the services didn't provide to you file with token, but they provided token: create a new file for each one and enter or paste access token there (without any gaps).**

# Other information:
* [Video demonstration of the program's work](https://youtu.be/FVZniqrw4Lc)
* Developed by SerzhKorochan, Ukraine, 2021.
* Contacts: serzhkorochan@gmail.com
* Version: 1.0
