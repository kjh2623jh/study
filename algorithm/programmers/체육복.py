from bisect import bisect

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    lost,reserve = [*set(lost)-s], [*set(reserve)-s]
    lost.sort()
    reserve.sort()
    num=0

    for s in lost:
        idx = bisect(reserve, s)
        if idx>0 and reserve[idx-1] == s-1:
            del reserve[idx-1]
            num+=1
        elif idx<len(reserve) and reserve[idx] == s+1:
            del reserve[idx]
            num+=1
        
    return n-(len(lost)-num)
# 100점


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5])) # 5
    print(solution(5, [2, 4], [3])) # 4
    print(solution(3, [3], [1])) # 2


'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''