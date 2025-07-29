# https://stepik.org/lesson/1232048/step/6?unit=1245632

import numpy as np


def solution(arr):
    return np.max(arr, axis=0)


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))