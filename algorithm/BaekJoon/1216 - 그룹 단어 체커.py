# https://www.acmicpc.net/problem/1316

result = 0
for _ in range(int(input())):
    point = 0
    counter = [1, ]*26
    word = input()
    len_word = len(word)
    while point < len_word:
        while point != len_word-1 and word[point] == word[point+1]: point += 1
        idx = ord(word[point]) - 97
        if not counter[idx]: break
        counter[idx] = 0

        point += 1
    if point < len_word: continue
    result += 1
print(result)