def move(pos):
    if pos[1] == 'e':
        return pos[0][0]+str(int(pos[0][1])+1)
    elif pos[1] == 's':
        return str(int(pos[0][0]+1))+pos[0][1]
    elif pos[1] == 'w':
        return pos[0][0]+str(int(pos[0][1])-1)
    else: # 'n'
        return str(int(pos[0][0]-1))+pos[0][1]

def is_out_of_range():
    pass

def solution(grid): # ["SL","LR"]
    eswn = list(_ for _ in enumerate(['e', 's', 'w', 'n']))
    route = []
    dic = {}

    for i, value1 in enumerate(grid):
        for j, value2 in enumerate(value1):
            dic.update({str(i)+str(j) : value2})

    for row in range(len(grid)):
        for column in range(len(grid)):
            for dirc in range(len(eswn)):
                pos = ['00', dirc]

                while pos not in route:
                    if dic[pos[0]] == 'S':
                        pos[0] = move(pos)
                    elif pos[0] == 'L':
                        pos[1] = eswn
                        pos[0] = move(pos)
                    else: # 'R'
                        pass