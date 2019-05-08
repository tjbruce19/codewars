from functools import reduce
from math import gcd
def solution(a):
    init_len = len(a)
    while True:
        a = sorted(list(set(a)))
        if len(a) == 1:
            break
        for i in range(1, len(a)):
            a[i] = a[i] - a[i - 1] if a[i] > a[i - 1] else (a[i - 1] - a[i])
    return a[0] * init_len

a = [6, 9, 12]

def optimize_solution(a):
    return reduce(gcd,a) * len(a)
print(optimize_solution(a))