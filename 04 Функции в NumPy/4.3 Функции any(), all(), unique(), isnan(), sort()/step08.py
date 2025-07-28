# https://stepik.org/lesson/1222856/step/8?unit=1236260

import numpy as np


def solution(arr):
    return np.sort(arr.reshape(4, 4))


arr = np.arange(16)
print(solution(arr))