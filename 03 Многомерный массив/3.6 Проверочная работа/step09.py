# https://stepik.org/lesson/1232300/step/9?unit=1245886

import numpy as np


def solution(arr):
    return arr[(arr >= 4) | (arr % 3 == 0)]


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))
