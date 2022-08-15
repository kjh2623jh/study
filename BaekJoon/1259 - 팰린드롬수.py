while True:
    txt = input()
    if txt == '0':
        break
    else:
        if txt == txt[::-1]:
            print('yes')
        else:
            print('no')


'''
x = input()
while x != '0':
    print('yes' if x == x[::-1] else 'no')
    x = input()
    

while 1:
    i=input()
    if i=="0":break
    print(["no","yes"][i==i[::-1]])
'''