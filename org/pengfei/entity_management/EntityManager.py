from abc import ABC, abstractmethod

from atlasclient.client import Atlas


class EntityManager(ABC):

    def __init__(self, atlas_client):
        self.client = atlas_client

    @abstractmethod
    def create_entity(self, *args, **kwargs):
        pass

    def get_entity(self, guid):
        entity = self.client.entity_guid(guid)
        print("get_result" + str(entity._data))
        return entity.entity

    @staticmethod
    def get_entity_attributes(entity):
        return entity['attributes']

    @staticmethod
    def show_entity_attributes(entity):
        print(entity['attributes'])

    @staticmethod
    def get_s3_attributes_key_list(entity):
        return EntityManager.get_entity_attributes(entity).keys()

    def update_entity(self, guid, attribute_name, attribute_value):
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.entity['attributes'][attribute_name] = attribute_value
        s3_bucket.update(attribute=attribute_name)

    def delete_entity(self, guid):
        s3_bucket = self.client.entity_guid(guid)
        s3_bucket.delete()
