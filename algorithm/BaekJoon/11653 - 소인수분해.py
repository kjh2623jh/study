# https://www.acmicpc.net/problem/11653

N = int(input())
n = 2
while N > 1:
    d, m = divmod(N, n)
    if not m:
        print(n)
        N = d
        n = 2
    else: n += 1

# 성공