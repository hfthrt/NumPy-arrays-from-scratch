# https://stepik.org/lesson/1219565/step/13?unit=1232894

import numpy as np

def solution(arr):
    return arr[arr > 10]


arr = np.array([[1, 2, 30], [1, 2, 30], [1, 20, 3]])
print(arr)
print(solution(arr))