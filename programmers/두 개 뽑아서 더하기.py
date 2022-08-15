solution=lambda n: sorted([*set(n[i]+j for i in range(len(n)-1) for j in n[i+1:])])
# 100점


if __name__ == "__main__":
    print(solution([2,1,3,4,1])) # [2,3,4,5,6,7]
    print(solution([5,0,2,7])) # [2,5,7,9,12]