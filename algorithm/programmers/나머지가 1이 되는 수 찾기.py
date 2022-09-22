solution=lambda n:min(x for x in range(2,n) if n%x==1)
# 100점


if __name__ == "__main__":
    print(solution(10)) # 3
    print(solution(12)) # 11