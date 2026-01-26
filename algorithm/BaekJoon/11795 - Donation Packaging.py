# https://www.acmicpc.net/problem/11795

package = [0, 0, 0]
for i in range(int(input())):
    for idx, num in enumerate(map(int, input().split())):
        package[idx] += num
    minn = min(package)
    if (minn >= 30):
        for idx in range(3):
            package[idx] -= minn
        print(minn)
    else: print("NO")

# 성공