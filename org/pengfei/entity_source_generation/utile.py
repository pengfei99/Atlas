import os
import time
from configparser import SafeConfigParser

import jinja2


# get current time
def current_milli_time():
    return int(round(time.time() * 1000))


# set up config file
def init_config(config_file_path: str) -> str:
    if os.path.isfile(config_file_path):
        config = SafeConfigParser()
        config.read(config_file_path)
        return config
    else:
        print("config file not found")
        raise FileNotFoundError


# jinja2 util function, it takes a jinja2 template and a dict of attributes, then merges them to generate a target file
def populate_template(file_path: str, context: dict) -> str:
    path, file_name = os.path.split(file_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(file_name).render(context)
