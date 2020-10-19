from org.pengfei.atlas_client.client import Atlas


class EntityFinder:
    def __init__(self, atlas_client: Atlas):
        self.client = atlas_client

    def search_by_attribute(self, type_name: str, attribute_name: str, attribute_value: str) -> dict:
        params = {'typeName': type_name, 'attrName': attribute_name, 'attrValue': attribute_value, 'offset': '1',
                  'limit': '10'}
        return self.client.search_attribute(**params)

    def search_full_text(self, type_name: str, attribute_value: str) -> dict:
        params = {'typeName': type_name, 'attrValue': attribute_value, 'offset': '1',
                  'limit': '10'}
        return self.client.search_basic(**params)

    @staticmethod
    def show_search_results(search_results: dict) -> None:
        for s in search_results:
            print("Search query response: " + str(s._data))

    @staticmethod
    def get_entity_number(search_results: dict) -> int:
        size = 0
        for s in search_results:
            size += 1
        if size == 0 or size > 1:
            raise ValueError
        else:
            return len(next(iter(search_results)).entities)

    @staticmethod
    def get_result_entity_guid_list(search_results: dict) -> list:
        size = 0
        guid_list = []
        for s in search_results:
            size += 1
        if size == 0 or size > 1:
            raise ValueError
        else:
            for entity in next(iter(search_results)).entities:
                guid_list.append(entity.guid)
        return guid_list
