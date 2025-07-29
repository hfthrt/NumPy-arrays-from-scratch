# https://stepik.org/lesson/1232048/step/10?unit=1245632

import numpy as np


def solution(arr):
    return np.sort(arr, axis=0)[1, :3]


arr = np.arange(16).reshape(4, 4)
print(arr.T)
print(solution(arr.T))