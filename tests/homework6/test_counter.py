import pytest

from homework6.counter import instances_counter


@instances_counter
class User:
    pass


@pytest.fixture(scope='function')
def test_data_samples():
    """Creating sample instances"""
    user, _, _ = User(), User(), User()
    return user


def test_get_created_instances():
    """Testing that an instance counter of a class equals 0
    when the class doesn't have any instances"""
    assert User.get_created_instances() == 0


def test_get_created_instances_after_init(test_data_samples):
    """Testing that an instance counter of a class equals
    the number of created instances"""
    assert test_data_samples.get_created_instances() == 3
    test_data_samples.reset_instances_counter()


def test_reset_created_instances(test_data_samples):
    """Testing that an instance counter of a class got reset
    when reset_instances_counter() method called
    and after that the counter of created instances equals 0"""
    assert test_data_samples.reset_instances_counter() == 3
    assert test_data_samples.get_created_instances() == 0
