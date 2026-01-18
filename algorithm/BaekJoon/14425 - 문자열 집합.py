# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input() for i in range(N))
count = 0
for i in [input() for _ in range(M)]:
    if i in S: count += 1
print(count)

# 100점