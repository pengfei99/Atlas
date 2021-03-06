import s3fs
from s3fs import S3FileSystem

from org.pengfei.minio.S3PathClass import S3PathClass
from org.pengfei.minio.S3PathType import S3PathType


class MinioClient:
    def __init__(self, minio_end_point: str, minio_access_key: str, minio_secret_key: str, minio_token: str):
        self.minio_end_point = minio_end_point
        self.fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': 'http://' + minio_end_point}, key=minio_access_key,
                                    secret=minio_secret_key,
                                    token=minio_token)

    def get_fs(self) -> S3FileSystem:
        return self.fs

    def get_end_point(self) -> str:
        return self.minio_end_point

    @staticmethod
    def get_class_from_entity_meta(entity_metadata: dict) -> S3PathClass:
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
    def get_type_from__entity_meta(entity_metadata: dict) -> S3PathType:
        path_type = entity_metadata['type']
        if path_type == 'directory':
            return S3PathType.directory
        elif path_type == 'file':
            return S3PathType.file
        else:
            raise ValueError

    def get_path_meta_data(self, entity_path: str) -> dict:
        meta_data = self.fs.stat(entity_path)
        return meta_data

    def get_class_from_path(self, entity_path: str) -> S3PathClass:
        entity_metadata = self.get_path_meta_data(entity_path)
        return self.get_class_from_entity_meta(entity_metadata)

    def get_type_from_path(self, entity_path: str) -> S3PathType:
        entity_metadata = self.get_path_meta_data(entity_path)
        return self.get_type_from__entity_meta(entity_metadata)
