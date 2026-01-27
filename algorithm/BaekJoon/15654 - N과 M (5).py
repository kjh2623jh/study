# https://www.acmicpc.net/problem/15654

import itertools

N, M = map(int, input().split())
# for x in sorted(list(set(itertools.permutations(map(int, input().split()), M)))):
    # print(*x)

for x in sorted(itertools.permutations(map(int, input().split()), M)): print(*x)

# 성공