# https://www.acmicpc.net/problem/2751

from heapq import heappush, heappop
import sys

heap = []

for _ in range(int(sys.stdin.readline())):
    heappush(heap, int(sys.stdin.readline()))

while heap:
    print(heappop(heap))

# 100점