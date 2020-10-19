from org.pengfei.minio.S3PathClass import S3PathClass


class MinioScanner:
    def __init__(self, minio_client):
        self.minio_client = minio_client
        self.fs = minio_client.get_fs()

    def scan_path(self, path):
        content_list = self.fs.ls(path)
        for content in content_list:
            path_class = self.minio_client.get_class_from_path(content)
            if path_class == S3PathClass.BUCKET:
                print("load bucket into atlas: " + content)
                # call dir scanner recursively
                self.scan_path(content)
            elif path_class == S3PathClass.DIR:
                print("load dir into atlas: " + content)
                self.scan_path(content)
            elif path_class == S3PathClass.OBJECT:
                # avoid loading .keep file
                if content.split("/")[-1] == ".keep":
                    pass
                else:
                    print("load object into atlas: " + content)
            else:
                raise ValueError
