from atlasclient.client import Atlas


class EntityFinderByAttributes:
    def __init__(self, host_name, port_number, user_name, password):
        self.host_name = host_name
        self.port_number = port_number
        self.user_name = user_name
        self.password = password
        self.client = Atlas(host_name, port_number, username=user_name, password=password)

    def search_by_attribute(self, type_name, attribute_name, attribute_value):

        params = {'typeName': type_name, 'attrName': attribute_name, 'attrValue': attribute_value, 'offset': '1',
                  'limit': '10'}

        search_results = self.client.search_attribute(**params)
        #  Info about all entities in one dict
        for s in search_results:
            print(s._data)
            #  Getting name and guid of each entity
        for s in search_results:
            for e in s.entities:
                print(e.name)
                print(e.guid)

    def search_full_text(self, type_name, attribute_value):
        params = {'typeName': type_name, 'attrValue': attribute_value, 'offset': '1',
                  'limit': '10'}
        search_results = self.client.search_basic(**params)

        #  Getting name and guid of each entity
        for s in search_results:
            print("have result: ")
            for e in s.entities:
                print("have result: ")
                print(e.name)
                print(e.guid)
