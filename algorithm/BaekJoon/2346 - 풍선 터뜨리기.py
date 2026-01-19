# https://www.acmicpc.net/problem/2346

import collections

N = int(input())
deq = collections.deque(enumerate(map(int, input().split())))
for i in range(N):
    a, b = deq.popleft()
    print(a+1, end=" ")
    if b>0: b-=1
    deq.rotate(-b)