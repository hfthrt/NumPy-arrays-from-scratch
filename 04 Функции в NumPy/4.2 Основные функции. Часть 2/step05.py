# https://stepik.org/lesson/1222855/step/5?unit=1236259

import numpy as np

def solution(arr):
    return np.floor(np.ceil(arr * 4.3) * 3.7)


arr = np.arange(9).reshape(3, 3)
print(arr)
print('-' * 100)
print(solution(arr))