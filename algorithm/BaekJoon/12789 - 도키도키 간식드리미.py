# https://www.acmicpc.net/problem/12789

N = int(input())
stack = []
cur = 1

for n in map(int, input().split()):
    # print(f"stack: {stack}, cur: {cur}")
    if n == cur:
        cur += 1
    else:
        while stack and cur == stack[-1]:
            stack.pop()
            cur += 1
        stack.append(n)

# print(stack, sorted(stack, reverse=True))
print("Nice" if stack == sorted(stack, reverse=True) else "Sad")

# 성공