# https://www.acmicpc.net/problem/28295

s = 0
for i in range(10):
    s+=int(input())
print(['N', 'E', 'S', 'W'][s%4])

# 성공