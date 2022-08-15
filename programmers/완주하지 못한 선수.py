"""
def solution(participant, completion):
    for i in completion:
        if i in participant:
            a = participant.index(i)
            del participant [a]
            
    answer = participant[0]
    
    return answer

정확성: 50.0
효율성: 0.0
합계: 50.0 / 100.0
"""
from collections import Counter

def solution(participant, completion):
    a = Counter()
    for i in participant:
        a[i]+=1
    for i in completion:
        a[i]-=1
    return a.most_common()[0][0]

# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0


if __name__=="__main__":
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"])) # "leo"
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])) # "vinko"
    print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])) # "mislav"


'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''