from org.pengfei.minio.MinioAtlasHook import MinioAtlasHook

minio_end_point = 'minio.lab.sspcloud.fr'
minio_access_key = 'FICD0K51M6PLB9XFM419'
minio_secret_key = 'rWV296yBJWk0wFun6Bz+tiONkWnBoACNly+wjE1m'
minio_token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJGSUNEMEs1MU02UExCOVhGTTQxOSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJhdWQiOlsib255eGlhIiwiYWNjb3VudCJdLCJhdXRoX3RpbWUiOjE2MDI3NjAwODgsImF6cCI6Im9ueXhpYSIsImVtYWlsIjoibGl1LnBlbmdmZWlAaG90bWFpbC5mciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJleHAiOiIxNjAyODAzMjg4IiwiZmFtaWx5X25hbWUiOiJMaXUiLCJnaXZlbl9uYW1lIjoiUGVuZ2ZlaSIsImlhdCI6MTYwMjc2MDA4OCwiaXNzIjoiaHR0cHM6Ly9hdXRoLmxhYi5zc3BjbG91ZC5mci9hdXRoL3JlYWxtcy9zc3BjbG91ZCIsImp0aSI6Ijc5MDJhYzA0LTAzYTYtNGQ0Mi1iY2NjLTRjYWQxM2UwZmVkYyIsIm5hbWUiOiJQZW5nZmVpIExpdSIsIm5vbmNlIjoiZWI5YjIyYjQtZDM5ZC00ZTZkLWIzNzItMThlYjY1ZjdhNmRkIiwicG9saWN5IjoiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGVuZ2ZlaSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJBdGxhc19yb2xlX2FkbWluIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNlc3Npb25fc3RhdGUiOiI1NGJkYmRmZS1jYjQ3LTQwMzItOTk3OC00NzNmNGU5YWRlYmUiLCJzdWIiOiI0NzM0OTEyOC00YTRjLTQyMjYtYTViMS02ODA4MDFhZjVhMmIiLCJ0eXAiOiJCZWFyZXIifQ.7lyx2yQVCEF2YhZ_1uMwqmUS8kPyrUY4OgPvL0TrVCnC2Whm3e01mSLUoflgAYZiho321SgmZQtHJaIRaSidpg'
atlas_hostname = "localhost"
atlas_port = 21000
atlas_login = "admin"
atlas_pwd = "admin"

minio_hook = MinioAtlasHook(minio_end_point,minio_access_key,minio_secret_key,minio_token,atlas_hostname,atlas_port,atlas_login,atlas_pwd)

path = "pengfei"
path1 = "pengfei/pengfei_test"
path2 = "pengfei/pengfei_test/Demo2_ Retail_WEB_SITE_BI.json"

# Alias of FilesystemSpec.info
meta_data = minio_hook.get_entity_meta_data(path)
meta_data1 = minio_hook.get_entity_meta_data(path1)
meta_data2 = minio_hook.get_entity_meta_data(path2)
# print(content)
print(meta_data)
print(meta_data1)
print(meta_data2)

path_class = minio_hook.get_type_from_path(path)
path_class1 = minio_hook.get_class_from_path(path1)
path_class2 = minio_hook.get_class_from_path(path2)

print(path_class)
print(path_class1)
print(path_class2)

path_type = minio_hook.get_type_from_path(path)
path_type1 = minio_hook.get_type_from_path(path1)
path_type2 = minio_hook.get_type_from_path(path2)

print(path_type)
print(path_type1)
print(path_type2)

# minio_hook.create_atlas_bucket(meta_data,"added by minio hook")
minio_hook.create_atlas_ps_dir(meta_data1,"added by minio hook")