from time import time

from homework3.task02 import fast_calculate, slow_calculate


def test_fast_calculate_execution_time():
    """Testing that the execution time of slow_calculate is
     less than a minute"""
    start = time()
    fast_calculate(slow_calculate)
    end = time() - start
    assert end < 60
