# https://stepik.org/lesson/1222854/step/5?unit=1236258

import numpy as np

def solution(arr):
    new_arr = arr[:, [0, 2, 4]]
    new_arr = new_arr[new_arr < 15]
    return np.sum(new_arr**2)


arr = np.random.rand(5, 5)
print(arr)
print('-' * 100)

print(solution(arr))