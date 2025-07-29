# https://stepik.org/lesson/1232048/step/12?unit=1245632

import numpy as np


def solution(arr1, arr2):
    res = arr1 == arr2
    if np.all(res):
        return -1
    return np.sum(res)


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr, arr))