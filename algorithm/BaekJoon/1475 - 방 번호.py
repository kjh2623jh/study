from math import ceil
def solution(n):
    # n = int(input())
    n = list(str(n).replace('6','9'))
    return int(max([n.count(i) if i != '9' else ceil(n.count('9')/2) for i in n]))

if __name__ == "__main__":
    print(solution(9999)) # 2
    print(solution(122)) # 2
    print(solution(12639)) # 1
    print(solution(888888)) # 6
    print(solution(999)) # 6


# from math import ceil
# n = list(input().replace('6','9'))
# print(int(max([n.count(i) if i != '9' else ceil(n.count('9')/2) for i in n])))


# 성공


'''
a=[0]*9
for d in input():a[int(d)-(d>'8')*3]-=1
a[6]//=2;print(-min(a))

c=input().count
print(max(int(max(map(c,'01234578'))),(c('6')+c('9')+1)//2))

s=input().count;print(max([(s('6')+s('9')+1)//2]+[s(i) for i in "01234578"]))
'''