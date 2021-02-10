import datetime


class Parser:

    @staticmethod
    def parse_photos_data_to_upload(photos):
        parsed_data = []

        for photo in photos:
            parsed_data.append({
                'url': photo.get('max_sizes').get('url'),
                'likes_count': photo.get('likes').get('count'),
                'date': str(datetime.date.fromtimestamp(photo.get('date')))
            })

        return parsed_data
