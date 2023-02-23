def solution(keymap, targets):
    result = []
    apb = {x : float('inf') for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for a in keymap:
        for num, b in enumerate(a):
            if apb[b] > num:
                apb[b] = num
    for a in targets:
        cnt = 0
        for b in a:
            cnt += apb[b]+1
        result.append(cnt if type(cnt) != float else -1)
    return result


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9, 4]