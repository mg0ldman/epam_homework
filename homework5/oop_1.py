"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta


class Homework:
    """A class that helps create Homework tasks, based on text and deadline.
    Used in :class:'Teacher'
    :param text: assignment's description
    :type text: str
    :param deadline: number of days to complete the assignment
    :type deadline: int
    :param created: an exact day and time when assignment was created
    :type created: :class:'datetime.datetime'
    """
    def __init__(self, text, deadline):
        self.text = text
        if deadline < 1:
            self.deadline = '0:00:00'
        else:
            self.deadline = f'{deadline} day(s), 0:00:00'
        self.created = datetime.now()

    def is_active(self):
        """Checks whether the assignment is expired or not,
        based on its deadline parameter
        :return: 'True' if the task is not expired, 'False' otherwise
        :rtype: bool
        """
        if int(self.deadline[0]) > 0:
            return self.created + \
                timedelta(days=int(self.deadline.split()[0])) > datetime.now()
        else:
            return False


class Student:
    """A class that helps create student's profiles

    :param last_name: student's lastname
    :type last_name: str
    :param first_name: student's firstname
    :type first_name: str
    """

    def __init__(self, last_name, first_name):
        """Constructor method
        """
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        """Returns homework's text if
        the task is not expired or prints 'You are late' otherwise

        :param homework: an instance of a :class:'Homework'
        :type homework: :class:'Homework'
        :return: instance of a :class:'HomeworkResult'
        :rtype: str or None if the task is expired ('You are late' printed)
        if the task is not expired,
        """
        if homework.is_active():
            return homework.text
        else:
            print('You are late')


class Teacher:
    """A class that helps create teacher's profiles

    :param last_name: student's lastname
    :type last_name: str
    :param first_name: student's firstname
    :type first_name: str
    """
    def __init__(self, last_name, first_name):
        """Constructor method
        """
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        """Creates an object of :class: 'Homework'
        with the description and deadline.

        :param text: assignment's description
        :type text: str
        :param deadline: number of days to complete the assignment
        :type deadline: int
        :return: a Homework object
        :rtype: instance of a :class:'Homework'"""
        homework = Homework(text, deadline)
        return homework
