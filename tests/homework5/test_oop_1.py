from collections import namedtuple

import pytest

from homework5.oop_1 import Student, Teacher

Test_Data = namedtuple('Test_Data', ['teacher', 'student',
                                     'expired_homework', 'oop_homework'])


@pytest.fixture
def test_data(scope='session'):
    """Creating class instances for running the tests"""
    teacher = Teacher('Shadrin', 'Daniil')
    student = Student('Petrov', 'Roman')
    expired_homework = teacher.create_homework('Learn functions', 0)
    oop_homework = teacher.create_homework('create 2 simple classes', 5)
    return Test_Data(teacher, student, expired_homework, oop_homework)


def test_teacher_attributes(test_data):
    """Testing that the attributes of a class Teacher are correct"""
    assert test_data.teacher.last_name == 'Shadrin'
    assert test_data.teacher.first_name == 'Daniil'


def test_student_attributes(test_data):
    """Testing that the attributes of a class Student are correct"""
    assert test_data.student.last_name == 'Petrov'
    assert test_data.student.first_name == 'Roman'


def test_homework_attributes(test_data):
    """Testing that the attributes of a class Homework are correct"""
    assert test_data.expired_homework.deadline == '0:00:00'
    assert test_data.oop_homework.deadline == '5 day(s), 0:00:00'
    assert test_data.expired_homework.text == 'Learn functions'


def test_student_do_homework_method_expired(test_data, capsys):
    """Testing that Student's method 'do_homework' returns a correct result
    with an expired instance of a Homework class"""
    test_data.student.do_homework(test_data.expired_homework)
    captured = capsys.readouterr()
    assert captured.out == 'You are late\n'
