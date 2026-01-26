# https://www.acmicpc.net/problem/15650


import itertools

N, M = map(int, input().split())
# for i in range(1, M-N+2):
#     for j in range(i, N+1):
#         print(i, j)
for s in itertools.combinations(range(1, N+1), M):
    # print(" ".join(map(str, s)))
    print(*s)

# 성공