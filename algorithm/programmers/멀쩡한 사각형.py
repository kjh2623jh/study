from math import gcd
solution=lambda w,h:w*h - (w+h-gcd(w,h))
#100점

print(solution(8, 12)) # 80


'''
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)
'''