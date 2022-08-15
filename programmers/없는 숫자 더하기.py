def solution(numbers):
    return sum(set(range(10))-set(numbers))

if __name__ == "__main__":
    print(solution([1,2,3,4,6,7,8,0]))
    print(solution([5,8,4,0,6,7,9]))


# 100점

'''
def solution(numbers):
    return 45 - sum(numbers)


solution = lambda x: sum(range(10)) - sum(x)
'''