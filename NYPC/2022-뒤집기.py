n = int(input())
players = [int(x) for x in input().split()]
score = [0]

num=0
for i in players:
    num+=i
    if num<0:
        num=0
    elif num>score[-1]:
        score[-1]=num

for i in range(n-1):
    for j in range(i+2, n+1):
        players_ = players[0:i]+players[i:j][::-1]+players[j:n]
        score.append(0)
        num=0
        for p in players_:
            num+=p
            if num<0:
                num=0
            elif num>score[-1]:
                score[-1]=num

r = max(score)
print(r if r>0 else max(players))
# 시간