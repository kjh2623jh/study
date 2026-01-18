# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline
n = int(input())
dp = [[0,0,0],]*(n+2)
for i in range(2, n+2):
    number = input()
    dp[i] = [
        int(number) + max(dp[i-1][1:3]),
        int(number) + max(dp[i-2]),
        int(number) + max(dp[i-3]),
    ]
# print(dp)
print(max(*dp[n+1], *dp[n]))

# 성공