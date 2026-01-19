# https://www.acmicpc.net/problem/10870

cache = [0, 1, 1, 2, 3, 5, ]
def fibo(n):
    if n < len(cache): return cache[n]
    cache.append(fibo(n-1) + fibo(n-2))
    return cache[n]

print(fibo(int(input())))

# 성공