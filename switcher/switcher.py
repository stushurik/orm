import json
from cache.cache import Cache
from connectors.connectors import Connector, MySqlConnector
from data import relation
from data.fields import IntegerField, DateField, CharField, ForeignKey, \
    PrimaryKey
from data.manager import DataManager
from synchronization.manager import SynchronizationManager

__author__ = 'olexandr'


class SourceSwitcher(object):
    synchronization_manager = None
    cache = None
    data_managers = []

    def __new__(cls):

        cls.synchronization_manager = SynchronizationManager()

        if not hasattr(cls, 'instance'):
            cls.instance = super(SourceSwitcher, cls).__new__(cls)
        return cls.instance

    def set_model(self, model):

        connector = \
            MySqlConnector(self.synchronization_manager)

        self.synchronization_manager.connectors.append(connector)
        # self.cache = Cache()
        data_manager = DataManager(self._parse_model(model, connector))
        self.data_managers.append(data_manager)

        return data_manager

    def _parse_model(self, path, connector):

        relations = {}

        with open(path) as model_file:
            model = model_file.readlines()

        model_object = json.loads(''.join(model))

        for table in model_object['tables']:
            attrs = {'connector': connector, 'fields': table['fields'],
                     '__module__': relation.__name__}

            model_name = str(table['name']).capitalize()
            NewRelation = type(model_name, (relation.Relation,), attrs)

            NewRelation.original_source_name = table['name']

            setattr(relation, model_name, NewRelation)

            relations[model_name] = NewRelation

        return relations
