from abc import ABC, abstractmethod

from atlasclient.client import Atlas


class EntityManager(ABC):

    def __init__(self, atlas_client: Atlas):
        self.client = atlas_client

    @abstractmethod
    def create_entity(self, *args, **kwargs) -> None:
        pass

    def get_entity(self, guid: str) -> dict:
        entity = self.client.entity_guid(guid)
        print("get_result" + str(entity._data))
        return entity.entity

    @staticmethod
    def get_entity_attributes(entity: dict) -> dict:
        return entity['attributes']

    @staticmethod
    def show_entity_attributes(entity: dict) -> None:
        print(entity['attributes'])

    @staticmethod
    def get_s3_attributes_key_list(entity: dict) -> list:
        return EntityManager.get_entity_attributes(entity).keys()

    def update_entity(self, guid: str, attribute_name: str, attribute_value: str) -> None:
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.entity['attributes'][attribute_name] = attribute_value
        s3_bucket.update(attribute=attribute_name)

    def delete_entity(self, guid: str) -> None:
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.delete()
