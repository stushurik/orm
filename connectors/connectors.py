import mysql.connector
from cache.cache import Cache
from utils.utils import SOURCE_TYPES

__author__ = 'olexandr'


class Connector(object):
    synchronization_manager = None
    source_type = SOURCE_TYPES[1]

    connection = None
    # cursor = None

    host = '127.0.0.1'
    port = None
    user = None
    password = None

    # relations = []
    # data_manager = None
    cache = Cache()

    def __init__(self, synchronization_manager, **kwargs):
        super(Connector, self).__init__()
        # self.relations = relations  # holds classes that represent entities in data sources
        self.synchronization_manager = synchronization_manager
        # self.cache = Cache()
        # self.data_manager = DataManager(self.cache)

        # for key, value in kwargs.items():
        #     # self[key] =

    # def get_data_manager(self):
    #     return self.data_manager

    def connect(self):
        pass

    def get_data(self, relation):
        #transaction
        pass

    def insert_data(self, relation):
        #transaction
        self._set_changes()

    def update_data(self, relation):
        # ids are required
        #transaction
        self._set_changes()

    def delete_data(self, relation):
        #transaction
        self._set_changes()

    def _set_changes(self):
        self.synchronization_manager.set_changes()

    def close(self):
        pass


class MySqlConnector(Connector):

    # database = None
    user = 'root'
    password = 'n9vkshuri2k'
    database = 'diploma'

    def connect(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host
        )

    def _make_where_statement(self, **kwargs):
        condition = ""
        for key, value in kwargs.items():
            if len(value) == 1:                
                condition += " %s = '%s' AND" % (key, value[0])
            else:
                condition += " %s IN (%s) AND" % (key, ', '.join([ "'" + str(val) + "'" for val in value]) )

        return "WHERE %s true" % condition


    def bind(self, table, **kwargs):

        kwargs_part = ''
        key = table

        for dict_key,value in kwargs.items():
            kwargs_part += dict_key + '-' + str(value)

        if kwargs_part: key = table + '-' + kwargs_part


        if self.cache.retrieve(key):
            print "from cache"
            return self.cache.retrieve(key)
        else:

            print "from DB"
        
            where = self._make_where_statement(**kwargs)

            print where

            query = "SELECT * FROM %s\n%s " % (table, where)

            cursor = self.connection.cursor()
            cursor.execute(query, ())

            data = iter(cursor.fetchall())
            column_names = cursor.column_names
            cursor.close()

            self.cache.set(key, (column_names, data))
            
            return column_names, data

    def save(self, **kwargs):

        name = kwargs['name']
        fields = kwargs['fields']
        count = kwargs['count']
        pk = kwargs['pk']

        columns = fields.keys()


        rows = []
        for i in xrange(count):
            i_row = []
            for key in fields.keys():
                try:
                    i_row.append({"name": key, "value": fields[key][i]})
                except IndexError:
                    i_row.append({"name": key, "value":None})

            rows.append(i_row)

        last_id = fields[pk][len(fields[pk])-1]
        # print last_id

        for row in rows:
            values = []
            for value in row:

                if value['name'] == pk:
                    print value['value'] 
                    if value['value']:
                        func = self._update_data
                    else:
                        value['value'] = last_id + 1
                        func = self._insert_data

                values.append(value['value'] if value['value'] else u"null")

            # print values

            params = {
                "name" : name,
                "fields" : fields,
                "values" : values,
                "pk": pk
            }

            func(**params)
                

        #     if 

    def _insert_data(self, **kwargs):

        print "insert"

        name = kwargs['name']
        values = kwargs['values']
        fields = kwargs['fields']



        insert = ("INSERT INTO %s " % name + 
              "(" + ", ".join(fields) + ")\n")
              
        params = []
        for j in xrange(len(values)):
            params.append('%s')

        
        insert = insert + "VALUES (" + ", ".join(params) + ");"

        cursor = self.connection.cursor()
        cursor.execute(insert, values)


        self.connection.commit()
        cursor.close()



        self._set_changes()


    def _update_data(self, **kwargs):

        print "update"

        name = kwargs['name']
        values = kwargs['values']
        fields = kwargs['fields']
        pk = kwargs['pk']


        update = "UPDATE %s \n" % name
        where = ""

        new_pattern = []
        new_values = []
        for column, value in zip(fields, values):
            if column == pk:
                where = self._make_where_statement(**{column: value})

            else:
                new_pattern.append(column +" = %s")
                new_values.append(value)
                # print column +"="+str(value)

        sets = "SET %s \n" % ", ".join(new_pattern) 

        sql = update + sets + where

        print sql    

        cursor = self.connection.cursor()
        cursor.execute(sql, new_values)


        self.connection.commit()
        cursor.close()



        self._set_changes()