import json
import os
from bson import json_util


def write_a_json(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f'./json/{name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))
