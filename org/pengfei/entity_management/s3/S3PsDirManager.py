import json

from org.pengfei.atlas_client.client import Atlas
from org.pengfei.definition import TARGET_FOLDER
from org.pengfei.entity_management.EntityManager import EntityManager
from org.pengfei.entity_source_generation.S3PsDirEntityGenerator import S3PsDirEntityGenerator


class S3PsDirManager(EntityManager):
    def __init__(self, atlas_client: Atlas):
        super().__init__(atlas_client)

    def create_entity(self, name: str, qualified_name: str, bucket_qualified_name: str, object_prefix: str,
                      **kwargs) -> None:
        s3_ps_dir_json_source = S3PsDirEntityGenerator.generate_s3_ps_dir_entity_json_source(name, qualified_name,
                                                                                             bucket_qualified_name,
                                                                                             object_prefix, **kwargs)
        target_file = TARGET_FOLDER + "/s3_ps_dir.json"
        f = open(target_file, "w")
        f.write(s3_ps_dir_json_source)
        f.close()
        with open(target_file, "r") as json_file:
            s3_ps_dir_json_source = json.load(json_file)
            print(s3_ps_dir_json_source)
        self.client.entity_post.create(data=s3_ps_dir_json_source)
