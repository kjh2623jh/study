# https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())
d, m = divmod(V-A, A-B)
print(d + (2 if m else 1))

# 100점