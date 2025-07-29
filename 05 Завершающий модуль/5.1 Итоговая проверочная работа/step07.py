# https://stepik.org/lesson/1232048/step/7?unit=1245632

import numpy as np


def solution(arr1, arr2):
    return np.sort(arr1) == np.sort(arr2)


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr, arr.T))