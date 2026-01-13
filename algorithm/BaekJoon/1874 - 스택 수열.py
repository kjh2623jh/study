# https://www.acmicpc.net/problem/1874

import sys

head = 0
stack = []
resultstr = ""

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    while head < num:
        head += 1
        stack.append(head)
        resultstr += "+\n"
    popped = stack.pop()
    resultstr += "-\n"
    if popped != num:
        resultstr = "NO"
        break

print(resultstr.strip())