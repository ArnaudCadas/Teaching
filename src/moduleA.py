import numpy as np


def divide_arrays(a, b):
    return np.divide(a, b)


def sum_arrays(a, b, c):
    res = a + b + c
    print(f'Sum of {a}, {b} and {c}. The res is {res}')
    return res

def multiply_arrays(a, b):
    return np.multiply(a, b)
