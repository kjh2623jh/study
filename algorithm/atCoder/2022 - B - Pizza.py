n = int(input())
degree = list(map(int, input().split()))
circle = [0, ]

for i in degree:
    for j in range(len(circle)):
        circle[j] = (circle[j] + i)%360
    circle.append(0)
circle.sort()

a = [circle[i+1] - circle[i] for i in range(n)]
a.append(360 - circle[-1])

print(max(a))
