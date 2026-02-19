# https://www.acmicpc.net/problem/34115

N = int(input())
count = [-1]*2_001
find_max = 0
for idx, number in enumerate(map(int, input().split())):
    if count[number] == -1: count[number] = idx
    else: find_max = max(idx - count[number] - 1, find_max)
print(find_max)

# 성공