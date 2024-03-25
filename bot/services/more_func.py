import os
import json


# Выгрузка json(patterns)
def json_loader(key: str = None) -> [dict, list]:
    try:
        current_path = os.path.abspath(os.getcwd())
        parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
        json_file_path = os.path.join(parent_path, 'patterns', 'pattern.json')

        with open(json_file_path, 'r', encoding='utf-8') as file:
            templates = json.load(file)
            if key:
                return templates[key].values()
            else:
                return templates
    except Exception as e:
        print(Exception, e)


# Вытаскивает картинку из media
def get_image(filename):
    try:
        current_path = os.path.abspath(os.getcwd())
        image_path = os.path.join(current_path, 'media', filename)

        with open(image_path, 'rb') as photo:
            return photo.read()

    except Exception as e:
        print(Exception, e)
