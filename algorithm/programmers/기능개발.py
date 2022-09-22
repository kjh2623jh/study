def solution(progresses, speeds):
    p = [(100-x)//y+1 if (100-x)%y else (100-x)//y for x,y in zip(progresses, speeds)]
    # p = [-((x-100)//y) for x,y in zip(progresses, speeds)]
    cnt = 0
    pnt = p[0]
    result = []
    for i in p:
        if i>pnt:
            result.append(cnt)
            pnt=i
            cnt=0
        cnt+=1
    result.append(cnt)
    return result

if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
    print(solution([70],[20]))


# 100점


'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''