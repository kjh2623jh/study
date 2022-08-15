solution=lambda a,b:["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]\
                    [([5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4][a-1]+b)%7-1]
# 100점


if __name__ == "__main__":
    print(solution(5, 24)) # "THU"