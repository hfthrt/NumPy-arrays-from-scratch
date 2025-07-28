# https://stepik.org/lesson/1220480/step/8?unit=1233811

import numpy as np

def solution(arr):
    return arr[(arr % 5 == 2) | (arr**3 < 100)]