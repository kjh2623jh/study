# https://www.acmicpc.net/problem/1018

cWhite = 0b10101010 # 170
cBlack = 0b01010101 # 85
WBoard = [cWhite, cBlack, ] * 4
BBoard = [cBlack, cWhite, ] * 4

N, M = map(int, input().split())

board = []
for i in range(N):
    t = input()
    b = ''
    for c in t:
        if c == "W": b += "1"
        else : b += "0"

    board.append(b)

result_arr = []
for i in range(N-7):
    for j in range(M-7):
        count = 0
        pattern = WBoard if board[i][j] == "1" else BBoard
        for bit, row in zip(pattern, board[i:i+8]):
            count += (bit ^ int(row[j:j+8], 2)).bit_count()
        result_arr.append(min(64-count, count))
        
print(min(result_arr))

# 100점