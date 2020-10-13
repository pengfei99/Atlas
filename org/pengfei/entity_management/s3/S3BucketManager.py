from atlasclient.client import Atlas
from org.pengfei.entity_source_generation.S3BucketEntityGenerator import S3BucketEntityGenerator
import json
from org.pengfei.definition import TARGET_FOLDER


class S3BucketManager:

    def __init__(self, host_name, port_number, user_name, password):
        self.host_name = host_name
        self.port_number = port_number
        self.user_name = user_name
        self.password = password
        self.client = Atlas(host_name, port_number, username=user_name, password=password)

    def create_s3_bucket(self, name, domain, qualified_name, description, **kwargs):
        s3_bucket_json_source = S3BucketEntityGenerator.generate_s3_bucket_json_source(name, domain, qualified_name,
                                                                                       description)
        target_file = TARGET_FOLDER + "/s3_bucket.json"
        f = open(target_file, "w")
        f.write(s3_bucket_json_source)
        f.close()
        with open(target_file, "r") as json_file:
            s3_bucket_json_source = json.load(json_file)
            print(s3_bucket_json_source)
        self.client.entity_post.create(data=s3_bucket_json_source)

    def get_s3_bucket(self, guid):
        s3_bucket = self.client.entity_guid(guid)
        print("get_result"+str(s3_bucket._data))
        return s3_bucket.entity

    @staticmethod
    def get_s3_attributes(entity):
        return entity['attributes']

    @staticmethod
    def show_s3_attributes(entity):
        print(entity['attributes'])

    @staticmethod
    def get_s3_attributes_key_list(entity):
        return S3BucketManager.get_s3_attributes(entity).keys()

    def update_s3_bucket(self, guid, attribute_name, attribute_value):
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.entity['attributes'][attribute_name] = attribute_value
        s3_bucket.update(attribute=attribute_name)

    def delete_s3_bucket(self, guid):
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.delete()
