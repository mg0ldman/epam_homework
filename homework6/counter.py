"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """A class decorator for any class that adds an instance counter
    and two extra methods:
    get_created_instances - returns
    the number of class instances
    reset_instances_counter - returns
    the number of class instances and then resets it
    """
    setattr(cls, 'cnt', 0)

    def __init__(self):
        """A method that creates class instances and counts their number"""
        cls.cnt += 1

    setattr(cls, '__init__', __init__)

    def get_created_instances(*args):
        """A method that returns a number of
         created instances of a given class"""
        return cls.cnt

    setattr(cls, 'get_created_instances', get_created_instances)

    def reset_instances_counter(*args):
        """A method that returns a number of
        created instances of a given class and then resets it"""
        try:
            return cls.cnt
        finally:
            cls.cnt = 0
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls
