__author__ = 'olexandr'


class Relation(object):

    name = None
    original_source_name = None
    connector = None

    def __init__(self):
        super(Relation, self).__init__()
        self.connector.connect()
        self._bind(self.original_source_name)

    def _bind(self, original_source_name):
        column_names, g = self.connector.bind(original_source_name, None)

        column_count = len(column_names)

        print column_names

        try:
            for row in g:
                print row
                for i in range(column_count):
                    field = getattr(self, column_names[i])
                    field._data.append(row[i])

            # print next(self.fk_field())
            for v in self.fk_field():
                print v, self.fk_field.reference

        except StopIteration:
            pass



# class RelationFactory(object):
#
#     def get_relation(self, name, original_source_name, fields):
#         return Relation()