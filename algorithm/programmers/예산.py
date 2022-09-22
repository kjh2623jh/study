def solution(d, budget):
    cnt=0
    for i in sorted(d):
        if i>budget: break
        budget-=i
        cnt+=1
    return cnt
# 100점


if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9)) # 3
    print(solution([2,2,3,3], 10)) # 4


'''
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''