# https://stepik.org/lesson/1222855/step/6?unit=1236259

import numpy as np

def solution(arr):

    mean = np.mean(arr)
    median = np.median(arr)

    rules = {
        median > mean: np.floor
        , median == mean: np.round
        , median < mean: np.ceil
    }

    return rules[True](arr)


arr = np.random.rand(3, 3)
print(arr)
print('-' * 100)
print(solution(arr))