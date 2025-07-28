# https://stepik.org/lesson/1232300/step/10?unit=1245886

import numpy as np


def solution(arr):
    return arr.T.astype(dtype=int)


arr = np.full((4, 4), '1')
print(arr)
print(solution(arr))