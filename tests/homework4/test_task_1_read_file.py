import tempfile

import pytest

from homework4.task_1_read_file import read_magic_number


def create_temp_file(line):
    def decorator_create_temp_file(func):
        def wrapper(*args):
            with tempfile.NamedTemporaryFile() as tf:
                tf.write(line)
                tf.seek(0)
                return func(tf.name)
        return wrapper
    return decorator_create_temp_file


@create_temp_file(line=b'1')
def test_read_magic_number_positive(filename):
    """Testing that function returns True with the number
     within a given range"""
    assert read_magic_number(filename) is True


@create_temp_file(line=b'2')
def test_read_magic_number_border_value(filename):
    """Testing that function returns True with a border value number"""
    assert read_magic_number(filename) is True


@create_temp_file(line=b'3')
def test_read_magic_number_negative(filename):
    """Testing that function returns False with a number
     that is out of a given range"""
    assert read_magic_number(filename) is False


@create_temp_file(line=b'a')
def test_read_magic_number_exception(filename):
    """Testing that ValueError is raised if the data
    on the first line in the file is not an integer"""
    with pytest.raises(ValueError):
        assert read_magic_number(filename) is True


def test_read_magic_number_exception_no_file():
    """Testing that ValueError is raised if
     a file does not exist"""
    with pytest.raises(ValueError):
        read_magic_number('file_name.txt')
