# print(''.join(sorted(input(), reverse=True)))
print(*sorted(input())[::-1],sep='') # 언패킹