# https://stepik.org/lesson/1219565/step/12?unit=1232894
import numpy as np

def solution(arr):
    return arr.T[:2, 1:]


arr = np.arange(9).reshape(3, 3)
print(arr)
print(arr.T)
print(solution(arr))