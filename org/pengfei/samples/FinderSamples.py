from org.pengfei.atlas_client.client import Atlas
from org.pengfei.entity_search.EntityFinder import EntityFinder

atlas_hostname = "localhost"
atlas_port = 21000
atlas_login = "admin"
atlas_pwd = "admin"

atlas_client = Atlas(atlas_hostname, atlas_port, username=atlas_login, password=atlas_pwd)
finder = EntityFinder(atlas_client)
finder.search_by_attribute("aws_s3_bucket", "owner", "foobar")

search_result = finder.search_full_text("aws_s3_bucket", "test")

EntityFinder.show_search_results(search_result)
entity_number = EntityFinder.get_entity_number(search_result)
print("Find " + str(entity_number) + " result in total")

guid_list = EntityFinder.get_result_entity_guid_list(search_result)

for guid in guid_list:
    print("result:" + guid)
