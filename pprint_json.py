import json
import os
import sys
from json.decoder import JSONDecodeError


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def pretty_print_json(not_pretty_json):
    return json.dumps(not_pretty_json, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь к файлу')
    filepath = sys.argv[1]

    try:
        loaded_json = (load_data(filepath))
    except (OSError, JSONDecodeError):
        sys.exit('Файл отсутствует или это не json')

    print(pretty_print_json(loaded_json))
