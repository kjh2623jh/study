# https://www.acmicpc.net/problem/1003

memo = [[1, 0], [0, 1], [1, 1], [1, 2]]
def custom_fibo(n):
    if len(memo) <= n: memo.append([x+y for x, y in zip(custom_fibo(n-1), custom_fibo(n-2))])
    return memo[n]
for i in range(int(input())):
    print(*custom_fibo(int(input())))

# 성공 32ms

""" python 28ms 코드 """
import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    n=int(input())
    zero, one=1,0
    for i in range(n):
        zero, one= one, one+zero
    print(zero, one)