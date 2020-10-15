from enum import Enum


class S3PathClass(Enum):
    BUCKET = 1
    DIR = 2
    OBJECT = 3
