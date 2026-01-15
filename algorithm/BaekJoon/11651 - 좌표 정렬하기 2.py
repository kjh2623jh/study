# https://www.acmicpc.net/problem/11651

from operator import itemgetter
import sys

input = sys.stdin.readline
[print(row[0], row[1]) for row in sorted([list(map(int, input().split())) for _ in range(int(input()))], key=itemgetter(1, 0))]

# sys.stdin.readlines()[1:] 이런 문법이 있네 어떻게 쓰는거지

# 100점