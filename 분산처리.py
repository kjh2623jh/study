data = []
for _ in range(int(input())):
    data.append(list(map(int, input().split())))

for a, b in data:
    c = 1
    s = ''
    for _ in range(4):
        c = int(str(c)[-1])*a
        s += str(c)[-1]
    print(s[b%4-1])