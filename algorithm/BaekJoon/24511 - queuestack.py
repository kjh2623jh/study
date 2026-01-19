# https://www.acmicpc.net/problem/24511

import sys
import collections
input = sys.stdin.readline
N = int(input())
A = map(int, input().split())
B = map(int, input().split())
qs = collections.deque(v for isS, v in zip(A, B) if not isS)
M = int(input())
qs.extendleft(map(int, input().split()))
for i in range(M): print(qs.pop(), end=" ")

# 성공