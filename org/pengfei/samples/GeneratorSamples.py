from org.pengfei.docs.EntityManagerApiHelper import *

config_file_path = "/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/config/config.ini"
template_folder_path = "/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/entity_source_generation/template"


# get all supported entity types
print(get_all_supported_entity_type())

# get attributes info of entity aws_s3_bucket
print(S3BucketEntityGenerator.get_s3_bucket_all_supported_attributes())

# get attributes info of ps dir
print(S3PsDirEntityGenerator.get_s3_ps_dir_all_supported_attributes())

# get attributes info of s3 object
print(S3ObjectEntityGenerator.get_s3_object_all_supported_attributes())

# generate a aws_s3_bucket entity json source file
s3_bucket_json_source = S3BucketEntityGenerator.generate_s3_bucket_json_source("donnees-insee", "minio.lab.sspcloud.fr",
                                                                "s3://minio.lab.sspcloud.fr/donnees-insee", " open data"
                                                                , creator_id="pliu")
print(s3_bucket_json_source)

# generate a aws_ps_dir
s3_ps_dir_json_source = S3PsDirEntityGenerator.generate_s3_ps_dir_entity_json_source("pengfei", "s3://minio.lab.sspcloud.fr/donnees-insee/pengfei",
                                                              "s3://minio.lab.sspcloud.fr/donnees-insee", "pengfei/")
print(s3_ps_dir_json_source)


s3_object_json_source = S3ObjectEntityGenerator.generate_s3_object_entity_json_source("toto2.txt","s3://minio.lab.sspcloud.fr/donnees-insee/RP/toto2.txt","s3://minio.lab.sspcloud.fr/donnees-insee/RP", "RP/",
                                                              "txt","pliu","my test8 doc",size=12048)
print(s3_object_json_source)
