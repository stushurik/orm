import json
from cache.cache import Cache
from connectors.connectors import Connector, MySqlConnector
from data import relation
from data.fields import IntegerField, DateField, CharField, ForeignKey
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
        self._parse_model(model, connector)

        # self.cache = Cache()
        data_manager = DataManager()
        self.data_managers.append(data_manager)

        return data_manager

    def _field_by_type(self, field_type):
        if field_type == 'int':
            return IntegerField
        elif field_type == 'date':
            return DateField
        elif field_type == 'char':
            return CharField
        elif field_type == 'fk':
            return ForeignKey
        else:
            return None

    def _parse_model(self, path, connector):

        relations = []

        with open(path) as model_file:
            model = model_file.readlines()

        model_object = json.loads(''.join(model))

        for table in model_object['tables']:

            fields = table['fields']
            attrs = {

                'connector': connector

            }

            for field in fields:
                if field['type'] == 'fk':
                    attrs[field['name']] \
                        = self._field_by_type(field['type'])(field['reference'])
                else:
                    attrs[field['name']] \
                        = self._field_by_type(field['type'])()

            attrs['__module__'] = relation.__name__

            model_name = str(table['name']).capitalize()
            NewRelation = type(model_name, (relation.Relation,), attrs)

            NewRelation.original_source_name = table['name']

            setattr(relation, model_name, NewRelation)

            relations.append(NewRelation)

        return relations
