from org.pengfei.CreateEntityJsonSource import *

# get all supported entity types
print(get_all_supported_entity_type())

# get attributes info of entity aws_s3_bucket
print(get_all_s3_bucket_supported_attributes())

# generate a aws_s3_bucket entity json source file
s3_bucket_json_source=generate_s3_bucket_entity_json_source("donnees-insee","minio.lab.sspcloud.fr","s3://minio.lab.sspcloud.fr/donnees-insee "," open data"
                                     ,creator_id="pliu")
print(s3_bucket_json_source)

# generate a aws_ps_dir
