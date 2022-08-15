"""
def solution(scoville, K):
    scoville.sort()
    cnt=0
    while scoville[cnt] < K:
        cnt+=1
        scoville[cnt]= scoville[cnt-1]+scoville[cnt]*2
        if scoville[cnt]>scoville[cnt+1]:
            scoville[cnt],scoville[cnt+1]=scoville[cnt+1],scoville[cnt] 
            if scoville[cnt+1]>scoville[cnt+2]:
                scoville[cnt+1],scoville[cnt+2]=scoville[cnt+2],scoville[cnt+1]

    return cnt
"""
"""def solution(scoville, K):
    scoville.sort()
    cnt=0
    while scoville[0] < K:
        cnt+=1
        scoville[0]= scoville[1]+scoville[0]*2
        del scoville[1]
        scoville.sort()

    return cnt
"""
import heapq

def solution(scoville, K):
    cnt=0
    scoville.sort()
    min=heapq.heappop(scoville)
    while min<K:
        if len(scoville)<1: return -1
        heapq.heappush(scoville, min+heapq.heappop(scoville)*2)
        min=heapq.heappop(scoville)
        cnt+=1

    return cnt
# 100점


if __name__ == "__main__":
    print(solution([1,2,3,9,10,12], 7)) # 2
    print(solution([1,2,3], 11)) # 2