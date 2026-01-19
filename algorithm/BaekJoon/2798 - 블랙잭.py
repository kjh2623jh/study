# https://www.acmicpc.net/problem/2798

import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
max_n = 0
for x in itertools.combinations(A, 3):
    sum_x = sum(x)
    if sum_x > M: continue
    max_n = max(sum_x, max_n)
print(max_n)