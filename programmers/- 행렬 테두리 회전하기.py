def printl(l):
    for i in l:
        print(''.join(['{:3}'.format(x) for x in map(str, i)]))
    print()

def solution(rows, columns, queries):
    result=[]
    mapl = [[j+1 for j in range(columns*i,columns*i+columns)] for i in range(rows)]
    printl(mapl)
    return ''
    if len(queries)==1:
        result.append(mapl[queries[0][0]-1][queries[0][1]-1])
    else:
        for pos in queries:
            r1,c1,r2,c2=pos[0]-1,pos[1]-1,pos[2]-1,pos[3]-1
            minl=[]
            temp=mapl[r1][c1]
            temp2=mapl[r2][c2]
            minl.append(mapl[r1][c2])
            minl.append(mapl[r2][c1])
            for i in range(r2-r1):
                minl.append(mapl[r1+i][c1])
                minl.append(mapl[r2-i][c2])
                mapl[r1+i][c1]=mapl[r1+i+1][c1]
                mapl[r2-i][c2]=mapl[r2-i-1][c2]
            for i in range(c2-c1-1):
                minl.append(mapl[r1][c1+i])
                minl.append(mapl[r2][c2-i])
                mapl[r2][c1+i]=mapl[r2][c1+i+1]
                mapl[r1][c2-i]=mapl[r1][c2-i-1]
            mapl[r1][c1+1]=temp
            mapl[r2][c2-1]=temp2
            result.append(min(minl))
    
    return result


# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
# print(solution(100, 97, [[1,1,100,97]])) # [1]
print(solution(6,8,[]))