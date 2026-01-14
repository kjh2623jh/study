# https://www.acmicpc.net/problem/10988

word = input()
print(1 if word == word[::-1] else 0)