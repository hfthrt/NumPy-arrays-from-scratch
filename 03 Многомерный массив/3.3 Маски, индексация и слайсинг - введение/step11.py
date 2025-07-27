# https://stepik.org/lesson/1219565/step/11?unit=1232894

import numpy as np

def solution(arr):
    return arr[1:3, 1:3]


arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr))