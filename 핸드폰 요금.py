from typing import MutableSet


N = int(input())
L = [a for a in map(int, input().split())]

m=0
y=0
for i in L:
    for _ in range(0,i,60):
        m+=15
    for _ in range(0,i,30):
        y+=10

if y==m:
    print(f"Y M {m}")
elif y>m:
    print(f"M {m}")
else:
    print(f"Y {y}")