a=int(input())
b=0
k=0
while b < a:
    k+=1
    b+=k
print(f'{a-b+k}/{b-a+1}' if k%2==0 else f'{b-a+1}/{a-b+k}')