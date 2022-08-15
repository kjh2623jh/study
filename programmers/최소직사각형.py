def solution(sizes):
    a,b=zip(*[sorted(x) for x in sizes])
    return max(a)*max(b)
# 100점


if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133



'''
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
'''