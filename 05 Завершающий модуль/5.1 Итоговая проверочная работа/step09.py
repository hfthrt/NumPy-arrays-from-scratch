# https://stepik.org/lesson/1232048/step/9?unit=1245632

import numpy as np


# def solution(arr1, arr2):
#     max1 = arr1.max()
#     max2 = arr2.max()
#     new_arr = np.abs(np.append(arr1[arr1 == max1], arr2[arr2 == max2]))
#     return np.abs(np.mean(new_arr) - np.median(new_arr))


# def solution(arr1, arr2):
#     new_arr = np.abs(np.append(arr1, arr2))
#     return np.abs(np.mean(new_arr) - np.median(new_arr))

def solution(arr1, arr2):
    new_arr = np.abs(np.maximum(arr1, arr2))
    return np.abs(np.mean(new_arr) - np.median(new_arr))



arr = np.arange(16).reshape(4, 4)
print(arr)
print(solution(arr, arr.T))