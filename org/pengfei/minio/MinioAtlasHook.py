import s3fs
from org.pengfei.minio.S3PathClass import S3PathClass
from org.pengfei.minio.S3PathType import S3PathType
from org.pengfei.entity_management.s3.S3BucketManager import S3BucketManager
from org.pengfei.entity_management.s3.S3PsDirManager import S3PsDirManager
from org.pengfei.entity_management.s3.S3ObjectManager import S3ObjectManager
from datetime import datetime


class MinioAtlasHook:
    def __init__(self, minio_end_point, minio_access_key, minio_secret_key, minio_token, atlas_hostname, atlas_port,
                 atlas_login, atlas_pwd):
        self.minio_end_point = minio_end_point
        self.fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': 'http://' + minio_end_point}, key=minio_access_key,
                                    secret=minio_secret_key,
                                    token=minio_token)
        self.s3_bucket_manager = S3BucketManager(atlas_hostname, atlas_port, atlas_login, atlas_pwd)
        self.s3_ps_dir_manager = S3PsDirManager(atlas_hostname, atlas_port, atlas_login, atlas_pwd)
        self.s3_object_manager = S3ObjectManager(atlas_hostname, atlas_port, atlas_login, atlas_pwd)

    @staticmethod
    def get_class_from_entity_meta(entity_metadata):
        path_class = entity_metadata['StorageClass']
        if path_class == 'BUCKET':
            return S3PathClass.BUCKET
        elif path_class == 'DIRECTORY':
            return S3PathClass.DIR
        elif path_class == 'STANDARD':
            return S3PathClass.OBJECT
        else:
            raise ValueError

    @staticmethod
    def get_type_from__entity_meta(entity_metadata):
        path_type = entity_metadata['type']
        if path_type == 'directory':
            return S3PathType.directory
        elif path_type == 'file':
            return S3PathType.file
        else:
            raise ValueError

    def get_entity_meta_data(self, entity_path):
        meta_data = self.fs.stat(entity_path)
        return meta_data

    def get_class_from_path(self, entity_path):
        entity_metadata = MinioAtlasHook.get_entity_meta_data(self, entity_path)
        return self.get_class_from_entity_meta(entity_metadata)

    def get_type_from_path(self, entity_path):
        entity_metadata = MinioAtlasHook.get_entity_meta_data(self, entity_path)
        return self.get_type_from__entity_meta(entity_metadata)

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
            bucket_name = ps_dir_metadata['name'].split("/")[0]
            entity_name = ps_dir_metadata['name'].split("/")[-1]
            qualified_bucket_name = self.minio_end_point + "/" + bucket_name
            qualified_entity_name = qualified_bucket_name + "/" + entity_name
            prefix = entity_name + "/"
            self.s3_ps_dir_manager.create_entity(entity_name, qualified_entity_name,
                                                 qualified_bucket_name, prefix, description=ps_dir_description)

    def create_atlas_object(self, object_metadata, object_description):
            self.s3_obj_manager.create_entity("toto.csv", "s3://pengfei.org/pengfei_test1/data_science/toto.csv",
                                              "s3://pengfei.org/pengfei_test1/data_science", "data_science", "csv",
                                              "pengfei",
                                              "test txt")
