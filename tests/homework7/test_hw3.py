from collections import namedtuple

import pytest

from homework7.hw3 import tic_tac_toe_checker

TestData = namedtuple('TestData', ['field_1', 'field_2', 'field_3', 'field_4'])


@pytest.fixture
def test_data():
    field_1 = [['o', 'x', 'x'], ['o', 'o', 'o'], ['x', 'o', 'x']]
    field_2 = [['x', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    field_3 = [['x', 'o', 'x'], ['x', 'x', 'o'], ['o', 'o', 'x']]
    field_4 = [['-', 'o', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    return TestData(field_1, field_2, field_3, field_4)


def test_tic_tac_toe_checker_o_victory(test_data):
    """Testing that function returns a correct result when o
    wins in a tic_tac_toe game"""
    assert tic_tac_toe_checker(test_data.field_1) == 'o wins!'


def test_tic_tac_toe_checker_x_victory(test_data):
    """Testing that function returns a correct result when x
    wins in a tic_tac_toe game"""
    assert tic_tac_toe_checker(test_data.field_2) == 'x wins!'


def test_tic_tac_toe_checker_draw(test_data):
    """Testing that function returns a correct result when
    game ends in a draw"""
    assert tic_tac_toe_checker(test_data.field_3) == 'draw!'


def test_tic_tac_toe_checker_unfinished(test_data):
    """Testing that function returns a correct result when
    the game is unfinished"""
    assert tic_tac_toe_checker(test_data.field_4) == 'unfinished!'
