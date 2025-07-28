# https://stepik.org/lesson/1219566/step/4?unit=1232895

import numpy as np

def solution(a, b, arr):
    return arr[:, [a, b]]


arr = np.arange(25).reshape(5, 5)
print(arr)
print(solution(1, 3, arr))