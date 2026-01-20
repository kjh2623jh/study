# https://www.acmicpc.net/problem/11729

def hanoi(number: int, prev: int, space: int, to: int) -> list:
    if number == 1: return [f"{prev} {to}"]
    return [*hanoi(number-1, prev, to, space), f"{prev} {to}", *hanoi(number-1, space, prev, to)]

result = hanoi(int(input()), 1, 2, 3)
print(len(result))
# print(result)
print("\n".join(result))

# 정답
# 메모리: 100512KB  시간: 560ms

memo = {}
def hanoi(number: int, prev: int, space: int, to: int) -> list:
    key = f"{number} {prev} {to}"
    if key in memo: return memo[key]
    elif number == 1: return [f"{prev} {to}"]
    memo[key] = [*hanoi(number-1, prev, to, space), f"{prev} {to}", *hanoi(number-1, space, prev, to)]
    return memo[key]

result = hanoi(int(input()), 1, 2, 3)
print(len(result))
print("\n".join(result))

# 정답
# 메모리: 68572KB   시간: 84ms