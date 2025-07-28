# https://stepik.org/lesson/1222854/step/6?unit=1236258

import numpy as np

def solution(arr):
    return np.argmax(arr)


arr = np.arange(9).reshape(3, 3)
print(arr)
print('-' * 100)
print(solution(arr))