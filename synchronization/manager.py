__author__ = 'olexandr'


class SynchronizationManager(object):

    connectors = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SynchronizationManager, cls).__new__(cls)
        return cls.instance

    def set_changes(self):
        for connector in self.connectors:
            connector.cache.invalidate()