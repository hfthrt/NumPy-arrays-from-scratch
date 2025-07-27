# https://stepik.org/lesson/1219565/step/9?unit=1232894
import numpy as np

def solution(arr):
    return arr[..., 1:3]


arr = np.arange(8).reshape(2, 4)
print(arr)
print(solution(arr))