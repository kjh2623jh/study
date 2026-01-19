# https://www.acmicpc.net/problem/4153

a, b, c = map(lambda x: int(x)**2, input().split())
while (a+b+c):
    print("right"
        if  a+b == c or
            b+c == a or
            c+a == b
        else "wrong")

    a, b, c = map(lambda x: int(x)**2, input().split())