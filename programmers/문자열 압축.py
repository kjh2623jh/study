def solution(s):
    result=[]
    for i in range(1,len(s)//2+1):
        txt = [s[x:x+i] for x in range(0, len(s), i)]
        c=0
        r=''
        for t in range(len(txt)-1):
            if txt[t]==txt[t+1]:
                c+=1
            else:
                r+=f"{c+1 if c else ''}{txt[t]}"
                c=0
        r+=f"{c+1 if c else ''}{txt[t+1]}"
        result.append(len(r))

    return 1 if result==[] else min(result)
# 100점


if __name__ == "__main__":
    print(solution("aabbaccc")) # 7
    print(solution("ababcdcdababcdcd")) # 9
    print(solution("abcabcdede")) # 8
    print(solution("abcabcabcabcdededededede")) # 14
    print(solution("xababcdcdababcdcd")) # 17
    print(solution("a")) # 1