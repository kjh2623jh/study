# https://www.acmicpc.net/problem/18245

WORD = input()
c = 2
while WORD != "Was it a cat I saw?":
    result = ''
    for idx in range(0, len(WORD), c):
        result += WORD[idx]
    print(result)
    c+=1
    WORD = input()

# 성공