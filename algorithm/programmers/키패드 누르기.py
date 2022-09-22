def solution(numbers, hand):
    key_pad = {}
    a=1
    b=1
    result = ''
    for i in range(10):
        if i == 0:
            key_pad[0] = [4,2]
        else:
            key_pad[i]=[a,b]
            b+=1
            if b > 3:
                a+=1
                b=1
    left_hand = [4,1]
    right_hand = [4,3]
    
    for key in numbers:
        pos = key_pad[key]
        if pos[1] == 1:
            left_hand = pos
            result+='L'
        elif pos[1] == 3:
            right_hand = pos
            result+='R'
        else:
            distanceL = abs(pos[0]-left_hand[0])+pos[1]-left_hand[1]
            distanceR = abs(pos[0]-right_hand[0])+right_hand[1]-pos[1]
            if distanceL < distanceR:
                left_hand = pos
                result+='L'
            elif distanceR < distanceL:
                right_hand = pos
                result+='R'
            else:
                if hand == 'right':
                    right_hand = pos
                    result+='R'
                else:
                    left_hand = pos
                    result+='L'
    
    return result


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))


# 100점