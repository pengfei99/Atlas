from org.pengfei.S3BucketEntityManager import generate_s3_bucket_json_source
from org.pengfei.S3PsDirEntityManager import generate_s3_ps_dir_entity_json_source
from org.pengfei.S3ObjectEntityManager import generate_s3_object_entity_json_source

# get all supported entity types
# print(get_all_supported_entity_type())

# get attributes info of entity aws_s3_bucket
# print(get_all_s3_bucket_supported_attributes())

# generate a aws_s3_bucket entity json source file
s3_bucket_json_source = generate_s3_bucket_json_source ("donnees-insee", "minio.lab.sspcloud.fr",
                                                              "s3://minio.lab.sspcloud.fr/donnees-insee", " open data"
                                                              , creator_id="pliu")
# print(s3_bucket_json_source)

# generate a aws_ps_dir
s3_ps_dir_json_source = generate_s3_ps_dir_entity_json_source("RP", "s3://minio.lab.sspcloud.fr/donnees-insee/RP",
                                                              "s3://minio.lab.sspcloud.fr/donnees-insee", "RP/",
                                                              replicated_from="s3://minio.lab.sspcloud.fr/donnees-insee/pengfei_test")
# print(s3_ps_dir_json_source)
s3_object_json_source = generate_s3_object_entity_json_source("pengfei.txt","s3://minio.lab.sspcloud.fr/donnees-insee/RP/pengfei.txt","s3://minio.lab.sspcloud.fr/donnees-insee/RP",
                                                              "txt","pliu","my test doc",size=1024)
print(s3_object_json_source)
