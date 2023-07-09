import json
from typing import List


class JsonGenerator:
    @staticmethod
    def generate_json_as_list_of_value_and_key(values: List, key: str):
        temp_list = []
        for i in values:
            temp_list.append({key: i})

        return json.dumps(temp_list)

    @staticmethod
    def generate_json_as_key_and_list_of_values(values: List, key: str):
        return json.dumps({key: values})
