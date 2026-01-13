# https://www.acmicpc.net/problem/10814

users = []

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    users.append((age, name))

users.sort(key=lambda x: x[0])

for user in users:
    print(user[0], user[1])

# 100점