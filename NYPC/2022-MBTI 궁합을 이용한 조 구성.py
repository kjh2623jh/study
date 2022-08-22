from collections import Counter

# ['enfp', 'enfj', 'entp', 'entj', 'esfp', 'esfj', 'estp', 'estj', 'infp', 'infj', 'intp', 'intj', 'isfp', 'isfj', 'istp', 'istj']

for _ in range(int(input())):
    number, m, b, t, i = map(int, input().split())
    cnt = 0
    mbti = Counter(input().split())
    pp = [[x for x in mbti if mbti[x]%2]]
    mbti = [m,b,t,i]
    for n, i in sorted(zip(mbti, range(4)), reverse=True)[:-1]:
        for j in range(len(pp)):
            if len(pp[j])<=2:
                break
            t = sorted(pp[j],key=lambda x: x[i])
            idx=len(t)//2
            if t[idx][i]!=t[idx-1][i]:
                pp[j]=[t[:idx],t[idx:]]
            else:
                pp[j]=[t[:idx+1],t[idx+1:]]
    t=0
    for g in pp:
        if len(g)>1:
            for i in range(4):
                if g[0][i] != g[1][i]:
                    cnt+=mbti[i]
        elif t:
            for i in range(4):
                if t[i] != g[0][i]:
                    cnt+=mbti[i]
        else:
            t = g[0]
    print(cnt)