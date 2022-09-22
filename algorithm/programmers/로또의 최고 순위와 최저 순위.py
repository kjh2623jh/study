def solution(lottos, win_nums):
    posi = 0
    score = 0
    for i in lottos:
        if not i:
            posi+=1
        elif i in win_nums:
            score+=1
    rank = [6,6,5,4,3,2,1]
    return [rank[score+posi], rank[score]]

# 100점