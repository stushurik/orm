__author__ = 'olexandr'

import sys


class Relation(object):

    name = None
    original_source_name = None
    connector = None

    def __init__(self, *args, **kwargs):        

        super(Relation, self).__init__()
        self.connector.connect()
        self._bind(self.original_source_name, **kwargs)

    def _bind(self, original_source_name, **kwargs):

        column_names, g = self.connector.bind(original_source_name, **kwargs)

        column_count = len(column_names)
        # print column_names, column_count

        try:
            for row in g:
                for i in range(column_count):
                    field = getattr(self, column_names[i])
                    field._data.append(row[i])

            # self.fk_field()
            # self.fk_field()

            # for v in self.fk_field():

            #     fk_table, fk_value = self.fk_field.reference.split(".")
            #     fk_relation_class = getattr(sys.modules[__name__], fk_table.capitalize())
            #     print fk_relation_class

        except StopIteration:
            pass



# class RelationFactory(object):
#
#     def get_relation(self, name, original_source_name, fields):
#         return Relation()