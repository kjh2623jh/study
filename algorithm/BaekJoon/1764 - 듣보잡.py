# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.readline
듣, 보 = map(int, input().split())
d_s = set()
b_s = set()
for i in range(듣):
    d_s.add(input().strip())
for i in range(보):
    b_s.add(input().strip())
db_set = d_s & b_s
print("\n".join([str(len(db_set)), *sorted(db_set)]))