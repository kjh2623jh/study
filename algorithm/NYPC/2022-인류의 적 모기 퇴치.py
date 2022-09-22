m, n = map(int, input().split())
Map = []
cnt=-2
cnt_=-1
Cnt = []

for i in range(m):
    Map.append([*map(int, input().split())])

for i in range(m):
    for j in range(m):
        cnt+=2
        cnt_+=2
        Cnt.append(Map[i][j])
        Cnt.append(Map[i][j])
        for x in range(-n, n+1):
            if not x:
                continue
            if i+x>=0 and i+x<m:
                Cnt[cnt]+=Map[i+x][j]
                if j+x>=0 and j+x<m:
                    Cnt[cnt_]+=Map[i+x][j+x]
            if j+x>=0 and j+x<m:
                Cnt[cnt]+=Map[i][j+x]
                if i+x>=0 and i+x<m:
                    Cnt[cnt_]+=Map[i+x][j+x]

print(max(Cnt))
# for i in range(0, m*m, m):
#     print(Cnt[i:i+5], sep=' ')