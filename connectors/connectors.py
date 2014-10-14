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
    password = 'qweasd'
    database = 'diploma'

    def connect(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host
        )

        # self.

    def _make_where_statement(self, **kwargs):
        condition = ""
        for key, value in kwargs.items():
            condition += " %s = %s AND" % (key, value)

        return "WHERE %s true" % condition


    def bind(self, table, **kwargs):
        
        # print kwargs
        where = self._make_where_statement(**kwargs)
        # print where

        query = "SELECT * FROM %s\n%s " % (table, where)
        cursor = self.connection.cursor()
        cursor.execute(query, ())

        # print cursor.column_names

        return cursor.column_names, iter(cursor.fetchall())

