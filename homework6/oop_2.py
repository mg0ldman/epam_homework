"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from collections import defaultdict
from datetime import datetime, timedelta


class Person:
    """A parent class for Student and Teacher

    :param last_name: Person's lastname
    :type last_name: str
    :param first_name: Person's firstname
    :type first_name: str
    """
    def __init__(self, last_name, first_name):
        """Constructor method
        """
        self.last_name = last_name
        self.first_name = first_name


class Teacher(Person):
    """A class that helps create teacher's profile, constructor method
    is inherited from :class: 'Person'
    """
    homework_done = defaultdict(set)

    def create_homework(self, text, deadline):
        """Creates an object of :class: 'Homework'
        with the description and deadline.

        :param text: assignment's description
        :type text: str
        :param deadline: number of days to complete the assignment
        :type deadline: int
        :return: a Homework object
        :rtype: instance of a :class:'Homework'

        """
        homework = Homework(text, deadline)
        return homework

    def check_homework(self, homework_result):
        """Checks homework result.

        :param homework_result: a result of
        a do_homework method of :class:'Student'
        :type homework_result: :class:'HomeworkResult'
        :return: 'True' if homework_result.solution argument has
        more than 5 characters, 'False' otherwise.
        If 'True' is returned the homework_result is also added
        to homework_done (a class attribute) of :class:'Teacher',
        not added otherwise.
        :rtype: bool
        """
        if len(homework_result.solution) > 5:
            try:
                return True
            finally:
                Teacher.homework_done[
                    homework_result.homework].add(homework_result)
        else:
            return False

    def reset_results(*args, homework=None):
        """Removes results of a specific homework
         from homework_done if any argument is passed,
         removes results of all homeworks if no argument was passed.

        :param homework: an instance of a :class:'Homework', defaults to None
        :type homework: :class:'Homework', optional
        :rtype: None
        """
        if homework:
            Teacher.homework_done.pop(homework, None)
        else:
            Teacher.homework_done.clear()


class Student(Person):
    """A class that helps create student's profiles"""
    def do_homework(self, homework, solution):
        """Returns instance of a :class:'HomeworkResult' if it's not expired,
        raises a DeadlineError otherwise

        :param homework: an instance of a :class:'Homework'
        :type homework: :class:'Homework'
        :param solution: text with the solution to homework
        :type solution: str
        :return: instance of a :class:'HomeworkResult'
        if the task is not expired,
        raises a DeadlineError with a message 'You are late!' otherwise
        """
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError('You are late!')


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
        """Constructor method
        """
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


class HomeworkResult:
    """Returns a homework result instance,
    created in do_homework method of :class:'Student'

    :param homework: instance of a :class:'Homework'
    :type homework: :class:'Homework'
    :param solution: solution to homework
    :type solution: str
    :param author: instance of a :class:'Student'
    :type author: :class:'Student'
    :param created: an exact day and time when homework was done
    :type created: :class:'datetime.datetime'
    :raise TypeError: raises TypeError with a message
    'You gave not a Homework object'
    if homework parameter is not an instance of a :class:'Homework'
    """
    def __init__(self, homework, solution, author):

        self.author = author
        self.homework = homework
        if not isinstance(homework, Homework):
            raise TypeError('You gave not a Homework object')
        self.solution = solution
        self.created = datetime.now()


class DeadlineError(Exception):
    """An exception that is raised when a Student tries
    to do the Homework which is past due"""
    pass
