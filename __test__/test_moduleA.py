import numpy as np

from src.moduleA import sum_arrays


def test_sum_arrays():
    a = np.array([1., 2.])
    b = np.array([3., 4.])
    expected = np.array([4., 6.])

    res = sum_arrays(a=a, b=b)

    assert np.all(res == expected)
