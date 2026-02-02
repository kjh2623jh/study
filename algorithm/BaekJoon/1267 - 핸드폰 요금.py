# https://www.acmicpc.net/problem/1267

input()
Y, M = 0, 0
for i in map(int, input().split()):
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
if Y == M: print("Y M", Y)
elif Y<M: print("Y", Y)
else: print("M", M)