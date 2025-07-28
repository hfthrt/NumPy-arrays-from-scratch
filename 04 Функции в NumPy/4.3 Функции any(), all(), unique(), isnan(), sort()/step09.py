# https://stepik.org/lesson/1222856/step/9?unit=1236260

import numpy as np


def solution(arr):
    if not np.all(arr):
        arr[arr == 0] = 1
    return 1 / arr


arr = np.arange(16).reshape(4, 4)
print(solution(arr))