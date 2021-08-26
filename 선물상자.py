N, M = map(int, input().split())
D = list(map(int, input().split()))
DD = {}
for i, j in enumerate(D):
    DD.update({i+1:j})

while len(DD) > 1:
    for i in range(1, len(DD)+1):
        DD[i] -= 1
        if DD[i] < 1:
            DD.pop(i)

print(list(DD.keys())[0])
