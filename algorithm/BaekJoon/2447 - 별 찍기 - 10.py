# https://www.acmicpc.net/problem/2447

def draw_star(n):
    number = n//3
    if number == 1: return ["***", "* *", "***"]

    prev_star = draw_star(number)
    result = []
    for i in prev_star: result.append(i*3)
    for i in prev_star: result.append(i + " "*(number) + i)
    for i in prev_star: result.append(i*3)
    return result

print("\n".join(draw_star(int(input()))))

# 성공