# https://stepik.org/lesson/1216558/step/7?unit=1229835

import numpy as np

def solution(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return ((arr1**2 + arr2**2) / 2)**0.5


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(solution(a, b))