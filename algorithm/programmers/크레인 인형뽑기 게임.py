# def solution(board, moves):
#     cnt=0
#     line = {}
#     bag = [0]
#     for i in range(1, len(board)+1):
#         line[i] = []
#     for i in board[::-1]:
#         for j in range(1, len(board)+1):
#             if i[j-1] != 0:
#                 line[j].append(i[j-1])
    
#     for i in moves:
#         if line[i][-1]==[]:
#             continue
#         elif bag[-1] != line[i][-1]:
#             bag.append(line[i].pop())
#         else:
#             bag.pop()
#             cnt+=1
    
#     return cnt*2

# 27.3점

def solution(board, moves):
    result = 0
    stacks = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            idx = len(board) - i - 1
            if board[idx][j]:
                stacks[j].append(board[idx][j])
    # print(stacks)
    basket = []
    for move in moves:
        if not stacks[move-1]: continue
        cur = stacks[move-1].pop()
        if basket and basket[-1] == cur:
            basket.pop()
            result += 2
        else: basket.append(cur)
        # print(stacks, basket)

    return result


if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
    # result: 4

# 성공