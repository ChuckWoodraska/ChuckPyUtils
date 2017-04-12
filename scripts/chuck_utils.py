"""
Chuck Utilities - Common functionality I use a lot.
"""

import datetime
from configparser import ConfigParser
import os


def read_config(path):
    """Read config file."""
    config = ConfigParser()
    config.read(path)
    return config


def get_file_path(input_file, config_file):
    """Good for getting the current path of the python script by using __file__ and then joining a config name to it."""
    return os.path.join(os.path.dirname(os.path.abspath(input_file)), config_file)


def default_json_serializer(obj):
    """Default JSON serializer. Usually fed to default of json.dumps"""
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date) or isinstance(obj, datetime.timedelta):
        return str(obj)
    else:
        return obj


def json_serializer(the_dict):
    """Runs through entire dictionary to serialize."""
    for key in the_dict:
        the_dict[key] = default_json_serializer(the_dict[key])
    return the_dict


def list_to_json_serialize(the_list):
    """List of dicts to serialize"""
    new_list = []
    for the_dict in the_list:
        new_list.append(json_serializer(the_dict))
    return new_list


def transform_checkbox(checkbox):
    """Transform checkbox return value from JavaScript."""
    if checkbox == 'on':
        return True
    elif checkbox == 'off':
        return False
    else:
        return False


def transform_boolean(bool_value):
    """Transform boolean return value from JavaScript."""
    if bool_value == 'true':
        return True
    elif bool_value == 'false':
        return False
    else:
        return False
