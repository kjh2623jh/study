import numpy as np

def ii (n,nn):
    return list(map(lambda x: x+1 if x<n else x, nn))

def solution(n, left, right):
    num = 1
    li = np.array(range(1, n+1))
    lii = ii(num,li)
    while num!=n:
        num+=1
        lii = ii(num,lii)
        li = np.append(li, np.array(lii))
    return list(li[left:right+1])

print(solution(4, 7, 14))


'''
# import numpy as np
def ii (n,nn):
    return list(map(lambda x: x+1 if x<n else x, nn))
def solution(n, left, right):
    num = 1
    li = list(range(1, n+1))
    lii = ii(num,li)
    while num!=n:
        num+=1
        lii = ii(num,lii)
        for i in lii: li.append(i)
    return li[left:right+1]
print(solution(4, 7, 14))
'''

# 35점