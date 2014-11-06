__author__ = 'olexandr'

import sys
from sets import Set

from data.fields import Field, field_by_type


class Relation(object):
    name = None
    original_source_name = None
    connector = None
    column_names = None

    __params = None
    __filter_params = None

    def __init__(self, *args, **kwargs):

        super(Relation, self).__init__()
        self.connector.connect()
        self.__params = kwargs
        self.__filter_params = []

        # self._bind(self.original_source_name, **kwargs)

        # for attr in dir(self):
        # obj = getattr(self, attr)
        # if isinstance(obj, (Field)):
        #         setattr(obj, "relation", self)

        for field in self.fields:
            if field['type'] == 'fk':
                setattr(self, field['name'],
                        field_by_type(field['type'])(
                            field['name'], self, field['reference'])
                        )
            else:
                setattr(self, field['name'],
                        field_by_type(field['type'])(field['name'], self)
                        )

    def filter(self, **kwargs):
        self.__filter_params.append(kwargs)

        return self

    def _clear_filter_params(self):
        del self.__filter_params[:]

    def _bind(self, original_source_name, **kwargs):

        # print self.__params, self.__filter_params

        self.__filter_params.append(self.__params.copy())

        key_set = Set()
        values = []

        result_params = {}

        for filters in self.__filter_params:
            values.append(filters)
            for key in filters.keys():
                # print key
                key_set.add(key)

        # print key_set

        for key in key_set:
            # print key
            for param_dict in values:

                if not result_params.get(key):
                    result_params[key] = [param_dict.get(key)]
                else:
                    result_params[key].append(param_dict.get(key))

        # print result_params

        for key, value in result_params.items():
            res = filter(None, value)
            result_params[key] = res
        # print result_params


        column_names, g = self.connector.bind(original_source_name,
                                              **result_params)

        column_count = len(column_names)

        self.column_names = column_names

        try:
            for row in g:
                for i in range(column_count):
                    field = getattr(self, column_names[i])
                    field._data.append(row[i])
        except StopIteration:
            pass

    def save(self):

        fields = {}
        row_count = 0
        pk = ""
        for i in range(len(self.column_names)):
            field = getattr(self, self.column_names[i])

            if field.field_type == 'pk':
                pk = field.name

            values = []

            for value in field():
                values.append(value)

            fields[field.name] = values

            if row_count < len(values):
                row_count = len(values)

        self.connector.save(name=self.original_source_name, fields=fields,
                            count=row_count, pk=pk)



        # class RelationFactory(object):
        #
        # def get_relation(self, name, original_source_name, fields):
        # return Relation()