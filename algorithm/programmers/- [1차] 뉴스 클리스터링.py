from itertools import pairwise


def solution(str1, str2):
    pairwise(str1)
    pairwise(str2)



    return 0


if __name__ == "__main__":
    print(solution("FRANCE", "french")) # 16384
    print(solution("handshake", "shake hands")) # 65536
    print(solution("aa1+aa2", "AAAA12")) # 43690
    print(solution("E=M*C^2", "e=m*c^2")) # 65536


# 다중집합 구현을 어떻게 하지.