import heapq

def solution(jobs):
    arr=[]
    inp,req=map(list, zip(*sorted(jobs)))
    total_t=req[0]
    t_list = [total_t, ]
    d = {x:y for x,y in zip(req,inp)}

    for cnt in range(len(jobs)-1):
        p=cnt+1
        while inp[p]<req[cnt]:
            heapq.heappush(arr, req[p])
            p+=1
            if p>=len(inp)-cnt:break
        inp[cnt+1],inp[p-1]=inp[p-1],inp[cnt+1]
        req[cnt+1],req[p-1]=req[p-1],req[cnt+1]
        min=heapq.heappop(arr)
        total_t += min
        t_list.append(total_t-d[min])
        arr=[]

    return sum(t_list)//len(jobs)
# 5.0 / 100.0


if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]])) # 9
    print(solution([[0, 11], [2, 9], [2, 6]])) # 9