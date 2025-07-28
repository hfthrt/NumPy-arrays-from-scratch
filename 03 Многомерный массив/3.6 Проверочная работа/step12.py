# https://stepik.org/lesson/1232300/step/12?unit=1245886

import numpy as np


def solution(arr):
    return arr[[0, 1, 3, 3], [0, 1, 2, 0]]


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))
print(list(arr))