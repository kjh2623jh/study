'''
def solution(nums):
    m=len(nums)//2
    nums.append(0)
    nums=[nums[x] for x in range(len(nums)-1) if nums[x]!=nums[x+1]]
    return min(m,len(nums))

정확성: 40.0
합계: 40.0 / 100.0
'''
def solution(nums):
    m=len(nums)//2
    nums=set(nums)
    return min(m,len(nums))
# 100점

if __name__ == "__main__":
    print(solution([3,1,2,3])) # 2
    print(solution([3,3,3,2,2,4])) # 3
    print(solution([3,3,3,2,2,2])) # 2


'''
solution = lambda nums: min(len(nums)/2, len(set(nums)))
'''