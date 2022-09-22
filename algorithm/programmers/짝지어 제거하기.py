# def solution(s):
#     t=[0]*(len(s)//2+1)
#     p=0
#     if len(s)%2!=0: return 0
#     try:
#         for i in s:
#             if p==0 or t[p-1]!=i:
#                 t[p]=i
#                 p+=1
#             else:
#                 p-=1
#         return 1
#     except IndexError:
#         return 0
'''
채점 결과
정확성: 44.8
효율성: 19.9
합계: 64.7 / 100.0
'''

def solution(s):
    t=[]
    if len(s)%2!=0: return 0
    for i in s:
        if t and t[-1]==i:
            t.pop()
        else:
            t.append(i)
    return 0 if t else 1
# 100점

print(solution('baabaa')) # 1
print(solution('cdcd')) # 0
print(solution('a')) # 0