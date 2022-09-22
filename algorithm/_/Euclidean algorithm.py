a, b = map(int, input().split())
if b>a: b=a

while a%b!=0:
    a,b=b,a%b
print(b)