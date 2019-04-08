import os
from pathlib import Path

import yaml


class ConfigLoader:
    config = {}  # type: dict

    def __init__(self, config_path=None):
        my_file = Path(config_path)

        if config_path and my_file.is_file():
            self.__load_config_file(config_path)

        else:

            self.config['SLACK_CLIENT_TOKEN'] = os.getenv(
                'SLACK_CLIENT_TOKEN', 'ERROR')
            self.config['SLACK_CLIENT_NAME'] = os.getenv(
                'SLACK_CLIENT_NAME', 'lighthouse')

            self.config['CHECK_MK_SERVER'] = os.getenv('CHECK_MK_SERVER',
                                                       'ERROR')
            self.config['CHECK_MK_USER'] = os.getenv('CHECK_MK_USER', 'ERROR')
            self.config['CHECK_MK_PASSWORD'] = os.getenv(
                'CHECK_MK_PASSWORD', 'ERROR')

    def __load_config_file(self, config_path):
        with open(config_path, 'r') as ymlfile:
            self.config = yaml.load(ymlfile)
