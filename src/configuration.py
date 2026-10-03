import json


class Configuration:
    CONFIGURATION_FILE = "configuration.json"

    _configuration = {}

    try:
        with open(CONFIGURATION_FILE, "r") as file:
            _configuration = json.loads(file.read())
    except FileNotFoundError as e:
        print(f"Configuration file '{CONFIGURATION_FILE}' not found.")
    except json.JSONDecodeError:
        print(f"Configuration file '{CONFIGURATION_FILE}' is not valid JSON. Ensure file contains correct JSON syntax.")

    @classmethod
    def get(cls, key, default=None):
        return cls._configuration.get(key, default)