import time
import configparser
import os
import jinja2


# get current time
def current_milli_time():
    return int(round(time.time() * 1000))


# set up config file
def init_config():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + "/config/config.ini")
    return config


# jinja2 util function, it takes a jinja2 template and a dict of attributes, then merges them to generate a target file
def populate_template(file_path, context):
    path, file_name = os.path.split(file_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(file_name).render(context)