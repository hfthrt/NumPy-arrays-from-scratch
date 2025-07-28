# https://stepik.org/lesson/1222886/step/6?unit=1236290

import numpy as np


def solution(arr):
    return np.where(arr < 0, 0, 1).astype(bool)


arr = np.array([1, -2, 0, -3, 3, 4, 1, 0])
print(solution(arr))
