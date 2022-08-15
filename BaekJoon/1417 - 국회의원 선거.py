def solution():
    n = int(input()) - 1
    m = int(input())
    if n == False: return 0
    a = [int(input()) for _ in range(n)]
    cnt=0

    while m <= max(a):
        m+=1
        a[a.index(max(a))]-=1
        cnt+=1
    
    return cnt

print(solution())