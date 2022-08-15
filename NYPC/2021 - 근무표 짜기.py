N, K = map(int, input().split())
day = list(map(int, input().split()))
maxPeople = list(map(int, input().split()))
dayDic = {}
for i, j in enumerate(day):
    dayDic.update({i+1:j})
a = []

for i in maxPeople:
    print(i, end=' ')
    for j in sorted(dayDic.values())[-i:]: print(j, end=' ')
    print() 