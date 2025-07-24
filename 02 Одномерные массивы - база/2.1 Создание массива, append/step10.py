# https://stepik.org/lesson/1216557/step/10?unit=1229834

import numpy as np


def solution(n) -> np.ndarray:
    if n > 0:
        return np.ones(n)
    return np.zeros(abs(n))

print(solution(3))