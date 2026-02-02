# https://www.acmicpc.net/problem/11866

from collections import deque

N, K = map(int, input().split())
arr = deque(range(1, N+1))
result = []
for i in range(N):
    arr.rotate(-K+1)
    result.append(arr.popleft())
print(f"<{", ".join(map(str, result))}>")

# 성공