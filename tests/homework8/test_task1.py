import tempfile

import pytest

from homework8.task1 import KeyValueStorage


def create_temp_file(lines):
    """A decorator that creates a temporary file with
    sample data"""
    def decorator_create_temp_file(func):
        def wrapper(*args):
            with tempfile.NamedTemporaryFile() as tf:
                tf.write(lines)
                tf.seek(0)
                return func(tf.name)
        return wrapper
    return decorator_create_temp_file


@create_temp_file(lines=b'name=kek\n'
                        b'last_name=top\n'
                        b'power=9001\n')
def test_attributes_values(file_path):
    """Testing that values are accessible both as elements of collection(dict)
    and attributes"""
    storage = KeyValueStorage(file_path)
    assert storage['name'] == 'kek'
    assert storage.last_name == 'top'
    assert storage.power == 9001


@create_temp_file(lines=b'1=one\n')
def test_value_error(file_path):
    """Testing that ValueError is raised when key is an integer"""
    with pytest.raises(ValueError, match='The key should be a string'):
        assert KeyValueStorage(file_path)
