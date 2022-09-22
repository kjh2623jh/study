txts = [input() for _ in range(int(input()))]

result = list(txts[0])
for txt in txts:
    for i in range(len(txt)):
        if result[i] != txt[i]:
            result[i] = '?'

print(''.join(result))