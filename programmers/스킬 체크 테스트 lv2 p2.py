"""
from math import gcd

def solution(w,h):
    n = gcd(w,h) # 최대 공약수
    c = w//n
    return w*h - c * 2 * (w//c)


채점 결과
정확성: 0.0
효율성: 0.0
합계: 0.0 / 50
"""


def solution(w,h):
    return 0



if __name__ == "__main__":
    print(solution(8, 12)) # 80