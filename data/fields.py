import relation


class Field(object):

    _data = None
    field_type = None
    iterator = None
    name = None
    # _current = None

    def __init__(self, name):
        super(Field, self).__init__()
        self._data = []
        self.name = name
        # self.field_type = field_type

    def __call__(self, *args, **kwargs):
        if not self.iterator:
            self.iterator = iter(self._data)

        return self.iterator

    def __setitem__(self, key, item):
        try:
            self._data[key] = item
        except IndexError:
            self._data.append(item)
        
        # self.relation.update()

    def __getitem__(self, key):
        print dir(self)
        return self._data[key]

    # def __iter__(self):
    #     if not self.iterator:
    #         self.iterator = iter(self._data)                 # Get iterator object on iter
    #     return self.iterator

    # def __next__(self):                 # Return a square on each iteration
    #     if self.value == self.stop:     # Also called by next built-in
    #         raise StopIteration
    #     self.value += 1
    #     return self.value ** 2


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name)
        self.field_type = 'int'

class PrimaryKey(Field):

    def __init__(self, name):
        super(PrimaryKey, self).__init__(name)
        self.field_type = 'pk'


class DateField(Field):
    def __init__(self, name):
        super(DateField, self).__init__(name)
        self.field_type = 'date'


class CharField(Field):
    def __init__(self, name):
        super(CharField, self).__init__(name)
        self.field_type = 'char'


class ForeignKey(Field):

    reference = None
    relation_iter = None
    fk_table = None
    fk_value = None

    def __init__(self, name, reference):
        super(ForeignKey, self).__init__(name)
        self.field_type = 'fk'
        self.fk_table, self.fk_value = reference.split(".")

    def __call__(self, *args, **kwargs):
        
        iterator = super(ForeignKey, self).__call__(*args, **kwargs)

        # print dir(relation)

        try:
            # print 'asdasd', self.fk_table

            fk_relation_class = getattr(relation, self.fk_table.capitalize())

            # print 'sdfsdfs', fk_relation_class

            params = {}
            params[self.fk_value] = next(iterator)

            # print params

            return fk_relation_class(**params)


        except StopIteration:
            pass



        #     for v in self.fk_field():

        #         
        #         fk_relation_class = getattr(sys.modules[__name__], fk_table.capitalize())
        #         print fk_relation_class

    def __setitem__(self, key, item):
        super(ForeignKey, self).__setitem__(key, item)
        self._data[key] = item

    def __getitem__(self, key):
        fk_relation_class = getattr(relation, self.fk_table.capitalize())
        params = {}
        params[self.fk_value] = self._data[key]
        return fk_relation_class(**params)

