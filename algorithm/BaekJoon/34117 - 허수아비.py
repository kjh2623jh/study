# https://www.acmicpc.net/problem/34117

# import heapq
# import sys

# input = sys.stdin.readline

# heap = []
# N, P = map(int, input().split())
# for number in map(int, input().split()):
#     heapq.heappush(heap, -number)

#     sum_ = 0
#     cnt = 0
#     heap_copy = heap.copy()
#     while heap_copy and sum_ < P:
#         sum_ += -heapq.heappop(heap_copy)
#         cnt += 1
#     if sum_ < P: cnt = -1
#     print(cnt, end=' ')

# 잘 모르겠어서 다른사람 풀이를 봤다
# https://anginjunddi.tistory.com/71

# 새로 들어오는 값을 계속 더해주면서
# 힙의 최솟값들을 P에 맞춰 계속 빼준다면
# 최대한 적은 개수의 숫자의 합으로 구할 수 있다.

"""
일단 순서대로 숫자를 s라는 변수에 다 더해준다.
만약 s 가 P를 초과하게 된다면
    우선순위큐(heapq) 자료구조에서 값이 작은 값을 하나씩 꺼내서 빼주면서
    최대한 적은 개수의 숫자들로 P이상의 s를 만들면 된다.
"""

import heapq
import sys
input = sys.stdin.readline

N, P = map(int, input().split())

s = 0
cnt = 0
heap = []

for x in map(int, input().split()):
    heapq.heappush(heap, x)
    s+=x
    cnt+=1

    while len(heap) > 1:
        a = heapq.heappop(heap)
        if s - a >= P:
            s-=a
            cnt-=1
        else:
            heapq.heappush(heap, a)
            break
    if s >= P:
        print(cnt, end = ' ')
    else:
        print(-1, end = ' ')