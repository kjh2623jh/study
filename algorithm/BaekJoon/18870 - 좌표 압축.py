# https://www.acmicpc.net/problem/18870

import bisect
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))

d = {}
for i, element in enumerate(sorted_arr):
    d[element] = i

for element in arr:
    # print(bisect.bisect_left(sorted_arr, element), end=' ')
    print(d[element])

