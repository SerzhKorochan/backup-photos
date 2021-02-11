import datetime


class Parser:

    def __is_value_unique(self, items: list, key: str, value):
        count = 0

        for item in items:
            if item.get(key) == value:
                count += 1

        if count == 1:
            return True
        return False

    def parse_photos_data_to_upload(self, photos):
        parsed_data = []

        for photo in photos:
            parsed_data.append({
                'url': photo.get('max_sizes').get('url'),
                'name': str(photo.get('likes').get('count')),
                'date': str(datetime.date.fromtimestamp(photo.get('date')))
            })

        for item in parsed_data:
            if not self.__is_value_unique(parsed_data, 'name', item['name']):
                item['name'] = f"{item['name']}__{item['date']}"

        return parsed_data
