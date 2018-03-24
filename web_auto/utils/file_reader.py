import yaml
import os


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
