def solution(n):
    to124 = [0,'1','2','4']
    idx=[]

    while 1:
        a,b = divmod(n,3)
        if b:
            idx.append(b)
            n=a
        else:
            idx.append(3)
            n=a-1
        if n<1:
            break

    return ''.join([to124[x] for x in idx][::-1])
#100점

if __name__ == "__main__":
    print(solution(1)) # 1
    print(solution(2)) # 2
    print(solution(3)) # 4
    print(solution(4)) # 11


'''
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]


def change124(n):
    return '' if n == 0 else change124((n - 1) // 3) + "412"[n % 3]
'''