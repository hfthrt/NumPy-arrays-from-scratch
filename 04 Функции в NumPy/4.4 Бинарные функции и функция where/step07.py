# https://stepik.org/lesson/1222886/step/7?unit=1236290

import numpy as np


def solution(arr):
    return np.where(arr < 0, np.abs(arr), 0)


arr = np.array([1, -2, 0, -3, 3, 4, 1, 0])
print(solution(arr))