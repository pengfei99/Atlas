from org.pengfei.entity_management.s3.S3BucketManager import S3BucketManager

config_file_path="/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/config/config.ini"
template_folder_path="/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/entity_source_generation/template"

s3 = S3BucketManager("localhost", 21000, "admin", "admin")
s3.create_s3_bucket("pengfei_test", "s3://pengfei.org", "s3://pengfei.org/pengfei_test", "test for me")
s3.get_s3_bucket()

