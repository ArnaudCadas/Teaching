import numpy as np


def divide_arrays(a, b):
    return np.divide(a, b)


def sum_arrays(a, b):
    res = a + b
    print(f'Sum of {a} and {b}. The res is {res}')
    return res
