from collections import Counter

for _ in range(int(input())):
    number, i, n, f, p = map(int, input().split())
    pp = []
    cnt = []
    mbti = Counter()
    for aa in input().split():
        mbti[aa] +=1
    for aa in mbti:
        if mbti[aa]%2:
            pp.append(mbti[aa])
    
    '''
    mbti = [i,n,f,p]
    for aa in range(0, len(pp)-1):
        for bb in range(aa+1, len(pp)):
            c=0
            for x in range(4):
                if pp[aa][x] != pp[bb][x]:
                    c+=mbti[x]
            cnt.append(c)
    '''