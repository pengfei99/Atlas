import json

from org.pengfei.atlas_client.client import Atlas
from org.pengfei.definition import TARGET_FOLDER
from org.pengfei.entity_management.EntityManager import EntityManager
from org.pengfei.entity_source_generation.S3BucketEntityGenerator import S3BucketEntityGenerator


class S3BucketManager(EntityManager):
    def __init__(self, atlas_client: Atlas):
        super().__init__(atlas_client)

    def create_entity(self, name: str, domain: str, qualified_name: str, description: str, **kwargs) -> None:
        s3_bucket_json_source = S3BucketEntityGenerator.generate_s3_bucket_json_source(name, domain, qualified_name,
                                                                                       description, **kwargs)
        target_file = TARGET_FOLDER + "/s3_bucket.json"
        f = open(target_file, "w")
        f.write(s3_bucket_json_source)
        f.close()
        with open(target_file, "r") as json_file:
            s3_bucket_json_source = json.load(json_file)
            print(s3_bucket_json_source)
        try:
            self.client.entity_post.create(data=s3_bucket_json_source)
        except Exception as e:
            print("atlas bucket entity creation failed. Origin exception: " + str(e))
            return False
        else:
            return True
