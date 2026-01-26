# https://www.acmicpc.net/problem/26332

for i in range(int(input())):
    amount, price = map(int, input().split())
    print(amount, price)
    print(price*amount-(amount-1)*2)