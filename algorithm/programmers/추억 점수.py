'''
def solution(name, yearning, photo):
    return [sum([{n:y for n,y in zip(name, yearning)}.get(y, 0) for y in x]) for x in photo]
'''
solution = lambda name, yearning, photo: [sum([{n:y for n,y in zip(name, yearning)}.get(y, 0) for y in x]) for x in photo]



def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]