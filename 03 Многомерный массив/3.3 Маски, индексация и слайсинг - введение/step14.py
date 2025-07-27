# https://stepik.org/lesson/1219565/step/14?unit=1232894
import numpy as np

def solution(arr):
    return sum(arr.diagonal())


arr = np.array([[1, 2, 30], [1, 2, 30], [1, 20, 3]])
print(arr)
print(solution(arr))