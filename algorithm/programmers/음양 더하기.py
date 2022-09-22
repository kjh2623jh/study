def solution(absolutes, signs):
    result = 0
    for a,b in zip(absolutes,signs):
        if b:
            result+=a
        else:
            result-=a
    
    return result


if __name__ == "__main__":
    print(solution([4,7,12],[True,False,True]))
    print(solution([1,2,3],[False,False,True]))


# 100점

'''
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''