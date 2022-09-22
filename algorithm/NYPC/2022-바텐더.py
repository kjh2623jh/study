'''
input()
p = sorted([*map(int, input().split())])
m = p.pop()
cnt = [0, 0, 0]
p = [m-i for i in p]
while p and p[-1] == 0:
    p.pop()
for i in p:
    if i%2:
        cnt[0]+=1
        i-=1
    if i%4:
        cnt[1]+=1
    cnt[2]+=i//4
print((max(cnt)-1)*3 + (3-cnt[::-1].index(max(cnt))))
'''

'''
from itertools import cycle

for i in cycle([1,2,4]):
    cnt+=1
    if i == 1:
        if p[-1]%2:
            p[-1]-=i
        elif p[-1] == 2:
            for iter in range(2, len(p)-2):
                if p[-iter]%2:
                    p[-iter]-=i
                    break
    elif i == 2:
        pass
    else:
        pass
    if p[-1] == 0:
        p.pop()
        if not p:
            break
print(cnt)
'''
input()
p = [*map(int, input().split())]
cnt = [0]*3
m = max(p)
for i in [m-x for x in p]:
    if i%2:
        cnt[0]+=1
        i-=1
    if i%4:
        cnt[1]+=1
    cnt[2]+=i//4
print((max(cnt)-1)*3 + (3-cnt[::-1].index(max(cnt))))