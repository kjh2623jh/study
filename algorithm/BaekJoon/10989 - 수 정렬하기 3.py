# https://www.acmicpc.net/problem/10989

import sys

input = sys.stdin.readline

N = int(input())
count = [0, ] * 10_000
for i in range(N):
    count[int(input())-1] += 1
for i in range(10_000):
    if count[i]:
        for j in range(count[i]):
            print(i+1)

# 100점