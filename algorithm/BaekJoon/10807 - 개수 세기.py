# https://www.acmicpc.net/problem/10807

input()
counter = {x:0 for x in range(201)}
for i in map(int, input().split()):
    counter[i+100] += 1
print(counter[int(input())+100])

# 성공


import sys

# 입력 전체를 한 번에 읽어서 문자열 리스트로 만듦
input_data = sys.stdin.read().split()

# input_data[0]은 n, input_data[-1]은 찾으려는 값 v
# 중간에 있는 데이터들(인덱스 1 ~ n)이 우리가 찾는 대상 리스트
target_list = input_data[1:-1]
v = input_data[-1]

# count 메서드는 문자열 상태에서도 동작하므로 굳이 int 변환 안 해도 됨!
print(target_list.count(v))

# ^ 재밌는 풀이