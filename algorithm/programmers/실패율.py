def solution(N, stages):
    result=[0]*N
    t=len(stages)
    for i in range(1,N+1):
        f=stages.count(i)
        result[i-1]=[i,f/t] if t !=0 else [i,0]
        t-=f
    for i in range(N):
        while i>0 and result[i-1][1]<result[i][1]:
            result[i-1],result[i]=result[i],result[i-1]
            i-=1
    return [x[0] for x in result]
# 100점


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
    print(solution(4, [4,4,4,4,4])) # [4,1,2,3]
    print(solution(3, [1,1,1]))


'''
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''