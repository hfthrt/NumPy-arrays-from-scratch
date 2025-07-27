# https://stepik.org/lesson/1219565/step/7?unit=1232894

import numpy as np

def solution(arr):
    return arr[-1, -1, -1]


a = np.arange(12).reshape(2, 2, 3)
print(a)
print(solution(a))