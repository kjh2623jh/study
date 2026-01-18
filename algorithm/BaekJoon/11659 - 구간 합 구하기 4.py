# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [0, ] * (N+1)
for i, n in enumerate(map(int, input().split())):
    A[i+1] = A[i] + n
for i in range(M):
    i, j = map(int, input().split())
    print(A[j] - A[i-1])

# 정답