import json

from org.pengfei.definition import TARGET_FOLDER
from org.pengfei.entity_management.EntityManager import EntityManager
from org.pengfei.entity_source_generation.S3ObjectEntityGenerator import S3ObjectEntityGenerator


class S3ObjectManager(EntityManager):
    def __init__(self, atlas_client):
        super().__init__(atlas_client)

    def create_entity(self, name, qualified_name, ps_dir_qualified_name, object_prefix, data_type, owner, description,
                      **kwargs):
        s3_object_json_source = S3ObjectEntityGenerator.generate_s3_object_entity_json_source(name, qualified_name,
                                                                                              ps_dir_qualified_name,
                                                                                              object_prefix, data_type,
                                                                                              owner, description,
                                                                                              **kwargs)
        target_file = TARGET_FOLDER + "/s3_object.json"
        f = open(target_file, "w")
        f.write(s3_object_json_source)
        f.close()
        with open(target_file, "r") as json_file:
            s3_object_json_source = json.load(json_file)
            print(s3_object_json_source)
        self.client.entity_post.create(data=s3_object_json_source)
