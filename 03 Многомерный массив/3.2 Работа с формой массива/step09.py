# https://stepik.org/lesson/1219593/step/9?unit=1232922

import numpy as np

def solution(arr: np.ndarray) -> np.ndarray:
    if arr.ndim >= 2:
        return arr.flatten()
    return arr.reshape((2, 2, 2, 2))