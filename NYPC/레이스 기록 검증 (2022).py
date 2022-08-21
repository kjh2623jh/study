p, n = map(int, input().split())
c = 0

p = [0]*p
for i in range(n):
    a, s, d = map(int, input().split())
    if d == 0 and p[s-1] == 0:
        p[s-1]=a
    elif a-p[s-1] < 60:
        c = 1
    elif p[s-1] != 0:
        p[s-1] = 0
    else:
        c = 1
if sum(p) > 0:
    c = 1
print("NO" if c else "YES")