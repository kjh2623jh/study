m, n = map(int, input().split())
Map = []
cnt=-1
Cnt = []

for i in range(m):
    Map.append([*map(int, input().split())])

for i in range(-n, m-n+1):
    for j in range(n, m+n+1):
        [y for x in Map[i:j+1] for y in x[i:j+1]]

print(max(Cnt))
# for i in range(0, m*m, m):
#     print(Cnt[i:i+5], sep=' ')