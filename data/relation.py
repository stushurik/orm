__author__ = 'olexandr'

import sys

from data.fields import Field


class Relation(object):

    name = None
    original_source_name = None
    connector = None
    column_names = None

    def __init__(self, *args, **kwargs):        

        super(Relation, self).__init__()
        self.connector.connect()
        self._bind(self.original_source_name, **kwargs)

        for attr in dir(self):
            obj = getattr(self, attr)
            if isinstance(obj, (Field)):
                setattr(obj, "relation", self)     

    def _bind(self, original_source_name, **kwargs):

        column_names, g = self.connector.bind(original_source_name, **kwargs)

        column_count = len(column_names)

        self.column_names = column_names
        # print column_names, column_count

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


        self.connector.save(name=self.original_source_name, fields=fields, count=row_count, pk=pk)



# class RelationFactory(object):
#
#     def get_relation(self, name, original_source_name, fields):
#         return Relation()