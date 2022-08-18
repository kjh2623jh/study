n = int(input())
players = [int(x) for x in input().split()]
score = []

for lo in range(n-1):
    for hi in range(lo+1, n):
        score.append(sum(players[lo:hi]))

for i in range(n-2):
    for j in range(i+2, n):
        players_ = players[0:i]+players[i:j][::-1]+players[j:n-1]
        for lo in range(n-1):
            for hi in range(lo+1, n):
                score.append(sum(players_[lo:hi]))

print(max(score))

#이거 부르트 포스 아님 뭐로 풀어야하지?
# 그리디?..