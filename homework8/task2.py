"""
Write a wrapper class TableData for database table, that when initialized with
database name and table acts as collection
object (implements Collection protocol).
Assume all data has unique values in 'name' column.

So, if presidents = TableData(database_name=
'example.sqlite', table_name='presidents')
then
len(presidents) will give current amount of
rows in presidents table in database
presidents['Yeltsin'] should return single
data row for president with name Yeltsin
'Yeltsin' in presidents should return
if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.
Avoid reading entire table into memory. When iterating
through records, start reading the first record,
then go to the next one, until records are exhausted.
When writing tests, it's not always necessary
to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import sqlite3


def connect_db(f):
    """A decorator that opens a connection to the DB,
     initialises the cursor and closes it automatically"""
    def wrapper(self, *args, **kwargs):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        try:
            return f(self, cursor, *args, **kwargs)
        finally:
            cursor.close()

    return wrapper


class TableData:
    """A wrapper class for database table, that when initialized
     with database name and table acts as a
     collection object (implements Collection protocol)

    :param database_name: a name of the database that we plan to connect
    :type database_name: str
    :param table_name: a name of the table within the DB
    :type table_name: str
    """
    def __init__(self, database_name, table_name):
        """Constructor method
        """
        self.database_name = database_name
        self.table_name = table_name

    @connect_db
    def __len__(self, cursor):
        """Method __len__ returns a current number of rows in a given table of the db

        :param cursor: a cursor that was created in @connect_db decorator
        :type cursor: an instance of the :class: 'sqlite3.Cursor'
        :return: returns a current number of rows in a given table of the db
        :rtype: int
        """
        cursor.execute(f'SELECT count(*) from {self.table_name}')
        return cursor.fetchone()[0]

    @connect_db
    def __getitem__(self, cursor, name):
        """Method __getitem__ returns a single row from the table of a specific name

        :param cursor: a cursor that was created in @connect_db decorator
        :type cursor: an instance of the :class: 'sqlite3.Cursor'
        :param name: specifies the value of the column 'name'
        for the entry that is to be returned
        :type name: str
        :return: returns a single row from the table of a specific name
        :rtype: tuple
        """
        cursor.execute(f'SELECT * from {self.table_name}'
                       f' where name=:name', {'name': name})
        return cursor.fetchone()

    @connect_db
    def __contains__(self, cursor, name):
        """Returns if an entry with a specified name is present in table

        :param cursor: a cursor that was created in @connect_db decorator
        :type cursor: an instance of the :class: 'sqlite3.Cursor'
        :param name: specifies the value of the column 'name' for
        the entry whose presence in the table is to be checked
        :type name: str
        :return: returns True if an entry with
        the specified name is present in the table
        :rtype: bool
        """
        cursor.execute(f'SELECT * from {self.table_name}'
                       f' where name=:name', {'name': name})
        return cursor.fetchone()

    def __iter__(self):
        """Initializes an iterator protocol for the table
        """
        self.n = 0
        return self

    def __next__(self):
        """Method allowing to get the next element from the table

        :return: returns the next element from the iterable(table)
        :rtype: str
        :raises StopIteration: if the number of elements
        previously returned is more or equal to the value of __len__
        """
        if self.n < self.__len__():
            self.n += 1
            return self
        else:
            raise StopIteration
