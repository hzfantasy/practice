import yaml
import os
import json


class YamlReader:
    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError('File not exists.')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yaml_file, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class JsonReader:
    def __init__(self, json_file):
        if os.path.exists(json_file):
            self._json_file = json_file
        else:
            raise FileNotFoundError('File does not exist')
        self._data = list()

    @property
    def data(self):
        if not self._data:
            with open(self._json_file, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        return self._data


if __name__ == '__main__':
    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    DATA_PATH = os.path.join(BASE_PATH, 'data')
    j_test_file = JsonReader(DATA_PATH + "/test_data.json")
    print(json.dumps(j_test_file.data, indent=2))
