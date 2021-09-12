for _ in range(3):
    s=0
    for _ in range(int(input())):
        s+=int(input())
    if s<0:print('-')
    elif s>0:print('+')
    else:print(0)