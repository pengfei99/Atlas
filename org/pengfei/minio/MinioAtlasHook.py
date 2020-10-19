import os
from datetime import datetime

from org.pengfei.entity_management.s3.S3BucketManager import S3BucketManager
from org.pengfei.entity_management.s3.S3ObjectManager import S3ObjectManager
from org.pengfei.entity_management.s3.S3PsDirManager import S3PsDirManager
from org.pengfei.minio.MinioClient import MinioClient


class MinioAtlasHook:
    def __init__(self, minio_client: MinioClient, atlas_client):
        self.minio_end_point = minio_client.get_end_point()
        self.fs = minio_client.get_fs()
        self.s3_bucket_manager = S3BucketManager(atlas_client)
        self.s3_ps_dir_manager = S3PsDirManager(atlas_client)
        self.s3_object_manager = S3ObjectManager(atlas_client)

    def create_atlas_bucket(self, bucket_metadata, bucket_description):
        entity_name = bucket_metadata['name']
        qualified_bucket_name = self.minio_end_point + "/" + entity_name
        domain = self.minio_end_point
        date = bucket_metadata['CreationDate']
        create_time_stamp = round(datetime.timestamp(date) * 1000)
        print("timestamp =", create_time_stamp)
        self.s3_bucket_manager.create_entity(entity_name, domain,
                                             qualified_bucket_name,
                                             bucket_description, create_time=create_time_stamp)

    def create_atlas_ps_dir(self, ps_dir_metadata, ps_dir_description):
        names = ps_dir_metadata['name'].split("/")
        bucket_name = names[0]
        entity_name = "/".join(names[1:])
        qualified_bucket_name = self.minio_end_point + "/" + bucket_name
        qualified_entity_name = qualified_bucket_name + "/" + entity_name
        prefix = entity_name + "/"
        self.s3_ps_dir_manager.create_entity(entity_name, qualified_entity_name,
                                             qualified_bucket_name, prefix, description=ps_dir_description)

    def create_atlas_object(self, object_metadata, object_description):
        names = object_metadata['name'].split('/')
        entity_name = names[-1]
        qualified_entity_name = object_metadata['name']
        qualified_ps_dir_name = "/".join(names[:-1])
        ps_dir_prefix = "/".join(names[1:-1]) + "/"
        extension = str(os.path.splitext(entity_name)[1])[1:]
        date = object_metadata['LastModified']
        last_modified_stamp = round(datetime.timestamp(date) * 1000)
        size = object_metadata['size']
        self.s3_object_manager.create_entity(entity_name, qualified_entity_name,
                                             qualified_ps_dir_name, ps_dir_prefix, extension,
                                             "pengfei",
                                             object_description, create_time=last_modified_stamp,
                                             update_time=last_modified_stamp, size=size)
