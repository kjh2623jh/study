# https://www.acmicpc.net/problem/1436

number = int(input())
count = 0
for i in range(666, 3_000_000):
    if '666' in str(i): count += 1
    if count == number: break
print(i)