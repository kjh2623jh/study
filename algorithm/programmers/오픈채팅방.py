def solution(record):
    udict = {}
    result = []

    for txt in record:
        txt = txt.split()

        if txt[0] == 'Enter':
            udict[txt[1]] = txt[2]
        elif txt[0] == 'Change':
            udict[txt[1]] = txt[2]
    
    for txt in record:
        txt = txt.split()

        if txt[0] == 'Enter':
            result.append(f"{udict[txt[1]]}님이 들어왔습니다.")
        elif txt[0] == 'Leave':
            result.append(f"{udict[txt[1]]}님이 나갔습니다.")

    return result


'''
def solution(record):
    udict = {}
    result = []
    text = {'Enter':"님이 들어왔습니다.",'Leave':"님이 나갔습니다."}

    for txt in record:
        txt = txt.split()

        if txt[0] != 'Leave':
            udict[txt[1]] = txt[2]
    
    for txt in record:
        txt = txt.split()

        if txt[0] != 'Change':
            result.append(udict[txt[1]]+text[txt[0]])

    return result
'''


if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
    # return: ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


# 100점



'''
def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else
        f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]
'''