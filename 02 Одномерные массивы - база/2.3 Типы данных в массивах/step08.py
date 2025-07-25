# https://stepik.org/lesson/1219560/step/8?unit=1232889

import numpy as np

def solution(arr: np.ndarray) -> np.ndarray:
    return np.array(arr * 3, dtype=int)


a = np.array([1.1, 2.2, .4])
print(solution(a))