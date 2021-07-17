from collections import namedtuple

import pytest

from homework6.oop_2 import (DeadlineError, HomeworkResult, Person, Student,
                             Teacher)

Test_Data = namedtuple('Test_Data',
                       ['opp_teacher', 'advanced_python_teacher',
                        'lazy_student', 'good_student', 'expired_homework',
                        'oop_hw', 'docs_hw', 'result_1',
                        'result_2', 'result_3'])


@pytest.fixture
def test_data(scope='session'):
    """Creating class instances for running the tests"""
    opp_teacher = Teacher('Shadrin', 'Daniil')
    advanced_python_teacher = Teacher('Smetanin', 'Aleksandr')
    lazy_student = Student('Petrov', 'Roman')
    good_student = Student('Sokolov', 'Lev')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)
    expired_homework = advanced_python_teacher.\
        create_homework('Read Python Zen', 0)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    return Test_Data(opp_teacher, advanced_python_teacher,
                     lazy_student, good_student, expired_homework,
                     oop_hw, docs_hw, result_1, result_2, result_3)


def test_student_attributes(test_data):
    """Testing that the attributes of a class Student are correct"""
    assert test_data.good_student.last_name == 'Sokolov'
    assert test_data.good_student.first_name == 'Lev'


def test_teacher_attributes(test_data):
    """Testing that the attributes of a class Teacher are correct"""
    assert test_data.opp_teacher.last_name == 'Shadrin'
    assert test_data.opp_teacher.first_name == 'Daniil'


def test_teacher_create_homework_method(test_data):
    """Testing that the attributes of created homework are correct"""
    assert test_data.oop_hw.text == 'Learn OOP'
    assert test_data.oop_hw.deadline == '1 day(s), 0:00:00'


def test_teacher_check_homework_method_positive(test_data):
    """Testing that 'check_homework' returns
     True and saves a HW object to 'homework_done'
     when HomeworkResult object's attribute solution has more than 5 symbols"""
    assert test_data.opp_teacher.check_homework(test_data.result_1) is True
    assert test_data.oop_hw in test_data.opp_teacher.homework_done


def test_teacher_check_homework_method_negative(test_data):
    """Testing that 'check_homework' returns False and doesn't save
    a HW object to 'homework_done' when HomeworkResult object's
    attribute solution has less than 5 symbols"""
    assert test_data.opp_teacher.check_homework(test_data.result_3) is False
    assert test_data.docs_hw not in test_data.opp_teacher.homework_done


def test_teacher_homework_done_class_attribute(test_data):
    """Testing that 'homework_done' is a class attribute
    that is shared by all instances of a Teacher class"""
    test_data.opp_teacher.check_homework(test_data.result_1)
    temp_1 = test_data.opp_teacher.homework_done
    test_data.advanced_python_teacher.check_homework(test_data.result_2)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_teacher_reset_result_with_argument(test_data):
    """Testing that 'reset_results' method deletes only its argument
    from class attribute 'homework_done' """
    test_data.opp_teacher.check_homework(test_data.result_1)
    test_data.opp_teacher.check_homework(test_data.result_2)
    test_data.opp_teacher.reset_results(test_data.result_2)
    assert test_data.result_2 not in test_data.opp_teacher.homework_done


def test_teacher_reset_result_no_arguments(test_data):
    """Testing that 'reset_results' method clears
    class attribute 'homework_done' when no argument was provided"""
    test_data.opp_teacher.check_homework(test_data.result_1)
    test_data.opp_teacher.check_homework(test_data.result_2)
    test_data.opp_teacher.reset_results()
    assert not Teacher.homework_done


def test_student_homework_result_attributes(test_data):
    """Testing that the attributes of a class HomeworkResult are correct"""
    assert test_data.result_1.homework.text == 'Learn OOP'
    assert test_data.result_1.solution == 'I have done this hw'
    assert test_data.result_1.author == test_data.good_student


def test_student_homework_result_wrong_object_exception(test_data):
    """Testing that TypeError with a message 'You gave not a Homework object'
    is raised if homework parameter is not an instance of a class Homework"""
    with pytest.raises(TypeError, match='You gave not a Homework object'):
        assert HomeworkResult(test_data.good_student,
                              'abc', test_data.opp_teacher)


def test_student_do_homework_deadline_exception(test_data):
    """Testing that a DeadlineError is raised when the homework is expired"""
    with pytest.raises(DeadlineError, match='You are late!'):
        test_data.good_student.do_homework(test_data.expired_homework, 'abc')


def test_student_teacher_inheritance(test_data):
    """Testing that instances of Student and Teacher classes
     are also instances of a class Person"""
    assert all(isinstance(i, Person) for i
               in (test_data.opp_teacher, test_data.good_student))
