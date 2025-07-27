# https://stepik.org/lesson/1219565/step/10?unit=1232894

import numpy as np

def solution(arr):
    first_column = arr[..., 0]
    second_column = arr[..., -1]
    # print(first_column)
    # print(second_column)
    return first_column == second_column


arr = np.arange(8).reshape(2, 4)
# print(arr)
print(solution(arr))