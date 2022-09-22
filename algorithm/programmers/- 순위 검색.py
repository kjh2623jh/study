"""
def solution(info, query):
    info_dict = {
        '-': set(list(range(len(info)))),
        'cpp':set(),
        'python':set(),
        'java':set(),
        'backend':set(),
        'frontend':set(),
        'junior':set(),
        'senior':set(),
        'chicken':set(),
        'pizza':set(),
        'score':[]
    }
    result = []
    
    
    for i, j in enumerate(info):
        l, t, c, f, s = j.split()
        info_dict[l].update([i])
        info_dict[t].update([i])
        info_dict[c].update([i])
        info_dict[f].update([i])
        info_dict['score'].append(int(s))

    
    for i in query:
        l, t, c, f, s = i.replace('and','').split()
        result.append(len(info_dict[l] & info_dict[t] & info_dict[c] & info_dict[f] & set([x for x,y in enumerate(info_dict['score']) if y>=int(s)])))
    
    return result


정확성: 40.0 / 40.0
효율성: 0.0 / 60.0
합계: 40.0 / 100.0
"""

# binary search  (이진 검색)
def binarySearch(arr, number, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
    mid = (lo+hi)//2
    if lo>=hi:
        return mid
    if arr[mid] < number:
        return binarySearch(arr,number,mid+1,hi)
    elif arr[mid] > number:
        return binarySearch(arr,number,lo,mid-1)
    
    return mid

from bisect import bisect
def solution(info, query):
    info_dict = {
        '-': set(list(range(len(info)))),
        'cpp':set(),
        'python':set(),
        'java':set(),
        'backend':set(),
        'frontend':set(),
        'junior':set(),
        'senior':set(),
        'chicken':set(),
        'pizza':set()
    }
    score_dict = {}
    result = []
    
    
    for i, j in enumerate(info):
        l, t, c, f, s = j.split()
        info_dict[l].update([i])
        info_dict[t].update([i])
        info_dict[c].update([i])
        info_dict[f].update([i])
        try:
            score_dict[int(s)].append(i)
        except KeyError:    
            score_dict[int(s)] = [i]
    sorted_score = sorted(score_dict)
    # print(score_dict) # 150점이 두명인데 하나로 합쳐짐.
    # print(sorted_score)

    
    for i in query:
        l, t, c, f, s = i.replace('and','').split()
        score_set = set()
        # for j in score_dict[sorted_score[num]] for num in range(binarySearch(sorted_score, int(s), 0, len(sorted_score-1))):
        # print(binarySearch(sorted_score, int(s), 0, len(sorted_score)-1))
        for j in sorted_score[binarySearch(sorted_score, int(s)):]:
            for k in score_dict[j]:
                score_set.add(k)
        # result.append(len(info_dict[l] & info_dict[t] & info_dict[c] & info_dict[f] & set([x for x,y in enumerate(info_dict['score']) if y>=int(s)])))
        result.append(len(info_dict[l] & info_dict[t] & info_dict[c] & info_dict[f] & score_set))

        # a = binarySearch(sorted_score, int(s), 0, len(sorted_score)-1)
        # print(f"binary search: {a}")
        # for num in range(a,len(sorted_score)):
        #     print(f"num: {num}")
        #     print(f"sorted_score[num]: {sorted_score[num]}")
        #     print(f"score_dict[sorted_score[num]]: {score_dict[sorted_score[num]]}")

        # print(set([ score_dict[sorted_score[num]] for num in range( binarySearch( sorted_score, int(s), 0, len(sorted_score)-1), len(sorted_score) ) ]) )
        # print()
    
    return result


if __name__ == "__main__":
    print(solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150"
        ]
        ))  # [1,1,1,1,2,4]