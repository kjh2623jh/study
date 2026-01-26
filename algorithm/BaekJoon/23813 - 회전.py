# https://www.acmicpc.net/problem/23813

N = input()
numbers = []
for i in range(len(N)):
    N = N[-1]+N[:-1]
    numbers.append(N)
print(sum(map(int, numbers)))

# 성공