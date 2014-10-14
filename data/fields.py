import relation


class Field(object):

    connector = None
    _data = None
    field_type = None
    iterator = None

    def __init__(self):
        super(Field, self).__init__()
        self._data = []
        # self.field_type = field_type

    def __call__(self, *args, **kwargs):
        if not self.iterator:
            self.iterator = iter(self._data)

        return self.iterator

    def __setitem__(self, key, item):
        self._data[key] = item

    def __getitem__(self, key):
        return self._data[key] 


class IntegerField(Field):

    def __init__(self):
        super(IntegerField, self).__init__()
        self.field_type = 'int'


class DateField(Field):
    def __init__(self):
        super(DateField, self).__init__()
        self.field_type = 'date'


class CharField(Field):
    def __init__(self):
        super(CharField, self).__init__()
        self.field_type = 'char'


class ForeignKey(Field):

    reference = None
    relation_iter = None
    fk_table = None
    fk_value = None

    def __init__(self, reference):
        super(ForeignKey, self).__init__()
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
        self._data[key] = item

    def __getitem__(self, key):
        fk_relation_class = getattr(relation, self.fk_table.capitalize())
        params = {}
        params[self.fk_value] = self._data[key]
        return fk_relation_class(**params)

