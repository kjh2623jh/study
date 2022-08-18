p, n = map(int, input().split())
c = 0

p = [0]*p
for i in range(n):
    a, b, c = map(int, input().split())
    if c == 0 and p[b-1] == 0:
        p[b-1]=a
    elif a-p[b-1] < 60:
        c = 1
    elif p[b-1] != 0:
        p[b-1] = 0
    else:
        c = 1
if sum(p) > 0:
    c = 1
print("NO" if c else "YES")