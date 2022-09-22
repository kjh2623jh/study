def solution(answers):
    lnans = len(answers)
    p=[1,2,3,4,5]*(lnans//5+1), [2,1,2,3,2,4,2,5]*(lnans//8+1), [3,3,1,1,2,2,4,4,5,5]*(lnans//10+1)
    answer = [0,0,0]
    for i in range(3):
        for num in zip(answers, p[i]):
            if num[0]==num[1]: answer[i]+=1
    m=max(answer)
    for i in range(3):
        if answer[i]==m: answer.append(i+1)
    return answer[3:]

# 100점
    
if __name__ == "__main__":
    print(solution([1,2,3,4,5])) # [1]
    print(solution([1,3,2,4,2])) # [1, 2, 3]