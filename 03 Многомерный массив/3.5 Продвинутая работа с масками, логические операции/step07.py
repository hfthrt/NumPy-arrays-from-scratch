# https://stepik.org/lesson/1220480/step/7?unit=1233811

import numpy as np

def solution(arr):
    mask1 = arr % 3 == 0
    mask2 = abs(arr * 3) > 40
    return arr[mask1 & mask2]


arr = np.array([[-1, 2], [30, 4], [1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]])
print(solution(arr))
