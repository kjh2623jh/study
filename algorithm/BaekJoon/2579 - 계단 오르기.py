# https://www.acmicpc.net/problem/2579

# top-down으로 ㄱㄱ
# ? bottom-top으로 해야하나?

# 현재기준 앞에 4개 계단에 대해서 최솟값을 뛰어넘으면

# 배열에 3가지 max를 넣는다
# [ 3연속, 12연속 23연속 ]

# staires_max[current] = max([
#     staires[current] + staires[current-1] / 23연속일 때 가능 / + staires[current-2] / 12연속일 떄 가능 /,
#     staires[current] + staires[current-2] / 3연속, 23연속일 때 가능 / + staires[current-3] / 23연속, 12연속일 떄 가능 /, ((3, 23), (23, 12)) 이렇게 연결돼야함
#     staires[current] + staires[current-1] / 12연속일 떄 가능 / + staires[current-3] / 다 가능 /,
# ])

# 아니 최대 2번 연속이었네
# [ 2dus, 띈거 ]

import sys
input = sys.stdin.readline

max_staires = [[0, 0], [0, 0]]

for _ in range(int(input())):
    staire_value = int(input())
    max_staires.append([
        staire_value + max_staires[-1][1],
        staire_value + max(max_staires[-2])
    ])
print(max(max_staires[-1]))