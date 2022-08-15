"""
def solution(s):
    for i in range(500000):
        s= s.replace(s[i%len(s)]*2,'')
        if s == '':
            return 1
    return 0

채점 결과
정확성: 15.2
효율성: 2.5
합계: 17.7 / 50
"""


"""
def solution(s):
    a = set(s)
    for i in a:
        s=s.replace(i*2,'')
    if s=='':
        return 1
    return 0

채점 결과
정확성: 20.1
효율성: 12.4
합계: 32.6 / 50
"""

def solution(s):


    return 0




if __name__ == "__main__":
    print(solution("baabaa")) # 1
    print(solution("cdcd")) # 0