M, F, N = map(int, input().split())
cnt = 1

if N == 0:
    print(0)
else:
    if F == 1:
        cnt = 0
    while F <= N:
        N -= M
        cnt += 1
    
    print(cnt) 
