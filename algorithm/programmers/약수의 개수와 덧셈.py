def solution(left, right):
    result=0
    for num in range(left, right+1):
        cnt=0
        for i in range(1,num+1):
            if num%i==0: cnt+=1
        result += num if cnt%2==0 else -num
    return result
# 100점


# solution=lambda l,r:sum([-n if int(n**.5)==n**.5 else n for n in range(l,r+1)])

if __name__ == "__main__":
    print(solution(13, 17)) # 43
    print(solution(24, 27)) # 52



'''
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''