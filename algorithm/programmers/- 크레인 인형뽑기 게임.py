def solution(board, moves):
    cnt=0
    line = {}
    bag = [0]
    for i in range(1, len(board)+1):
        line[i] = []
    for i in board[::-1]:
        for j in range(1, len(board)+1):
            if i[j-1] != 0:
                line[j].append(i[j-1])
    
    for i in moves:
        if line[i][-1]==[]:
            continue
        elif bag[-1] != line[i][-1]:
            bag.append(line[i].pop())
        else:
            bag.pop()
            cnt+=1
    
    return cnt*2


if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
    # result: 4

# 27.3점