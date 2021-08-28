a=list(map(int,input().split()))
for i in range(6):
    if i<2:print(1-a[i],end=' ')
    elif i<5:print(2-a[i],end=' ')
    else:print(8-a[i],end=' ')