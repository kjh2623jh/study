def solution(cards1, cards2, goal):
    cards1.append(1)
    cards2.append(1)
    idx = [0, 0]
    for txt in goal:
        if cards1[idx[0]] == txt:
            idx[0] += 1
            continue
        if cards2[idx[1]] == txt:
            idx[1] += 1
            continue
        return "No"
    return "Yes"

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))


'''
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
'''