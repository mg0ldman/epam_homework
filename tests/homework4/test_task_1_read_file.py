import tempfile

import pytest

from homework4.task_1_read_file import read_magic_number


def test_read_magic_number_positive():
    """Testing that function returns True with the number
     within a given range"""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b'2')
        tf.seek(0)
        assert read_magic_number(tf.name) is True


def test_read_magic_number_border_value():
    """Testing that function returns True with a border value number"""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b'1')
        tf.seek(0)
        assert read_magic_number(tf.name) is True


def test_read_magic_number_negative():
    """Testing that function returns False with a number
     that is out of a given range"""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b'3')
        tf.seek(0)
        assert read_magic_number(tf.name) is False


def test_read_magic_number_exception():
    """Testing that ValueError is raised if the data
    on the first line in the file is not an integer"""
    with pytest.raises(ValueError, match='An error occurred'):
        with tempfile.NamedTemporaryFile() as tf:
            tf.write(b'a')
            tf.seek(0)
            assert read_magic_number(tf.name) is True


def test_read_magic_number_exception_no_file():
    """Testing that ValueError is raised if
     a file does not exist"""
    with pytest.raises(ValueError, match='An error occurred'):
        read_magic_number('file_name.txt')
