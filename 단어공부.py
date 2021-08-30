a=sorted(input().upper())
b=''
l=[]
for i in a:
    if b[-1:]==i:
        b+=i
    else:
        l.append(b)
        b=i
l.append(b)
l=sorted(l,key=len)
print(l[-1][0] if len(l[-1]) != len(l[-2]) else '?')