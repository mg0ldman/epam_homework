"""Calculate total sum of slow_calculate() of all numbers
starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function."""

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def fast_calculate(fun):
    """Speeds up the execution of slow_calculate"""
    with Pool(100) as p:
        return sum(p.imap(fun, range(501)))
