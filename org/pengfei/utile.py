import time
import configparser
import os


# get current time
def current_milli_time():
    return int(round(time.time() * 1000))


# set up config file
def init_config():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + "/config/config.ini")
    return config
