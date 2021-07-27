from collections import namedtuple

import pytest

from homework8.task2 import TableData

TestData = namedtuple('TestData', ['presidents', 'books'])


@pytest.fixture
def test_data():
    """Creating python fixture with sample data"""
    presidents = TableData(database_name='tests/homework8/example.sqlite',
                           table_name='presidents')
    books = TableData(database_name='tests/homework8/example.sqlite',
                      table_name='books')
    return TestData(presidents, books)


def test_tabledata_method_len(test_data):
    """Testing that method __len__ returns a correct
     length of specified tables from DB"""
    assert len(test_data.presidents) == 3
    assert len(test_data.books) == 3


def test_tabledata_method_getitem(test_data):
    """Testing that method __getitem__ returns correct entries from the tables
    with specified values"""
    assert test_data.presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    assert test_data.books['Farenheit 451'] == ('Farenheit 451', 'Bradbury')


def test_tabledata_method_contains(test_data):
    """Testing that method __contains__ resurns a correct result when entries
     with specified values are present in the tables"""
    assert 'Yeltsin' in test_data.presidents
    assert 'Farenheit 451' in test_data.books


def test_tabledata_method_iter(test_data):
    """Testing that method __iter__ works correctly and it's
     possible to use tables as iterable """
    assert [president['Yeltsin'] for president in test_data.presidents] ==\
           [('Yeltsin', 999, 'Russia'), ('Yeltsin', 999, 'Russia'),
            ('Yeltsin', 999, 'Russia')]


def test_tabledata_raises_stopiteration(test_data):
    """Testing that StopIteration is raised when method __next__ is called
    more times than the number of entries within the table"""
    with pytest.raises(StopIteration):
        custom_iter = iter(test_data.presidents)
        next(custom_iter)
        next(custom_iter)
        next(custom_iter)
        next(custom_iter)


def test_tabledata_updates(test_data):
    """Testing that method __len__ returns correct result
     even after adding a new entry"""
    import sqlite3
    conn = sqlite3.connect(test_data.presidents.database_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM presidents')
    assert len(cursor.fetchall()) == 3
    cursor.execute('INSERT INTO presidents (name,age,country) VALUES (?,?,?)',
                   ('Bush', 123, 'America'))
    cursor.execute('SELECT * FROM presidents')
    assert len(cursor.fetchall()) == 4
