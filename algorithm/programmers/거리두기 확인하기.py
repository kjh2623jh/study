def solution(places):
    result = []
    for place in places:
        c = 1
        for x in range(5):
            for y in range(5):
                if c == 1:
                    if place[x][y] == 'P':
                        if x != 0:
                            if place[x-1][y] == 'P': c=0
                        if x != 4:
                            if place[x+1][y] == 'P': c=0
                        if y != 0:
                            if place[x][y-1] == 'P': c=0
                        if y != 4:
                            if place[x][y+1] == 'P': c=0
                    elif place[x][y] == 'O':
                        if x != 0:
                            if place[x-1][y] == 'P': c+=1
                        if x != 4:
                            if place[x+1][y] == 'P': c+=1
                        if y != 0:
                            if place[x][y-1] == 'P': c+=1
                        if y != 4:
                            if place[x][y+1] == 'P': c+=1
                        c = 1 if c<3 else 0
        result.append(c)
    return result


if __name__ == "__main__":
    print(solution(
        [
            [
                "POOOP", 
                "OXXOX", 
                "OPXPX", 
                "OOXOX", 
                "POXXP"
            ], 
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
        )) # [1, 0, 1, 1, 1]


# 100점



'''
def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P':
                continue
            if irow != 4 and place[irow + 1][icol] == 'P':
                return 0
            if icol != 4 and place[irow][icol + 1] == 'P':
                return 0
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
                return 0
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
                return 0
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]
'''