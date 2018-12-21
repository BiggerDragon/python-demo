import doctest


def average(values):
    """Computing arithmetic number of a list of numbers.
    >>> print(average([20,30,40]))
    30.0
    """
    return sum(values)/len(values)

doctest.testmod()

import re

def is_correct_id_no(id_no):
    """Tell if the given id no is correct!
    >>> is_correct_id_no("000")
    False
    >>> is_correct_id_no("")
    False
    >>> is_correct_id_no("411524199507037213")
    True
    >>> is_correct_id_no("YYsssYYYuu12345678")
    False
    """
    reg = "[0-9]{17}[xX0-9]"
    if re.match(reg, id_no):
        return True
    else:
        return False

doctest.testmod()


