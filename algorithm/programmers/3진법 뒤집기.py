def to3(n):
    q, r = divmod(n,3)
    if q==0: return str(r)
    else: return to3(q)+str(r)

def solution(n):
    return int(to3(n)[::-1],3)
# 100점


if __name__ == "__main__":
    print(solution(45)) # 7
    print(solution(125)) # 229


'''
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
'''