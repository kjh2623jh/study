from collections import Counter

['enfp', 'enfj', 'entp', 'entj', 'esfp', 'esfj', 'estp', 'estj', 'infp', 'infj', 'intp', 'intj', 'isfp', 'isfj', 'istp', 'istj']

for _ in range(int(input())):
    number, m, b, t, i = map(int, input().split())
    cnt = []
    mbti = Counter(input().split())
    pp = [x for x in mbti if mbti[x]%2]
    mbti = [m,b,t,i]
    for n, i in sorted(zip(mbti, range(4)), reverse=True):
        ...