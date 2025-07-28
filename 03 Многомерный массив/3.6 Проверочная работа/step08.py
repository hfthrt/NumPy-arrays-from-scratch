# https://stepik.org/lesson/1232300/step/8?unit=1245886

import numpy as np


def solution(arr):
    return arr.flatten()


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))
