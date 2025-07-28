# https://stepik.org/lesson/1232300/step/13?unit=1245886

import numpy as np


def solution(arr):
    mask = (arr >= 3) & (arr <= 7)
    arr[mask] = arr[mask]**2
    return np.abs(arr).T


arr = np.array(
    [[-1, -3, -7,  8],
     [-1, -3, 4,  8],
     [-1, -3, -7,  5],
     [-1, -3, -7,  8]]
)

print(solution(arr))