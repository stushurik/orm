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

        # try:
        #     return next(self.iterator)
        # except StopIteration:
        #     return None


    # def set_data(self):


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

    def __init__(self, reference):
        super(ForeignKey, self).__init__()
        self.field_type = 'fk'
        self.reference = reference

