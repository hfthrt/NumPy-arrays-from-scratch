# https://stepik.org/lesson/1232048/step/8?unit=1245632

import numpy as np


def solution(arr):
    if arr.min() > arr.max():
        return np.mean(arr)
    return np.median(arr)


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))