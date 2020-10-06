import os
import time
import configparser

# get current path
base_path = os.getcwd()



# get all supported entity types
def get_all_supported_entity_type():
    return ["aws_s3_bucket", "aws_s3_pseudo_dir", "aws_s3_object"]







