from org.pengfei.entity_management.s3.S3BucketManager import S3BucketManager

# config_file_path = "/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/config/config.ini"
# template_folder_path = "/home/pliu/PycharmProjects/AtlasPyApi/org/pengfei/entity_source_generation/template"

hostname = "localhost"
port = 21000
login = "admin"
pwd = "admin"

prod_h_name = "atlas.lab.sspcloud.fr"
prod_port = 80
prod_login = "pengfei"
prod_pwd = ""

s3 = S3BucketManager(hostname, port, login, pwd)

# creat s3 bucket in atlas
# s3.create_s3_bucket("pengfei_test", "s3://pengfei.org", "s3://pengfei.org/pengfei_test", "test for me")
# s3.create_s3_bucket("pengfei_test1", "s3://pengfei.org", "s3://pengfei.org/pengfei_test1", "test1 for me")
# s3.create_s3_bucket("pengfei_test2", "s3://pengfei.org", "s3://pengfei.org/pengfei_test2", "test2 for me")
# s3.create_s3_bucket("pengfei_test3", "s3://pengfei.org", "s3://pengfei.org/pengfei_test3", "test3 for me")

# get s3 bucket via guid
guid = "9642d134-4d0e-467c-8b36-ca73902d4c14"
e = s3.get_s3_bucket(guid)
s3.show_s3_attributes(e)
e_attributes = s3.get_s3_attributes(e)
e_attributes_key_list = s3.get_s3_attributes_key_list(e)
print(e_attributes_key_list)
print(e_attributes['description'])

# update s3 bucket attributes
s3.update_s3_bucket(guid, 'description', 'update description from api')

# delete s3 bucket
s3.delete_s3_bucket(guid)
