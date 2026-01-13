# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

raw_string = input().strip()
bomb = input().strip()

stack = []

for char in raw_string:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print("FRULA")