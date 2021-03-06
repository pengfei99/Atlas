from org.pengfei.atlas_client.client import Atlas
from org.pengfei.minio.MinioAtlasHook import MinioAtlasHook
from org.pengfei.minio.MinioClient import MinioClient

minio_end_point = 'minio.lab.sspcloud.fr'
minio_access_key = 'GU7PNGYWCDJWQMUVBETV'
minio_secret_key = 'TgWhOohHdkgW+f9KZg4jParqPZGfcHl2GlK7f+5H'
minio_token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJHVTdQTkdZV0NESldRTVVWQkVUViIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJhdWQiOlsib255eGlhIiwiYWNjb3VudCJdLCJhdXRoX3RpbWUiOjE2MDMwOTUzNTcsImF6cCI6Im9ueXhpYSIsImVtYWlsIjoibGl1LnBlbmdmZWlAaG90bWFpbC5mciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJleHAiOiIxNjAzMTM4NTU3IiwiZmFtaWx5X25hbWUiOiJMaXUiLCJnaXZlbl9uYW1lIjoiUGVuZ2ZlaSIsImlhdCI6MTYwMzA5NTM1NywiaXNzIjoiaHR0cHM6Ly9hdXRoLmxhYi5zc3BjbG91ZC5mci9hdXRoL3JlYWxtcy9zc3BjbG91ZCIsImp0aSI6IjI4ODlmMjZmLTYyODEtNGFmOS1iMWYzLWRjYTZiZmVmZWM5ZCIsIm5hbWUiOiJQZW5nZmVpIExpdSIsIm5vbmNlIjoiMDUzYjU4MjYtYjIyMi00YTdlLThhMWMtMzAzZGQxYTc5ZTI3IiwicG9saWN5IjoiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGVuZ2ZlaSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJBdGxhc19yb2xlX2FkbWluIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNlc3Npb25fc3RhdGUiOiJiYmM3ZWU0Mi1iNWJlLTQ1MWEtOWM3YS1lMWU0N2FkZDhhMzciLCJzdWIiOiI0NzM0OTEyOC00YTRjLTQyMjYtYTViMS02ODA4MDFhZjVhMmIiLCJ0eXAiOiJCZWFyZXIifQ.rJ8mWFtiUok6Y0jJfFabsbdbF5KP9GuQ1KwdCKH1dZKCNTM_bZgrZWL9lf08vsQp9n_gbXb19OEGm86qafiuWg'

atlas_hostname = "http://atlas.lab.sspcloud.fr"
atlas_port = 80
oidc_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhUHNCSzhYRC1od1gtMWJFbjdZZDRLS0tWS0hYRy03RHg3STZDaVZZWUtRIn0.eyJleHAiOjE2MDMxNDM4MzUsImlhdCI6MTYwMzEwMDYzNiwiYXV0aF90aW1lIjoxNjAzMTAwNjM1LCJqdGkiOiI5ZTBkZTY2YS1lY2E1LTQ1ZmUtYWE4ZC0xYjhkODI2YjFjZDMiLCJpc3MiOiJodHRwczovL2F1dGgubGFiLnNzcGNsb3VkLmZyL2F1dGgvcmVhbG1zL3NzcGNsb3VkIiwiYXVkIjpbIm9ueXhpYSIsImFjY291bnQiXSwic3ViIjoiNDczNDkxMjgtNGE0Yy00MjI2LWE1YjEtNjgwODAxYWY1YTJiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoib255eGlhIiwibm9uY2UiOiI2ZjcxNzNjNS1iYzM0LTQwZjItOGM0OS04ZjdiNDBmMWI3NTYiLCJzZXNzaW9uX3N0YXRlIjoiNGM3MTcxMmQtZTQzOS00MDkyLWI3MGEtZTNlODAzYmQxMjNkIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJBdGxhc19yb2xlX2FkbWluIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiUGVuZ2ZlaSBMaXUiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwZW5nZmVpIiwiZ2l2ZW5fbmFtZSI6IlBlbmdmZWkiLCJmYW1pbHlfbmFtZSI6IkxpdSIsImVtYWlsIjoibGl1LnBlbmdmZWlAaG90bWFpbC5mciJ9.P3z_Xqv18cIlV1nGLqMOrbhPd2i2iawjyZy-7oL7TyATOnT8U31d7WgBmTJcPKII4mqd1wl-oLJ3IuSObcPdlM1bV8PhndEJqDKql1QWvrMVRkv3wv1YVYoap5ImL0tCcn-0NmxnmUdGfgvulyePzjBEDLQjMb0Z9hBANqJ2F9kNVwImh4gcA2y3QCBdqzoxkZ3ZoaIjiJzX1JYCP3hy1wLWrNiIDGOuWTs0Ebw2h4embxyn87qW3vlrr3PCerHArR9w_QLXRybh3KDFF_XG3lDWhFmdofn11zk9qxY9Q1FAWaytqBnpZezuyPkvSerCkzfeG25Ys8l9wpi7rLP42Q"

minio_client = MinioClient(minio_end_point, minio_access_key, minio_secret_key, minio_token)
atlas_client = Atlas(atlas_hostname, atlas_port, oidc_token=oidc_token)
minio_hook = MinioAtlasHook(minio_client, atlas_client)

path = "pengfei"
path1 = "pengfei/pengfei_test/data_science/deep_learning"
path_long = "pengfei/pengfei_test/data_science/deep_learning/data_set"
path2 = "pengfei/pengfei_test/data_science/deep_learning/paper.pdf"

# Alias of FilesystemSpec.info
# meta_data = minio_client.get_path_meta_data(path)
meta_data1 = minio_client.get_path_meta_data(path1)
meta_data2 = minio_client.get_path_meta_data(path2)
# long_meta = minio_client.get_path_meta_data(path_long)
# print(long_meta)

# print(meta_data)
print(meta_data1)
# print(meta_data2)

path_class = minio_client.get_type_from_path(path)
# path_class1 = minio_client.get_class_from_path(path1)
# path_class2 = minio_client.get_class_from_path(path2)
#
print(path_class)
# print(path_class1)
# print(path_class2)
#
path_type = minio_client.get_type_from_path(path)
# path_type1 = minio_client.get_type_from_path(path1)
# path_type2 = minio_client.get_type_from_path(path2)
#
print(path_type)
# print(path_type1)
# print(path_type2)

# minio_hook.create_atlas_bucket(meta_data,"added by minio hook")
minio_hook.create_atlas_ps_dir(meta_data1, "added by minio hook")
minio_hook.create_atlas_object(meta_data2, "added by minio hook")
