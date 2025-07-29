# https://stepik.org/lesson/1232048/step/13?unit=1245632

import numpy as np


def solution(arr):
    return arr.flat[-1]


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]).reshape(4, 4)
print(arr)
print(solution(arr))