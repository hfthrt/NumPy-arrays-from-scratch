# https://stepik.org/lesson/1219593/step/8?unit=1232922

import numpy as np

def solution(arr: np.ndarray) -> np.ndarray:
    return arr.reshape(-1)

arr = np.ones((4, 4, 4))
print(solution(arr))