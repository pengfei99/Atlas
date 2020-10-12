from org.pengfei.entity_search.EntityFinderByAttributes import EntityFinderByAttributes

finder = EntityFinderByAttributes("localhost", 21000, "admin", "admin")
finder.search_by_attribute("aws_s3_bucket", "owner", "foobar")

finder.search_full_text("aws_s3_bucket", "test")
