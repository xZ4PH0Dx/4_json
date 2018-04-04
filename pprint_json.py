import json
import os
import sys
from json.decoder import JSONDecodeError


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def prettify_json(not_pretty_data):
    return json.dumps(
        not_pretty_data,
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь к файлу')
    filepath = sys.argv[1]

    try:
        loaded_shops = load_data(filepath)
    except (OSError, JSONDecodeError):
        sys.exit('Файл отсутствует или это не json')

    print(prettify_json(loaded_shops))
