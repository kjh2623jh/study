a = []
b = {}
N, M = map(int, input().split())
for _ in range(M):
    a.append(list(map(int, input().split())))

try:
    for t, i, s in a:
        if s:
            if t - b.pop(i) < 60: raise KeyError
        else:
            if i in b: raise KeyError
            else:
                b.update({i:t})
    if b: raise KeyError
except KeyError: print("NO")
else: print("YES")