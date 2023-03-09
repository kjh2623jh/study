def solution(wallpaper):
    t, b, r, l = -1, 0, float("-inf"), float("inf")
    for i, aa in enumerate(wallpaper):
        for j, a in enumerate(aa):
            if a == '#':
                if t < 0: t = i
                b = i+1
                if l > j: l = j
                if r <= j: r = j+1
    return [t, l, b, r]

print(solution(["..", "#."]))


'''
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
'''