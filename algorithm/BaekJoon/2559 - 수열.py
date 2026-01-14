# https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))
sums = []
sums.append(sum(temperatures[0:K]))
for i in range(1, N-K+1):
    sums.append(sums[-1] - temperatures[i-1] + temperatures[i-1+K])
print(max(sums))

# 100점