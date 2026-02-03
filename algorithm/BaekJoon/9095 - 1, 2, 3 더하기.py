# https://www.acmicpc.net/problem/9095

result = [0, 1, 2, 4, ]
a, b, c = 1, 2, 4
for i in range(7):
    a, b, c = b, c, a+b+c
    result.append(c)
for i in range(int(input())):
    print(result[int(input())])

# 성공 36ms

""" python 28ms """
d = [0] * 12
d[1:4] = [1,2,4]
for i in range(4,12):
    d[i] = sum(d[i-3:i])

for _ in range(int(input())):
    n = int(input())
    print(d[n])