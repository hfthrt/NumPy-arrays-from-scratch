# https://stepik.org/lesson/1232048/step/5?unit=1245632

import numpy as np


def solution(arr):
    return np.sum(arr[arr > 0])


arr = np.array([[1, 2, 3, 4], [-1, -2, -3, -4]])
print(solution(arr))