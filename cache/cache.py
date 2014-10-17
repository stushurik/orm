__author__ = 'olexandr'


class Cache(object):

    data = None

    def __init__(self):
        super(Cache, self).__init__()
        self.data = {}

    def invalidate(self, key):
        self.data[key] = None

    def retrieve(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value