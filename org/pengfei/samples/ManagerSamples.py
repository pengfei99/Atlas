from org.pengfei.atlas_client.client import Atlas
from org.pengfei.entity_management.s3.S3BucketManager import S3BucketManager
from org.pengfei.entity_management.s3.S3ObjectManager import S3ObjectManager

hostname = "localhost"
port = 21000
login = "admin"
pwd = "admin"


atlas_client = Atlas(hostname, port, username=login, password=pwd)
s3_bucket_manager = S3BucketManager(atlas_client)

# creat s3 bucket in atlas
# s3_bucket_manager.create_s3_bucket("pengfei_test", "s3://pengfei.org", "s3://pengfei.org/pengfei_test", "test for me")
# s3_bucket_manager.create_entity("pengfei_test1", "s3://pengfei.org", "s3://pengfei.org/pengfei_test1", "test1 for me")
# s3_bucket_manager.create_s3_bucket("pengfei_test2", "s3://pengfei.org", "s3://pengfei.org/pengfei_test2", "test2 for me")
# s3_bucket_manager.create_s3_bucket("pengfei_test3", "s3://pengfei.org", "s3://pengfei.org/pengfei_test3", "test3 for me")

# get s3 bucket via guid
# guid = "9642d134-4d0e-467c-8b36-ca73902d4c14"
# e = s3_bucket_manager.get_entity(guid)
# s3_bucket_manager.show_entity_attributes(e)
# e_attributes = s3_bucket_manager.get_entity_attributes(e)
# e_attributes_key_list = s3_bucket_manager.get_s3_attributes_key_list(e)
# print(e_attributes_key_list)
# print(e_attributes['description'])

# update s3 bucket attributes
# s3_bucket_manager.update_entity(guid, 'description', 'update description from api')

# delete s3 bucket
# s3_bucket_manager.delete_entity(guid)

# s3_ps_dir_manager = S3PsDirManager(hostname, port, login, pwd)
# s3_ps_dir_manager.create_entity("data_science", "s3://pengfei.org/pengfei_test1/data_science",
#                                 "s3://pengfei.org/pengfei_test1", "data_science/")
#
# s3_ps_dir_manager.create_entity("data_science1", "s3://pengfei.org/pengfei_test1/data_science1",
#                                 "s3://pengfei.org/pengfei_test1", "data_science1/")

s3_obj_manager = S3ObjectManager(atlas_client)
s3_obj_manager.create_entity("toto.csv", "s3://pengfei.org/pengfei_test1/data_science/toto.csv",
                             "s3://pengfei.org/pengfei_test1/data_science", "data_science", "csv", "pengfei",
                             "test txt")
