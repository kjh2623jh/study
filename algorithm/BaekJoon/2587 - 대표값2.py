# https://www.acmicpc.net/problem/2587

a = []
for _ in range(5):
    a.append(int(input()))
a.sort()
print(f"{int(sum(a)/5)}\n{a[2]}")