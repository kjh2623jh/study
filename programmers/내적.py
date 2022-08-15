def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])


if __name__ == "__main__":
    print(solution([1,2,3,4],[-3,-1,0,2]))
    print(solution([-1,0,1],[1,0,-1]))


# 100점

'''
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
'''