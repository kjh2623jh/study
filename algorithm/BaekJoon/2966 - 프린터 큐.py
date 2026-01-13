# https://www.acmicpc.net/problem/1966

import sys

def solve():
    num_file, index_file = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    counter = [0] * 9
    result = 0
    
    for p in priority:
        counter[p-1] += 1
    
    for c in range(9):
        while counter[8-c] > 0:
            while priority[0] != 9-c:
                priority.append(priority.pop(0))
                index_file -= 1
                if index_file < 0:
                    index_file = num_file - 1

            result += 1
            if index_file == 0:
                return result
            priority.pop(0)
            counter[8-c] -= 1
            num_file -= 1
            index_file -= 1
    return result
            

for _ in range(int(sys.stdin.readline())):
    print(solve())

# 100점