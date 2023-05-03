for num in range(1, 999999999):
    camp = input()
    if camp == "0 0 0":
        break
    L, P, V = map(int, camp.split())
    print(f"Case {num}: {L*(V//P) + (V%P if V%P < L else L)}")
    # print(f"Case {num}: {L*(V//P) + min(L, V%P)}")

'''
j=0
for i in[*open(0)][:-1]:
    j+=1
    L,P,V=map(int,i.split())
    x=0
    while V>0:
        x+=min(L,V)
        V-=P
    print(f"Case {j}: {x}")
'''

'''
j=1
while(i:=input())>"1":L,P,V=map(int,i.split());print(f"Case {j}: {V//P*L+min(L,V%P)}");j+=1
'''