# https://www.acmicpc.net/problem/9012

import sys

for _ in range(int(sys.stdin.readline())):
    ps = sys.stdin.readline().strip()
    check = 0
    for char in ps:
        if char == '(':
            check += 1
        elif char == ')':
            check -= 1
            if check < 0:
                break
    if check == 0:
        print("YES")
    else:
        print("NO")

# 100점
