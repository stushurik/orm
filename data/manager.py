__author__ = 'olexandr'


class DataManager(object):
    # cache = None
    relations = None

    def __init__(self, relations):
        super(DataManager, self).__init__()
        self.relations = relations

    def __getitem__(self, key):

        return self.relations.get(key)

    def selection(self, relation, attributes):
        # self.cache.retrieve()
        pass

    def project(self, relation, attributes):
        # self.cache.retrieve()
        pass

    def union(self, relation_a, relation_b):
        # self.cache.retrieve()
        pass

    def intersection(self, relation_a, relation_b):
        # self.cache.retrieve()
        pass

    def difference(self, relation_a, relation_b):
        # self.cache.retrieve()
        pass

    def multiplication(self, relation_a, relation_b):
        # self.cache.retrieve()
        pass

    def division(self, relation_a, relation_b):
        # self.cache.retrieve()
        pass

    def connection(self, relation_a, relation_b, attributes):
        # self.cache.retrieve()
        pass

    def get_relation_by_name(self, name):
        # self.cache.retrieve()
        pass