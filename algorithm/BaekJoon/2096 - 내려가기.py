# https://www.acmicpc.net/problem/2096
# https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2096%EB%B2%88-%EB%82%B4%EB%A0%A4%EA%B0%80%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
DP랑 Sliding Window가 뭔지 몰라서 풀이를 보고 이해했다.
꽤나 명쾌하고 재밌다
각 줄에서의 최댓값과 최솟값을 저장하면서
다음 줄로 넘어가면 그 이전 줄의 최댓값과 최솟값으로 값을 계산하는 식
그럼 마지막에는 각 줄의 모든 경우 중 최대와 최소만 남아있어서 출력하면 된다.
"""

from sys import stdin

N = int(input())
# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값을 설정한다.
arr = list(map(int, stdin.readline().split()))
maxDP = arr
minDP = arr
for _ in range(N - 1):
    arr = list(map(int, stdin.readline().split()))
    # 세가지 값을 입력받을 때마다, DP에 새롭게 갱신한다.
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))
