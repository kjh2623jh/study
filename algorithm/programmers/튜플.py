def solution(s):
    result = []
    s = s.split("},{")
    n = len(s)
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    for i in range(n):
        s[i] = s[i].split(',')
    s = sorted(s, key=len)

    for i in range(n):
        result.append(s[i][0])
        for j in range(i,n):         
            s[j].remove(result[-1])
    
    return list(map(int,result))


if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
    print(solution("{{20,111},{111}}")) # [111, 20]
    print(solution("{{123}}")) # [123]
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]


# 100점


'''
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
'''