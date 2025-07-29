# https://stepik.org/lesson/1232048/step/11?unit=1245632

import numpy as np


def solution(arr1, arr2, arr3):
    mask = arr1 == 0
    res_arr = arr1.copy()
    res_arr[mask] = np.abs(arr2[mask])
    res_arr[~mask] = arr2[~mask] * arr3[~mask]
    return res_arr


arr1 = np.arange(16)
arr2 = np.arange(1, 17)
arr3 = np.arange(2, 18)
print(arr1)
print(arr2)
print(arr3)
print(solution(arr1, arr2, arr3))