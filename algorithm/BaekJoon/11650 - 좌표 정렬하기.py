# https://www.acmicpc.net/problem/11650

from operator import itemgetter
import sys

l = []

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    l.append((x, y))

l.sort(key=itemgetter(0, 1))

for point in l:
    print(point[0], point[1])

# 100점